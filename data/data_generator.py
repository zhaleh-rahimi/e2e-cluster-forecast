import numpy as np
import pandas as pd

class DataGenerator:
    def __init__(self, n_samples=500, seed=42):
        self.n_samples = n_samples
        self.seed = seed

    def generate(self):
        np.random.seed(self.seed)
        data = pd.DataFrame({
            'age': np.random.randint(20, 80, size=self.n_samples),
            'gender': np.random.choice([0, 1], size=self.n_samples),
            'comorbidities': np.random.randint(0, 5, size=self.n_samples),
            'prior_visits': np.random.poisson(2, size=self.n_samples),
            'region': np.random.choice([0, 1, 2], size=self.n_samples),
            'season': np.random.choice([0, 1, 2, 3], size=self.n_samples),
        })

        data['demand'] = (
            0.1 * data['age'] +
            0.3 * data['comorbidities'] +
            0.2 * data['prior_visits'] +
            0.1 * data['season'] +
            np.random.normal(0, 1, size=self.n_samples)
        )
        return data
