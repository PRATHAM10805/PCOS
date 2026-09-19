import matplotlib.pyplot as plt
import shap

from .config import RESULTS_DIR


def explain_model(model, X_test):

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X_test)

    plt.figure()

    shap.summary_plot(
        shap_values,
        X_test,
        show=False
    )

    plt.tight_layout()

    RESULTS_DIR.mkdir(exist_ok=True)

    plt.savefig(
        RESULTS_DIR / "shap_summary.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return explainer, shap_values