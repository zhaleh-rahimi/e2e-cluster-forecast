from sklearn.metrics import mean_squared_error
import numpy as np

def calculate_rmse(true_vals, predictions):
    true_vals = np.array(true_vals)
    predictions = np.array(predictions)

    # Remove any pair where either value is NaN
    mask = ~np.isnan(true_vals) & ~np.isnan(predictions)
    true_vals_clean = true_vals[mask]
    predictions_clean = predictions[mask]

    return np.sqrt(mean_squared_error(true_vals_clean, predictions_clean))
