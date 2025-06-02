# clustering/cluster_model.py
import pandas as pd
from sklearn.cluster import KMeans

class ClusterModel:
    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters
        self.model = KMeans(n_clusters=self.n_clusters, random_state=42)

    def fit(self, data, features):
        self.model.fit(data[features])
        data['cluster'] = self.model.predict(data[features])
        return data

    def predict(self, data, features):
        data['cluster'] = self.model.predict(data[features])
        return data