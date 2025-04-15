This repository contains the implementation of the framework proposed in  ["Clustering-based demand forecasting"]([https://www.sciencedirect.com/science/article/pii/S3050784725000030](https://www.sciencedirect.com/science/article/pii/S3050784725000030)). The paper presents an iterative clustering-based demand forecasting framework designed to improve demand predictions where several heterogeneous disaggregated time-series exist especially in healthcare settings.

## Overview

The proposed framework clusters patients based on domain-specific and time-series related features and iteratively refines these clusters to enhance forecasting accuracy. This approach addresses the challenges of heterogeneous patient populations and varying demand patterns in healthcare services. While previous studies consider these two steps (clustering and forecasting) separated, the proposed framework optimize the clustering phase based on final forecasting performance.


The proposed clustering-based forecasting framework considers the following components:
1. **Clustering phase**:
We will utilize domain expertise and available datasets to determine the patient-level features that are most relevant to Ig demand. Following this, the patients will be grouped into clusters by unsupervised learning.
2. **Forecasting phase**:
The demand data will be separated according to the cluster labels and aggregated based on the chosen time granularity. We will then predict the demand for each cluster and combine the demand forecasts.
3. **Iterative Refinement**:
Our final phase involves refining our forecasting results by iterating over an identified parameter set in the clustering or forecasting phase. We aim to meet either condition (5) or (6), depending on the chosen metric, and find the optimal clustering scheme for the best forecasting outcome.

## Citation


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

