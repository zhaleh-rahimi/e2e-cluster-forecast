from statsmodels.tsa.arima.model import ARIMA
from forecasting.base_model import BaseForecastModel


class ARIMAModel(BaseForecastModel):
    def __init__(self, order=(1,0,0)):
        self.order = order
        self.model_fit = None

    def fit(self, data, features, target):
        y = data[target]
        exog = data[features] if features else None
        model = ARIMA(y, exog=exog, order=self.order, trend= [1,0,0,0])
        self.model_fit = model.fit()

    def predict(self, data, features):
        exog = data[features] if features else None
        preds = self.model_fit.predict(start=0, end=len(data)-1, exog=exog)
        return preds
