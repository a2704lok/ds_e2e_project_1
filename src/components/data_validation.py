import os
from src import logger
import pandas as pd

from src.entity.config_entity import DataValidationConfig


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            data = pd.read_csv(self.config.root_dir+"/"+self.config.file_name)
            all_cols = list(data.columns)
            col_schema = self.config.all_schema.get('col_schema')

            for col in all_cols:
                if col not in col_schema:
                    validation_status = False
                else:
                    validation_status = True

            return validation_status
        except Exception as e:
            raise e

    

