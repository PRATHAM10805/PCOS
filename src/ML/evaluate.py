import json

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix
)

from .config import RESULTS_DIR


def evaluate_model(model, X_test, y_test):

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_prob)
    }

    print("\n" + "=" * 50)
    print("MODEL PERFORMANCE")
    print("=" * 50)

    for name, value in metrics.items():
        print(f"{name}: {value:.4f}")

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    RESULTS_DIR.mkdir(exist_ok=True)

    with open(RESULTS_DIR / "metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    return y_pred, y_prob, metrics