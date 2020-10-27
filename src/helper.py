"""Helper functions"""
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    accuracy_score,
    confusion_matrix,
)
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# helper function for outputing classification results
def praf1(y_true, y_pred, name):
    """Return precision, recall, accuracy, and f1_score for a classifier
    Can either output as a dictionary or print to stdout"""
    p = precision_score(y_true, y_pred)
    r = recall_score(y_true, y_pred)
    a = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    results = dict(precision=p, recall=r, accuracy=a, f1=f1)
    return pd.DataFrame(results, index=[name])


# helper function for confusion matrices
def confmat(y_true, y_pred, title):
    """Produce a confusion matrix
    Each argument should be a list of either 1 or 2 elements"""
    fig, ax = plt.subplots(ncols=len(title), figsize=(16, 6))
    ax = ax if isinstance(ax, np.ndarray) else [ax]

    for a, b, c, d in zip(y_true, y_pred, title, ax):
        sns.heatmap(confusion_matrix(a, b), center=True, annot=True, fmt=",", ax=d)
        d.set_title(c)
        d.set_xlabel("Predicted")
        d.set_ylabel("True")