import pandas as pd
import tensorflow as tf
import tensorflow_docs.modeling
from tensorflow.keras import optimizers
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Sequential

from .evaluation import evaluate_regression
from .preprocessing import normalize_features, split_dataset


def build_ann_model(input_shape, hidden_units=52, learning_rate=0.001):
    model = Sequential(
        [
            Input(shape=(input_shape,)),
            Dense(12),
            Dense(hidden_units, activation="relu"),
            Dense(1),
        ]
    )
    optimizer = optimizers.RMSprop(learning_rate)
    model.compile(
        loss="mse",
        optimizer=optimizer,
        metrics=["mae", "mse", "mape"],
    )
    return model


def make_training_callbacks(checkpoint_path=None, patience=200):
    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=patience,
            restore_best_weights=True,
        )
    ]
    if checkpoint_path is not None:
        callbacks.append(
            tf.keras.callbacks.ModelCheckpoint(
                filepath=str(checkpoint_path),
                monitor="val_loss",
                save_best_only=True,
                save_weights_only=True,
                verbose=0,
            )
        )
    callbacks.append(tensorflow_docs.modeling.EpochDots())
    return callbacks


def run_hidden_unit_experiment(
    data,
    hidden_unit_range=range(71, 81),
    repeats=15,
    max_epochs=3000,
    patience=100,
    batch_size=10,
    output_path=None,
    random_state=42,
):
    experiment_results = []

    for hidden_units in hidden_unit_range:
        for repeat in range(repeats):
            train_dataset, validation_dataset, test_dataset = split_dataset(
                data,
                random_state=random_state + repeat,
            )
            normalized_data = normalize_features(train_dataset, validation_dataset, test_dataset)

            model = build_ann_model(
                input_shape=normalized_data["normed_train_data"].shape[1],
                hidden_units=hidden_units,
            )
            callbacks = make_training_callbacks(
                checkpoint_path=None,
                patience=patience,
            )

            history = model.fit(
                normalized_data["normed_train_data"],
                normalized_data["train_labels"],
                batch_size=batch_size,
                epochs=max_epochs,
                verbose=0,
                shuffle=True,
                validation_data=(
                    normalized_data["normed_validation_data"],
                    normalized_data["validation_labels"],
                ),
                callbacks=callbacks,
            )

            train_predictions = model.predict(normalized_data["normed_train_data"]).flatten()
            validation_predictions = model.predict(normalized_data["normed_validation_data"]).flatten()
            test_predictions = model.predict(normalized_data["normed_test_data"]).flatten()

            train_metrics = evaluate_regression(normalized_data["train_labels"], train_predictions)
            validation_metrics = evaluate_regression(normalized_data["validation_labels"], validation_predictions)
            test_metrics = evaluate_regression(normalized_data["test_labels"], test_predictions)

            experiment_results.append(
                {
                    "hidden_units": hidden_units,
                    "repeat": repeat,
                    "train_rmse": train_metrics["RMSE"],
                    "validation_rmse": validation_metrics["RMSE"],
                    "test_rmse": test_metrics["RMSE"],
                    "test_r2": test_metrics["R2"],
                    "test_mae": test_metrics["MAE"],
                    "test_mape_percent": test_metrics["MAPE (%)"],
                    "epochs_trained": len(history.epoch),
                }
            )

    experiment_results = pd.DataFrame(experiment_results)
    if output_path is not None:
        experiment_results.to_csv(output_path, index=False)
    return experiment_results
