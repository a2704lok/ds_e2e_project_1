import os
from src import logger
from sklearn.model_selection import train_test_split
from src.entity.config_entity import DataTransformationConfig
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def train_test_splitting(self):
        data=pd.read_csv(self.config.root_dir+"/"+self.config.file_name)

        train, test = train_test_split(data)

        train.to_csv(self.config.output_path+"/"+"train.csv",index = False)
        test.to_csv(self.config.output_path+"/"+"test.csv",index = False)

        print(train.shape)
        print(test.shape)