from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from .data import TARGET_COLUMN


def save_figure(fig, filename, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    return output_path


def plot_feature_distributions(data, columns=None, filename="feature_distributions.png", output_dir=None):
    if columns is None:
        columns = [column for column in data.columns if column != TARGET_COLUMN]

    n_cols = 4
    n_rows = int(np.ceil(len(columns) / n_cols))
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, 3.5 * n_rows))
    axes = np.asarray(axes).flatten()

    for ax, column in zip(axes, columns):
        sns.histplot(data[column], kde=True, ax=ax)
        ax.set_title(column)
        ax.set_xlabel("")
        ax.set_ylabel("Count")

    for ax in axes[len(columns):]:
        ax.axis("off")

    fig.tight_layout()
    if output_dir is not None:
        save_figure(fig, filename, output_dir)
    plt.show()
    return fig


def plot_correlation_heatmap(data, filename="correlation_heatmap.png", output_dir=None):
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(
        data.corr(numeric_only=True),
        vmin=-1,
        vmax=1,
        cmap="coolwarm",
        square=True,
        annot=True,
        fmt=".2f",
        linewidths=0.5,
        ax=ax,
    )
    ax.set_title("Feature Correlation Heatmap")
    fig.tight_layout()
    if output_dir is not None:
        save_figure(fig, filename, output_dir)
    plt.show()
    return fig


def plot_training_history(history, filename="training_history.png", output_dir=None):
    history_frame = pd.DataFrame(history.history)
    history_frame["epoch"] = history.epoch
    history_frame["rmse"] = np.sqrt(history_frame["mse"])
    history_frame["val_rmse"] = np.sqrt(history_frame["val_mse"])

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].plot(history_frame["epoch"], history_frame["mae"], label="Train")
    axes[0].plot(history_frame["epoch"], history_frame["val_mae"], label="Validation")
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("MAE [MPa]")
    axes[0].set_title("Training and Validation MAE")
    axes[0].legend()

    axes[1].plot(history_frame["epoch"], history_frame["rmse"], label="Train")
    axes[1].plot(history_frame["epoch"], history_frame["val_rmse"], label="Validation")
    axes[1].set_xlabel("Epoch")
    axes[1].set_ylabel("RMSE [MPa]")
    axes[1].set_title("Training and Validation RMSE")
    axes[1].legend()

    fig.tight_layout()
    if output_dir is not None:
        save_figure(fig, filename, output_dir)
    plt.show()
    return history_frame


def plot_actual_vs_predicted(y_true, y_pred, split_name="test", filename=None, output_dir=None):
    y_pred = np.asarray(y_pred).ravel()
    y_true = np.asarray(y_true).ravel()
    lower = min(y_true.min(), y_pred.min())
    upper = max(y_true.max(), y_pred.max())
    padding = 0.05 * (upper - lower)
    limits = [lower - padding, upper + padding]

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(y_true, y_pred, alpha=0.75, edgecolor="none")
    ax.plot(limits, limits, color="black", linestyle="--", linewidth=1)
    ax.set_xlim(limits)
    ax.set_ylim(limits)
    ax.set_xlabel("Measured compressive strength [MPa]")
    ax.set_ylabel("Predicted compressive strength [MPa]")
    ax.set_title(f"Actual vs Predicted ({split_name.title()})")
    ax.set_aspect("equal", adjustable="box")
    fig.tight_layout()

    if filename is None:
        filename = f"actual_vs_predicted_{split_name.lower()}.png"
    if output_dir is not None:
        save_figure(fig, filename, output_dir)
    plt.show()
    return fig


def plot_prediction_errors(y_true, y_pred, split_name="test", filename=None, output_dir=None):
    errors = np.asarray(y_pred).ravel() - np.asarray(y_true).ravel()

    fig, ax = plt.subplots(figsize=(7, 4))
    sns.histplot(errors, bins=25, kde=True, ax=ax)
    ax.axvline(0, color="black", linestyle="--", linewidth=1)
    ax.set_xlabel("Prediction error [MPa]")
    ax.set_ylabel("Count")
    ax.set_title(f"Prediction Error Distribution ({split_name.title()})")
    fig.tight_layout()

    if filename is None:
        filename = f"prediction_errors_{split_name.lower()}.png"
    if output_dir is not None:
        save_figure(fig, filename, output_dir)
    plt.show()
    return fig
