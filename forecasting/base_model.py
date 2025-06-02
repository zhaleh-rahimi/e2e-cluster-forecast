from abc import ABC, abstractmethod

class BaseForecastModel(ABC):
    @abstractmethod
    def fit(self, data, features, target):
        pass

    @abstractmethod
    def predict(self, data, features):
        pass
