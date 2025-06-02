from forecasting.base_model import BaseForecastModel
from prophet import Prophet
import pandas as pd

class ProphetModel(BaseForecastModel):
    def __init__(self):
        self.model = Prophet()

    def fit(self, data, features, target):
        # Prophet requires dataframe with 'ds' and 'y' columns
        df = pd.DataFrame({
            'ds': data.index if data.index.dtype == 'datetime64[ns]' else pd.date_range(start='2020-01-01', periods=len(data)),
            'y': data[target]
        })
        self.model.fit(df)

    def predict(self, data, features):
        df = pd.DataFrame({
            'ds': data.index if data.index.dtype == 'datetime64[ns]' else pd.date_range(start='2020-01-01', periods=len(data))
        })
        forecast = self.model.predict(df)
        return forecast['yhat'].values
