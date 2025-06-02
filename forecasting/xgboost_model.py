# forecasting/xgboost_model.py

import numpy as np
import pandas as pd
import xgboost as xgb

class XGBoostModel:
    def __init__(self, n_lags=3):
        self.n_lags = n_lags
        self.model = xgb.XGBRegressor()

    def create_lag_features(self, data, target):
        df = data.copy()
        for lag in range(1, self.n_lags + 1):
            df[f'lag_{lag}'] = df[target].shift(lag)
        df = df.dropna().reset_index(drop=True)  # <--- drop NaNs + reset index
        return df

    def fit(self, data, features, target):
        df = self.create_lag_features(data, target)
        lag_cols = [f'lag_{i}' for i in range(1, self.n_lags + 1)]
        
        X = df[lag_cols]
        y = df[target]

        # Sanity check to confirm no NaNs
        if X.isnull().any().any() or y.isnull().any():
            raise ValueError("NaNs remain in training data after lag creation!")

        self.model.fit(X, y)

    def predict(self, data, features):
        df = self.create_lag_features(data, features[0])
        lag_cols = [f'lag_{i}' for i in range(1, self.n_lags + 1)]
        X = df[lag_cols]

        preds = self.model.predict(X)

        # Prepend NaNs to match original length
        full_preds = np.concatenate([np.full(self.n_lags, np.nan), preds])
        return full_preds
