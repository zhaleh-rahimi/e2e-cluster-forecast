import numpy as np
from forecasting.base_model import BaseForecastModel
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator

class LSTMModel(BaseForecastModel):
    def __init__(self, look_back=10, epochs=10, batch_size=16):
        self.look_back = look_back
        self.epochs = epochs
        self.batch_size = batch_size
        self.model = None

    def fit(self, data, features, target):
        series = data[target].values
        series = series.reshape(-1, 1)

        generator = TimeseriesGenerator(series, series, length=self.look_back, batch_size=self.batch_size)
        self.model = Sequential()
        self.model.add(Input(shape=(self.look_back, 1)))
        self.model.add(LSTM(50, activation='relu'))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam', loss='mse')
        self.model.fit(generator, epochs=self.epochs, verbose=0)

    def predict(self, data, features):
        series = data[features[0]].values if features else data.values
        series = series.reshape(-1, 1)
        preds = []
        input_seq = series[:self.look_back].reshape(1, self.look_back, 1)

        for i in range(len(series) - self.look_back):
            pred = self.model.predict(input_seq, verbose=0)[0][0]
            preds.append(pred)
            input_seq = np.append(input_seq[:,1:,:], [[[pred]]], axis=1)
        preds = [series[i][0] for i in range(self.look_back)] + preds
        return np.array(preds)
