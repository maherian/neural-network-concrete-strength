from pathlib import Path

import pandas as pd


TARGET_COLUMN = "compressive_strength"

EXPECTED_COLUMNS = [
    "cement",
    "water",
    "fly_ash",
    "slag",
    "micro_silica",
    "nano_silica",
    "water_cement_ratio",
    "fine_aggregate",
    "coarse_aggregate",
    "superplasticizer",
    "age",
    "strength",
    TARGET_COLUMN,
    "specific_surface_area",
]


def load_dataset(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {path}. "
            "Place the concrete dataset CSV at data/Nanodata.csv before running this notebook."
        )

    data = pd.read_csv(path)
    if data.shape[1] != len(EXPECTED_COLUMNS):
        raise ValueError(
            f"Expected {len(EXPECTED_COLUMNS)} columns, but found {data.shape[1]}. "
            "Check that data/Nanodata.csv matches the expected project dataset."
        )

    data.columns = EXPECTED_COLUMNS
    return data.drop(columns=["strength"], errors="ignore")
