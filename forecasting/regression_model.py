from sklearn.linear_model import LinearRegression
import numpy as np
from forecasting.base_model import BaseForecastModel

class RegressionModel(BaseForecastModel):
    def __init__(self):
        self.model = LinearRegression()

    def fit(self, data, features, target):
        self.model.fit(data[features], data[target])

    def predict(self, data, features):
        return self.model.predict(data[features])
