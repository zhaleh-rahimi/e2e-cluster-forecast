# main.py
import argparse
import pandas as pd
from utils.utils import calculate_rmse
from data.data_generator import generate_synthetic_data
from data.google_cluster_data import load_google_data

from clustering.cluster_model import ClusterModel
from forecasting.cluster_forecasting_model import ClusterForecastingModel
from forecasting.regression_model import RegressionModel
from forecasting.xgboost_model import XGBoostModel
from forecasting.lstm_model import LSTMModel
# (Import other forecasting models as needed)

models_available = {
    'regression': RegressionModel,
    'xgboost': XGBoostModel,
    'lstm': LSTMModel,
    'cluster_forecast': lambda: ClusterForecastingModel(
        cluster_model=ClusterModel(n_clusters=3),
        base_model_cls=RegressionModel,
        n_clusters=3
    )
}

def parse_args():
    parser = argparse.ArgumentParser(description="Run forecasting models with optional clustering")
    parser.add_argument('--model', type=str, choices=models_available.keys(), required=True, help='Model to use')
    parser.add_argument('--data', type=str, choices=['synthetic', 'google'], default='synthetic', help='Dataset to use')
    return parser.parse_args()

def load_data(source):
    if source == 'synthetic':
        return generate_synthetic_data()
    elif source == 'google':
        return load_google_data()
    else:
        raise ValueError("Invalid data source")

def main():
    args = parse_args()
    data = load_data(args.data)

    features = ['cpu']  # Adapt if multivariate
    target = 'cpu'

    # Train/test split
    split_idx = int(len(data) * 0.8)
    train_data = data.iloc[:split_idx].reset_index(drop=True)
    test_data = data.iloc[split_idx:].reset_index(drop=True)

    model = models_available[args.model]()
    model.fit(train_data, features, target)
    predictions = model.predict(test_data, features)

    rmse = calculate_rmse(test_data[target].values, predictions)
    print(f"RMSE ({args.model}):", rmse)

if __name__ == '__main__':
    main()