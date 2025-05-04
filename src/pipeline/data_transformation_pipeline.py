from src.config.configuration import ConfigManager
from src.components.data_transformation import DataTransformation
from src import logger

from pathlib import Path


class DataTransformationTrainingPipeline:
    def __init__(self, config_filepath, schema_filepath, train_params_filepath):
        self.config = ConfigManager(config_filepath, schema_filepath, train_params_filepath)

    def data_transformation(self):
        try:
            data_transformation_config=self.config.get_data_transformation_config()
            data_transformation=DataTransformation(config=data_transformation_config)
            data_transformation.train_test_splitting()

        except Exception as e:
            print(e)