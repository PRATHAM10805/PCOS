import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

from .train import train_model
from .config import RANDOM_STATE, RESULTS_DIR


def evaluate_single_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_prob),
        "false_positives": int(fp),
        "false_negatives": int(fn)
    }


def compare_models(X_train, y_train, X_test, y_test):

    print("\n" + "=" * 60)
    print("             MODEL COMPARISON")
    print("=" * 60)

    # -------------------------
    # MODEL 1: XGBoost
    # -------------------------
    print("\nTraining XGBoost...")
    xgb_model = train_model(X_train, y_train)

    xgb_results = evaluate_single_model(
        xgb_model, X_test, y_test
    )

    # -------------------------
    # MODEL 2: Random Forest
    # -------------------------
    print("Training Random Forest...")

    rf_model = RandomForestClassifier(
        n_estimators=200,
        max_depth=8,
        min_samples_split=4,
        random_state=RANDOM_STATE,
        class_weight=None,
        n_jobs=-1
    )

    rf_model.fit(X_train, y_train)

    rf_results = evaluate_single_model(
        rf_model, X_test, y_test
    )

    # -------------------------
    # Comparison
    # -------------------------

    results = {
        "XGBoost": xgb_results,
        "Random Forest": rf_results
    }

    print("\n" + "-" * 75)
    print(
        f"{'Model':<18}"
        f"{'Accuracy':<12}"
        f"{'Precision':<12}"
        f"{'Recall':<12}"
        f"{'F1':<12}"
        f"{'ROC-AUC':<12}"
    )
    print("-" * 75)

    for model_name, metrics in results.items():

        print(
            f"{model_name:<18}"
            f"{metrics['accuracy']:<12.4f}"
            f"{metrics['precision']:<12.4f}"
            f"{metrics['recall']:<12.4f}"
            f"{metrics['f1_score']:<12.4f}"
            f"{metrics['roc_auc']:<12.4f}"
        )

    print("-" * 75)

    print("\nConfusion Matrix Details:")

    for model_name, metrics in results.items():

        print(f"\n{model_name}")
        print(f"False Positives : {metrics['false_positives']}")
        print(f"False Negatives : {metrics['false_negatives']}")

    # Save results
    RESULTS_DIR.mkdir(exist_ok=True)

    with open(RESULTS_DIR / "model_comparison.json", "w") as f:
        json.dump(results, f, indent=4)

    print("\nComparison saved to:")
    print(RESULTS_DIR / "model_comparison.json")

    return xgb_model, rf_model, results