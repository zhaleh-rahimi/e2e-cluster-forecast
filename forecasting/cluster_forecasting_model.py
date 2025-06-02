import numpy as np
import pandas as pd
import copy

class ClusterForecastingModel:
    def __init__(self, cluster_model, base_model_cls, n_clusters=4):
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
            if len(cluster_data) == 0:
                continue
            model = copy.deepcopy(self.base_model_cls)
            model.fit(data = cluster_data, features=features, target=target)
            self.models_by_cluster[cluster] = model

    def predict(self, test_data, features):
        clustered_data = self.cluster_model.predict(test_data.copy(), features)

        # Create predictions series with the same index
        predictions = pd.Series(index=test_data.index, dtype=float)

        for cluster, model in self.models_by_cluster.items():
            cluster_idx = clustered_data[clustered_data['cluster'] == cluster].index
            if len(cluster_idx) == 0:
                continue
            subset = test_data.loc[cluster_idx]
            preds = model.predict(subset[features], features)
            predictions.loc[cluster_idx] = preds

        # Handle missing predictions if any
        if predictions.isnull().any():
            print("Warning: some predictions missing, filling with mean.")
            predictions.fillna(predictions.mean(), inplace=True)

        return predictions
