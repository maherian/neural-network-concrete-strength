# Machine Learning for Compressive Strength Prediction of Nano-Silica Modified Concrete

This repository contains a reproducible machine learning workflow for predicting the compressive strength of nano-silica modified concrete mixtures from mixture proportions and curing age.

The project is based on the published study:

> Maherian et al. (2023), "Machine learning-based compressive strength estimation in nano silica-modified concrete", Construction and Building Materials, 408, 133684. DOI: [10.1016/j.conbuildmat.2023.133684](https://doi.org/10.1016/j.conbuildmat.2023.133684)

## Repository Structure

```text
.
+-- data/
|   +-- README.md
+-- notebooks/
|   +-- 01_concrete_strength_modeling.ipynb
+-- results/
|   +-- figures/
+-- src/
|   +-- data.py
|   +-- evaluation.py
|   +-- models.py
|   +-- preprocessing.py
|   +-- visualization.py
+-- .gitignore
+-- README.md
+-- requirements.txt
```

## Dataset

The notebook expects the dataset at:

```text
data/Nanodata.csv
```

The dataset was compiled from 39 published articles and contains 1,143 concrete mixture records, with compressive strength values ranging from 4 MPa to 129 MPa. Input variables include `cement`, `water`, `fly_ash`, `slag`, `micro_silica`, `nano_silica`, `water_cement_ratio`, `fine_aggregate`, `coarse_aggregate`, `superplasticizer`, `age`, and `specific_surface_area`. The prediction target is `compressive_strength`.

The dataset is not included in this repository. It can be made available upon reasonable request.

A column description and five-row data preview are available in `data/README.md`.

## Getting Started

Create an environment and install the dependencies:

```bash
pip install -r requirements.txt
```

Then open and run:

```text
notebooks/01_concrete_strength_modeling.ipynb
```

## Results

The current ANN workflow uses a fixed 60/20/20 train/validation/test split with `random_state=42`.

| Split | MAE | RMSE | R2 | MAPE (%) |
| --- | ---: | ---: | ---: | ---: |
| Train | 3.138 | 4.154 | 0.956 | 7.940 |
| Validation | 4.738 | 6.773 | 0.894 | 10.464 |
| Test | 5.117 | 6.769 | 0.901 | 12.001 |

Generated metrics are available in `results/model_metrics.csv`, and generated figures are saved in `results/figures/`.

## Citation

If you use this repository or the dataset behind this work, please cite:

```bibtex
@article{maherian2023machine,
  title = {Machine learning-based compressive strength estimation in nano silica-modified concrete},
  author = {Maherian, Mahsa Farshbaf and Baran, Servan and Bicakci, Sidar Nihat and Toreyin, Behcet Ugur and Atahan, Hakan Nuri},
  journal = {Construction and Building Materials},
  volume = {408},
  year = {2023},
  doi = {10.1016/j.conbuildmat.2023.133684}
}
```
