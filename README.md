# OvaTwin

OvaTwin is a machine learning project for predicting Polycystic Ovary Syndrome (PCOS) from clinical and lifestyle data. The pipeline includes data loading, preprocessing, feature selection, model comparison, performance evaluation, and SHAP-based explainability.

## Overview

This project is designed to support early detection of PCOS using a tabular medical dataset. It uses a structured ML workflow to:

- load and inspect the dataset
- separate features from the target label
- split data into train/test sets
- balance the training data with SMOTE
- apply feature selection using SelectKBest
- compare multiple classifiers
- evaluate the best-performing model
- save the trained model and metrics
- generate SHAP explainability plots

## Features

- PCOS classification pipeline using tabular health data
- XGBoost as the primary model
- Random Forest as a comparison baseline
- SMOTE for handling class imbalance
- Mutual information feature selection
- Model performance metrics: accuracy, precision, recall, F1-score, ROC-AUC
- SHAP summary plot for model interpretability
- Saved outputs in JSON and image formats

## Project Structure

```text
OvaTwin/
├── main.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── data/
│   └── dataset.csv
├── models/
│   └── xgboost_pcos_model.pkl
├── results/
│   ├── metrics.json
│   ├── model_comparison.json
│   └── shap_summary.png
└── src/
    ├── __init__.py
    ├── config.py
    ├── data_loader.py
    ├── evaluate.py
    ├── explain.py
    ├── feature_selection.py
    ├── model_comparison.py
    ├── personalization.py
    ├── predict.py
    ├── preprocessing.py
    └── train.py
```

## Tech Stack

- Python 3.10+
- pandas
- NumPy
- scikit-learn
- imbalanced-learn
- XGBoost
- SHAP
- Matplotlib
- seaborn
- joblib

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd OvaTwin
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

Or using Poetry/pyproject if preferred:

```bash
pip install .
```

## Usage

Run the main training and evaluation pipeline:

```bash
python main.py
```

This script will:

1. load the dataset from `data/dataset.csv`
2. split features and target
3. preprocess and balance the training data
4. select the best features
5. train XGBoost and Random Forest models
6. compare accuracy and classification metrics
7. generate a SHAP summary plot
8. save model artifacts to `models/` and `results/`

## Output Files

After running the project, the following outputs are generated:

- `models/xgboost_pcos_model.pkl` — trained XGBoost model with selected feature metadata
- `results/metrics.json` — evaluation metrics for the final model
- `results/model_comparison.json` — comparison between XGBoost and Random Forest
- `results/shap_summary.png` — SHAP feature importance summary

## Model Workflow

The pipeline follows this flow:

```text
Dataset -> Train/Test Split -> SMOTE -> Feature Selection -> Model Training -> Evaluation -> Explainability -> Save Artifacts
```

## Notes

- The target column is defined as `PCOS` in the data source.
- SMOTE is applied only to the training split to prevent data leakage.
- Feature selection uses mutual information to keep the most relevant attributes.
- XGBoost is the primary model because it offers strong performance on structured tabular data.

## License

This project is currently unlicensed unless you add a license file or specify one in your organization.

## Acknowledgements

This project is intended for research and educational use in medical prediction workflows. It should be reviewed by healthcare professionals before being used in real clinical decision-making.

