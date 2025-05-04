from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataValidationConfig:
    root_dir: str
    file_name: str
    all_schema: dict

@dataclass
class DataTransformationConfig:
    root_dir: str
    file_name: str
    output_path: str

@dataclass
class ModelTrainerConfig:
    root_dir: str
    train_data_path: str
    test_data_path: str
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str

@dataclass
class ModelEvaluationConfig:
    root_dir: str
    test_data_path: str
    model_path: str
    all_params: dict
    metric_file_name: str
    target_column: str
    # mlflow_uri: str