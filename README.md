# Implementation of "Clustering-based demand forecasting with an application to immunoglobulin products"

This repository contains the implementation of the paper ["Clustering-based demand forecasting with an application to immunoglobulin products"]([https://www.sciencedirect.com/science/article/pii/S3050784725000030](https://www.sciencedirect.com/science/article/pii/S3050784725000030)). The paper presents an iterative clustering-based demand forecasting framework designed to improve demand predictions where several heterogeneous disaggregated time-series exist especially in healthcare settings.

## Overview

The proposed framework clusters patients based on domain-specific and time-series related features and iteratively refines these clusters to enhance forecasting accuracy. This approach addresses the challenges of heterogeneous patient populations and varying demand patterns in healthcare services. While previous studies consider these two steps (clustering and forecasting) separated, the proposed framework optimize the clustering phase based on final forecasting performance.

## Features

- **Iterative Clustering:** Refines patient clusters through forecasting perofmance (an iterative improvement approach).
- **Demand Forecasting:** Utilizes clustered data to predict patient demand more accurately (each cluster provides more predictable patterns than aggregated data from a heterogeneous population).


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

For any questions, feel free to reach out to (rhmi.zhle[at]gmail.com)!

