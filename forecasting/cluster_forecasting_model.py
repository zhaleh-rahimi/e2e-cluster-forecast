# forecasting/cluster_forecasting_model.py
from collections import defaultdict
import numpy as np

class ClusterForecastingModel:
    def __init__(self, cluster_model, base_model_cls, n_clusters=3):
        self.cluster_model = cluster_model
        self.base_model_cls = base_model_cls
        self.models_by_cluster = {}
        self.n_clusters = n_clusters

    def fit(self, train_data, features, target):
        # Assign clusters to training data
        clustered_data = self.cluster_model.fit(train_data.copy(), features)

        # Train one model per cluster
        for cluster in range(self.n_clusters):
            cluster_data = clustered_data[clustered_data['cluster'] == cluster]
            model = self.base_model_cls()
            model.fit(cluster_data, features, target)
            self.models_by_cluster[cluster] = model

    def predict(self, test_data, features):
        # Assign clusters to test data
        clustered_data = self.cluster_model.predict(test_data.copy(), features)

        # Predict per cluster
        predictions = np.full(len(test_data), np.nan)
        for cluster, model in self.models_by_cluster.items():
            cluster_idx = clustered_data[clustered_data['cluster'] == cluster].index
            if len(cluster_idx) > 0:
                preds = model.predict(clustered_data.loc[cluster_idx], features)
                predictions[cluster_idx] = preds
        return predictions
