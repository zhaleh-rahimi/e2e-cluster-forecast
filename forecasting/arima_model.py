from statsmodels.tsa.arima.model import ARIMA
import numpy as np
from forecasting.base_model import BaseForecastModel
import pandas as pd

class ARIMAModel(BaseForecastModel):
    def __init__(self, order=(5,1,0)):
        self.order = order
        self.model = None
        self.fitted_model = None

    def fit(self, data, features, target):
        # Assume 'target' is a univariate time series in order
        # ARIMA works on a 1D series, so we only use target column
        ts = data[target].values
        self.model = ARIMA(ts, order=self.order)
        self.fitted_model = self.model.fit()

    def predict(self, data, features):
        n = len(data)
        preds = self.fitted_model.predict(start=0, end=n-1)
        return preds
