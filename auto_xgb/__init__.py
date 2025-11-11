from .process import process_data
from .optimize import optimize_xgb, optimize_lightgbm
from typing import Dict, Any


def easy_benchmark(file_path: str, target_column: str) -> Dict[str, Any]:
    """Creates a benchmark accuracy/RMSE for a given dataset
    Returns benchmark results, model used, and hyperparameters used"""
    X, y = process_data(file_path, target_column)


    pass