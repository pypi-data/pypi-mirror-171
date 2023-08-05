import json
import os
from typing import Dict, Optional

import hubble
from docarray import Document, DocumentArray
from jina import __version__ as jina_version
from now_common.preprocess import preprocess_nested_docs, preprocess_text
from now_common.utils import get_indexer_config

from now.apps.base.app import JinaNOWApp
from now.constants import NOW_PREPROCESSOR_VERSION, Apps, Modalities, ModelNames
from now.finetuning.data_builder import DataBuilder
from now.finetuning.run_finetuning import finetune
from now.finetuning.settings import FinetuneSettings, parse_finetune_settings
from now.now_dataclasses import Task, UserInput


class TextToTextAndImage(JinaNOWApp):
    """
    Hybrid text to text+image search combining symbolic and neural IR approaches.
    """

    def __init__(self):
        super().__init__()

    @property
    def app_name(self) -> Apps:
        return Apps.TEXT_TO_TEXT_AND_IMAGE

    @property
    def is_enabled(self) -> bool:
        return True

    @property
    def description(self) -> str:
        return (
            'Text to text+image search app combining symbolic and neural IR approaches.'
        )

    def set_flow_yaml(self, **kwargs):
        """configure the flow yaml in the Jina NOW app."""
        flow_dir = os.path.abspath(os.path.join(__file__, '..'))
        self.flow_yaml = os.path.join(flow_dir, 'flow.yml')

    @property
    def input_modality(self) -> Modalities:
        return Modalities.TEXT

    @property
    def output_modality(self) -> Modalities:
        return Modalities.TEXT_AND_IMAGE

    @staticmethod
    def _create_task_config(user_input: UserInput, data_example: Document) -> Task:
        """
        Read task configuration template and replace field names.
        """
        # read task config template
        template_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'task_config.json'
        )
        with open(template_path) as f:
            config_dict = json.load(f)
            config = Task(**config_dict)
        # get text and image field names if they're not specified
        if not user_input.es_text_fields:
            user_input.es_text_fields = [
                chunk.tags['field_name']
                for chunk in data_example.chunks
                if chunk.modality == 'text'
            ]
        if not user_input.es_image_fields:
            user_input.es_image_fields = [
                chunk.tags['field_name']
                for chunk in data_example.chunks
                if chunk.modality == 'image'
            ]
        # put field names into generation function configurations
        for encoder in config.encoders:
            if encoder.name == 'text_encoder':
                for method in encoder.training_data_generation_methods:
                    method.query.scope = user_input.es_text_fields
                    method.target.scope = user_input.es_text_fields
            elif encoder.name == 'vision_encoder':
                for method in encoder.training_data_generation_methods:
                    method.query.scope = user_input.es_text_fields
                    method.target.scope = user_input.es_image_fields
        # specify text and image field for the indexer
        config.indexer_scope['text'] = user_input.es_text_fields[0]
        config.indexer_scope['image'] = user_input.es_image_fields[0]

        user_input.task_config = config
        return user_input.task_config

    def preprocess(
        self,
        da: DocumentArray,
        user_input: UserInput,
        is_indexing: Optional[bool] = False,
    ) -> DocumentArray:
        # Indexing
        if is_indexing:
            return preprocess_nested_docs(da=da, user_input=user_input)
        # Query
        else:
            return preprocess_text(da=da, split_by_sentences=False)

    @hubble.login_required
    def setup(
        self, dataset: DocumentArray, user_input: UserInput, kubectl_path
    ) -> Dict:
        task_config = self._create_task_config(user_input, dataset[0])
        data = DataBuilder(dataset=dataset, config=task_config).build()
        env_dict = {'N_DIM': []}
        for encoder_data, encoder_type in data:
            finetune_settings = self._construct_finetune_settings(
                user_input=user_input,
                dataset=dataset,
                encoder_type=encoder_type,
            )
            artifact_id, token = finetune(
                finetune_settings=finetune_settings,
                app_instance=self,
                dataset=encoder_data,
                user_input=user_input,
                env_dict={},
                kubectl_path=kubectl_path,
            )

            env_dict['JINA_TOKEN'] = token
            if finetune_settings.model_name == ModelNames.CLIP:
                env_dict['CLIP_ARTIFACT'] = artifact_id
                env_dict['N_DIM'].append(512)
            elif finetune_settings.model_name == ModelNames.SBERT:
                env_dict['SBERT_ARTIFACT'] = artifact_id
                env_dict['N_DIM'].append(768)
            else:
                print(f'{self.app_name} only expects CLIP or SBERT models.')
                raise

        env_dict[
            'PREPROCESSOR_NAME'
        ] = f'jinahub+docker://NOWPreprocessor/{NOW_PREPROCESSOR_VERSION}'
        env_dict['APP'] = self.app_name
        indexer_config = get_indexer_config(
            len(dataset),
            elastic=True,
            kubectl_path=kubectl_path,
            deployment_type=user_input.deployment_type,
        )
        env_dict['HOSTS'] = indexer_config['hosts']
        env_dict['INDEXER_NAME'] = f"jinahub+docker://{indexer_config['indexer_uses']}"
        env_dict['INDEXER_MEM'] = indexer_config['indexer_resources']['INDEXER_MEM']
        env_dict['JINA_VERSION'] = jina_version
        # retention days
        if 'NOW_CI_RUN' in os.environ:
            env_dict[
                'RETENTION_DAYS'
            ] = 0  # JCloud will delete after 24hrs of being idle if not deleted in CI
        else:
            env_dict['RETENTION_DAYS'] = 7  # for user deployment set it to 30 days
        env_dict['ADMIN_EMAILS'] = (
            user_input.admin_emails or [] if user_input.secured else [],
        )
        env_dict['USER_EMAILS'] = (
            user_input.user_emails or [] if user_input.secured else [],
        )

        self.set_flow_yaml()

        return env_dict

    def _construct_finetune_settings(
        self,
        user_input: UserInput,
        dataset: DocumentArray,
        encoder_type: str,
    ) -> FinetuneSettings:
        finetune_settings = parse_finetune_settings(
            user_input=user_input,
            dataset=dataset,
            model_name=self._model_name(encoder_type),
            loss=self._loss_function(encoder_type),
            add_embeddings=False,
        )
        # temporary adjustments to work with small text+image dataset
        finetune_settings.epochs = 2
        finetune_settings.num_val_queries = 5
        finetune_settings.train_val_split_ration = 0.8
        return finetune_settings

    @staticmethod
    def _model_name(encoder_type: Optional[str] = None) -> str:
        """Name of the model used in case of fine-tuning."""
        if encoder_type == 'text-to-text':
            return ModelNames.SBERT
        elif encoder_type == 'text-to-image':
            return ModelNames.CLIP

    @staticmethod
    def _loss_function(encoder_type: Optional[str] = None) -> str:
        """Loss function used during fine-tuning."""
        if encoder_type == 'text-to-image':
            return 'CLIPLoss'
        return 'TripletMarginLoss'
