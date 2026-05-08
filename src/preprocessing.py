from sklearn.model_selection import train_test_split

from .data import TARGET_COLUMN


def split_dataset(data, test_size=0.4, validation_size=0.5, random_state=42):
    train_dataset, temp_dataset = train_test_split(
        data,
        test_size=test_size,
        random_state=random_state,
    )
    validation_dataset, test_dataset = train_test_split(
        temp_dataset,
        test_size=validation_size,
        random_state=random_state,
    )
    return train_dataset, validation_dataset, test_dataset


def normalize_features(train_dataset, validation_dataset, test_dataset, target_column=TARGET_COLUMN):
    train_features = train_dataset.copy()
    validation_features = validation_dataset.copy()
    test_features = test_dataset.copy()

    train_labels = train_features.pop(target_column)
    validation_labels = validation_features.pop(target_column)
    test_labels = test_features.pop(target_column)

    feature_means = train_features.mean()
    feature_stds = train_features.std().replace(0, 1)

    def _normalize(features):
        return (features - feature_means) / feature_stds

    return {
        "train_features": train_features,
        "validation_features": validation_features,
        "test_features": test_features,
        "train_labels": train_labels,
        "validation_labels": validation_labels,
        "test_labels": test_labels,
        "normed_train_data": _normalize(train_features),
        "normed_validation_data": _normalize(validation_features),
        "normed_test_data": _normalize(test_features),
        "feature_means": feature_means,
        "feature_stds": feature_stds,
    }
