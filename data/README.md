# Dataset

The dataset used in this project was compiled from 39 published articles and contains 1,143 concrete mixture records for nano-silica modified concrete.

The dataset includes mixture proportions, curing age, specimen information, and measured compressive strength values. The compressive strength range is 4 MPa to 129 MPa.

The associated article is available at: https://doi.org/10.1016/j.conbuildmat.2023.133684

The dataset is not included in this repository, but it can be made available upon reasonable request.

## Columns

| Column | Description |
| --- | --- |
| `cement` | Cement content in the concrete mixture. |
| `water` | Water content in the concrete mixture. |
| `fly_ash` | Fly ash content. |
| `slag` | Slag content. |
| `micro_silica` | Micro-silica content. |
| `nano_silica` | Nano-silica content. |
| `water_cement_ratio` | Water-to-cement ratio. |
| `fine_aggregate` | Fine aggregate content. |
| `coarse_aggregate` | Coarse aggregate content. |
| `superplasticizer` | Superplasticizer dosage. |
| `age` | Curing age in days. |
| `specific_surface_area` | Specific surface area (SSA) of the nano-silica, in m2/g. |
| `compressive_strength` | Measured compressive strength in MPa. |

## Data Preview

The table below shows the first five cleaned records after standardizing column names.

| cement | water | fly_ash | slag | micro_silica | nano_silica | water_cement_ratio | fine_aggregate | coarse_aggregate | superplasticizer | age | compressive_strength | specific_surface_area |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 400 | 170 | 0 | 0 | 0 | 0 | 0.43 | 879.5 | 976.8 | 5.3 | 7 | 60.35 | 170 |
| 400 | 162.5 | 0 | 0 | 0 | 5 | 0.41 | 876.7 | 973.6 | 9.4 | 7 | 73 | 170 |
| 400 | 155 | 0 | 0 | 0 | 10 | 0.39 | 873.8 | 970.5 | 13.4 | 7 | 75.58 | 170 |
| 400 | 170 | 0 | 0 | 0 | 0 | 0.43 | 879.5 | 976.8 | 5.3 | 28 | 69.66 | 170 |
| 400 | 162.5 | 0 | 0 | 0 | 5 | 0.41 | 876.7 | 973.6 | 9.4 | 28 | 82.26 | 170 |
