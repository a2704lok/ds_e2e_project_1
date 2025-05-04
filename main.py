from src import logger
from src.pipeline.data_validation_pipeline import DataValidationPipeline
from src.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

config_filepath = "config/config.yaml"
schema_filepath = "schema.yaml"
train_params_filepath = "train_params.yaml"


data_valid = DataValidationPipeline(config_filepath = config_filepath, schema_filepath = schema_filepath, train_params_filepath = train_params_filepath)
data_valid.data_validation()

data_transform = DataTransformationTrainingPipeline(config_filepath = config_filepath, schema_filepath = schema_filepath, train_params_filepath = train_params_filepath)
data_transform.data_transformation()

model_train = ModelTrainerTrainingPipeline(config_filepath = config_filepath, schema_filepath = schema_filepath, train_params_filepath = train_params_filepath)
model_train.model_training()

model_evaluate = ModelEvaluationTrainingPipeline(config_filepath = config_filepath, schema_filepath = schema_filepath, train_params_filepath = train_params_filepath)
model_evaluate.model_evaluation()
