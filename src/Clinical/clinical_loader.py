from pathlib import Path

import pandas as pd


TARGET_COLUMN = "PCOS (Y/N)"

EXPECTED_COLUMNS = [
    TARGET_COLUMN,
    "Age (yrs)",
    "Weight (Kg)",
    "Height(Cm)",
    "BMI",
    "Cycle(R/I)",
    "Cycle length(days)",
    "FSH(mIU/mL)",
    "LH(mIU/mL)",
    "FSH/LH",
    "TSH (mIU/L)",
    "AMH(ng/mL)",
    "PRL(ng/mL)",
    "PRG(ng/mL)",
    "Follicle No. (L)",
    "Follicle No. (R)",
    "Avg. F size (L) (mm)",
    "Avg. F size (R) (mm)",
    "Endometrium (mm)",
]


NUMERIC_COLUMNS = [
    "Age (yrs)",
    "Weight (Kg)",
    "Height(Cm)",
    "BMI",
    "Pulse rate(bpm)",
    "RR (breaths/min)",
    "Hb(g/dl)",
    "Cycle length(days)",
    "FSH(mIU/mL)",
    "LH(mIU/mL)",
    "AMH(ng/mL)",
    "PRL(ng/mL)",
    "PRG(ng/mL)",
    "TSH (mIU/L)",
    "Vit D3 (ng/mL)",
    "RBS(mg/dl)",
    "BP _Systolic (mmHg)",
    "BP _Diastolic (mmHg)",
    "Follicle No. (L)",
    "Follicle No. (R)",
    "Avg. F size (L) (mm)",
    "Avg. F size (R) (mm)",
    "Endometrium (mm)",
]


def clean_column_names(df):
    df = df.copy()

    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
    )

    return df


def load_clinical_data(path):
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(
            f"Clinical dataset not found: {path}"
        )

    df = pd.read_csv(path)

    df = clean_column_names(df)

    # Convert known numerical columns.
    for column in NUMERIC_COLUMNS:

        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    return df


def validate_dataset(df):

    missing_columns = [
        column
        for column in EXPECTED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:

        raise ValueError(
            "The following expected columns are missing:\n"
            + "\n".join(
                f"- {column}"
                for column in missing_columns
            )
        )

    return True