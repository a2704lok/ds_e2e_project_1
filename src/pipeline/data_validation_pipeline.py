from src.config.configuration import ConfigManager
from src.components.data_validation import DataValiadtion


class DataValidationPipeline:
    def __init__(self, config_filepath, schema_filepath, train_params_filepath):
        self.config = ConfigManager(config_filepath, schema_filepath, train_params_filepath)
    
    def data_validation(self):
        data_validation_config = self.config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        
        data_validation_config = self.config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation_bool = data_validation.validate_all_columns()
        return data_validation_bool