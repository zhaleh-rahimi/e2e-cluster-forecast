# cluster-forecast
A clustering-based forecasting framework for several heterogeneous disaggregated time-series
# Implementation of "Clustering-based demand forecasting with an application to immunoglobulin products"

This repository contains the implementation of the paper ["Clustering-based demand forecasting with an application to immunoglobulin products"]([https://www.sciencedirect.com/science/article/pii/S3050784725000030](https://www.sciencedirect.com/science/article/pii/S3050784725000030)). The paper presents an iterative clustering-based demand forecasting framework designed to improve demand predictions where several heterogeneous disaggregated time-series exist especially in healthcare settings.

## Overview

The proposed framework clusters patients based on domain-specific and time-series related features and iteratively refines these clusters to enhance forecasting accuracy. This approach addresses the challenges of heterogeneous patient populations and varying demand patterns in healthcare services. While previous studies consider these two steps (clustering and forecasting) separated, the proposed framework optimize the clustering phase based on final forecasting performance.

## Features

- **Iterative Clustering:** Refines patient clusters through forecasting perofmance (an iterative improvement approach).
- **Demand Forecasting:** Utilizes clustered data to predict patient demand more accurately (each cluster provides more predictable patterns than aggregated data from a heterogeneous population).

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/zhaleh-rahimi/cluster-forecast.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd cluster-forecast
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare your dataset:** Ensure your patient data is formatted according to the specifications outlined in the `data/README.md` file.

2. **Run the main script:** Execute the following command to start the clustering and forecasting process:

   ```bash
   python main.py --data_path path/to/your/data.csv
   ```

3. **Review the results:** The output, including refined clusters and demand forecasts, will be saved in the `results/` directory.

## Configuration

The `config.yaml` file contains various parameters that can be adjusted to customize the clustering and forecasting process. Key parameters include:

- `num_clusters`: Number of initial clusters.
- `max_iterations`: Maximum number of clustering iterations.
- `convergence_threshold`: Threshold for determining convergence between iterations.

Modify these parameters as needed to suit your dataset and requirements.

## Evaluation

To assess the performance of the forecasting model, run the evaluation script:

```bash
python evaluate.py --predictions_path path/to/predictions.csv --ground_truth_path path/to/ground_truth.csv
```

This will generate performance metrics and visualizations, which will be stored in the `evaluation/` directory.

## Contributing

We welcome contributions to enhance this implementation. Please follow these steps:

1. **Fork the repository.**
2. **Create a new branch:** `git checkout -b feature/your-feature-name`
3. **Commit your changes:** `git commit -m 'Add some feature'`
4. **Push to the branch:** `git push origin feature/your-feature-name`
5. **Open a pull request.**

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Citation

Please cite the original paper:

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

For any questions or collaborations, feel free to reach out to (rhmi.zhle[at]gmail.com)!


