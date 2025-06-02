# End-to end Clustering-based Demand Forecasting
This project implements demand forecasting by first clustering similar data segments, then applying a range of forecasting models. The system supports both synthetic and real-world datasets, and allows CLI and Jupyter-based workflows.


## Project Structure
e2e-cluster-forecast/
├── clustering/
│   └── cluster_model.py
├── data/
│   ├── data_generator.py
│   └── google_cluster_data.py
├── forecasting/
│   ├── base_model.py
│   ├── regression.py
│   ├── arima_model.py
│   ├── prophet_model.py
│   ├── lstm_model.py
│   ├── xgboost_model.py
│   └── ensemble_model.py
├── utils/
│   └── utils.py
├── exploration/
│   └── eda.ipynb
├── main.py
├── requirements.txt
└── README.md


---

## Supported Forecasting Models

- Naive models: Last value, average
- Classical: Linear Regression, AR, ARIMA, Exponential Smoothing
- Machine Learning: XGBoost
- Deep Learning: RNN, LSTM
- Modern: Prophet
- Ensemble methods: Stacking/Averaging multiple weak learners

---

## Datasets

### 1. Synthetic (default)
Generated on the fly using `data/data_generator.py`.

### 2. Google Cluster Data (real)
- Dataset: [Google 2019 Cluster Sample](https://www.kaggle.com/datasets/derrickmwiti/google-2019-cluster-sample)
- Save the CSV locally and run with `--source google --filepath path/to/google.csv`

---

## How to Run

### CLI (Command Line)
```bash
# Synthetic data
python main.py --source synthetic --n_samples 1000

# Google data
python main.py --source google --filepath data/google_cluster_sample.csv

```
---
## Reference

```
@article{RAHIMI2025200469,
author = {Zhaleh Rahimi and Na Li and Douglas G. Down and Donald M. Arnold},
title = {Clustering-based demand forecasting with an application to immunoglobulin products},
journal = {Operations Research, Data Analytics and Logistics},
volume = {45},
pages = {200469},
year = {2025},
issn = {3050-7847},
doi = {https://doi.org/10.1016/j.ordal.2025.200469},
url = {https://www.sciencedirect.com/science/article/pii/S3050784725000030},
publisher = {Elsevier}
}
```

For any questions, feel free to reach out to (rhmi.zhle[at]gmail.com)!

