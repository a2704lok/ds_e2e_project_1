# from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity.config_entity import DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig


class ConfigManager:
    def __init__(self, config_filepath, schema_filepath, train_params_filepath):
        self.config=read_yaml(config_filepath)
        self.schema=read_yaml(schema_filepath)
        self.train_params=read_yaml(train_params_filepath)
    
    def get_data_validation_config(self) -> DataValidationConfig:
        path_config = self.config.data_validation
        col_schema = self.schema.COLUMNS
        target_schema = self.schema.TARGET_COLUMN

        data_validation_config = DataValidationConfig(
            root_dir=path_config.root_dir,
            file_name=path_config.file_name,
            all_schema = {"col_schema":col_schema,
                          "target_schema":target_schema}
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        transform_config = self.config.data_transformation
        data_transformation_config=DataTransformationConfig(
            root_dir = transform_config.root_dir,
            file_name = transform_config.file_name,
            output_path = transform_config.output_path,
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        train_params = self.train_params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = train_params.alpha,
            l1_ratio = train_params.l1_ratio,
            target_column = schema.name
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config=self.config.model_evaluation
        train_params=self.train_params.ElasticNet
        schema=self.schema.TARGET_COLUMN

        model_evaluation_config=ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path = config.model_path,
            all_params=train_params,
            metric_file_name = config.metric_file_name,
            target_column = schema.name,
            # mlflow_uri="https://dagshub.com/krishnaik06/datascienceproject.mlflow"
        )
        return model_evaluation_config