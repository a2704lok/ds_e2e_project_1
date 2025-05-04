from src.config.configuration import ConfigManager
from src.components.model_trainer import ModelTrainer
from src import logger

class ModelTrainerTrainingPipeline:
    def __init__(self, config_filepath, schema_filepath,train_params_filepath):
        self.config = ConfigManager(config_filepath, schema_filepath,train_params_filepath)

    def model_training(self):
        model_trainer_config = self.config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()