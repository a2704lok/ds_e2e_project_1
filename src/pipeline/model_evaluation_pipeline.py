from src.config.configuration import ConfigManager
from src.components.model_evaluation import ModelEvaluation
from src import logger


class ModelEvaluationTrainingPipeline:
    def __init__(self, config_filepath, schema_filepath,train_params_filepath):
        self.config = ConfigManager(config_filepath, schema_filepath,train_params_filepath)

    def model_evaluation(self):
        model_evaluation_config = self.config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluation_logging()
