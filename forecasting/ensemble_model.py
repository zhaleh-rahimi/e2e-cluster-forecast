# forecasting/ensemble_model.py
import numpy as np
from sklearn.linear_model import LinearRegression

class EnsembleModel:
    def __init__(self, base_models):
        self.base_models = base_models
        self.meta_model = LinearRegression()

    def fit(self, data, features, target):
        # Fit base models
        for model in self.base_models:
            model.fit(data, features, target)

        # Get base model predictions
        base_preds = []
        for model in self.base_models:
            pred = model.predict(data, features)
            base_preds.append(pred)

        base_preds = np.column_stack(base_preds)

        # Clean NaNs
        mask = ~np.isnan(base_preds).any(axis=1)
        meta_X = base_preds[mask]
        meta_y = data[target].values[mask]

        # Fit meta model
        self.meta_model.fit(meta_X, meta_y)

    def predict(self, data, features):
        base_preds = []
        for model in self.base_models:
            pred = model.predict(data, features)
            base_preds.append(pred)

        base_preds = np.column_stack(base_preds)

        # Replace NaNs with 0 or mean (zero here)
        base_preds = np.nan_to_num(base_preds, nan=0.0)

        return self.meta_model.predict(base_preds)
