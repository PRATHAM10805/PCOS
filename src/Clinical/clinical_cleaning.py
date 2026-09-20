import pandas as pd
import numpy as np

from .clinical_loader import load_clinical_data


DATA_PATH = "data/PCOS_data_without_infertility-Full_new.csv"


EXTREME_THRESHOLDS = {
    "FSH(mIU/mL)": 50,
    "LH(mIU/mL)": 50,
    "AMH(ng/mL)": 30,
    "PRL(ng/mL)": 100,
    "PRG(ng/mL)": 20,
    "TSH (mIU/L)": 20,
}


def create_quality_flags(df):

    df = df.copy()

    # ---------------------------------------------------------
    # Convert known physiological columns to numeric
    # ---------------------------------------------------------

    for column in EXTREME_THRESHOLDS:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    # ---------------------------------------------------------
    # Create individual extreme-value flags
    # ---------------------------------------------------------

    for column, threshold in EXTREME_THRESHOLDS.items():

        if column not in df.columns:
            continue

        flag_name = (
            column
            .replace("(", "")
            .replace(")", "")
            .replace("/", "_")
            .replace(" ", "_")
            .replace(".", "")
        )

        flag_name = f"flag_extreme_{flag_name}"

        df[flag_name] = (
            df[column].abs() > threshold
        )

    # ---------------------------------------------------------
    # FSH/LH ratio
    # Do NOT use the original #NAME? column
    # ---------------------------------------------------------

    if "FSH(mIU/mL)" in df.columns and "LH(mIU/mL)" in df.columns:

        fsh = pd.to_numeric(
            df["FSH(mIU/mL)"],
            errors="coerce"
        )

        lh = pd.to_numeric(
            df["LH(mIU/mL)"],
            errors="coerce"
        )

        df["computed_FSH_LH_ratio"] = np.where(
            lh > 0,
            fsh / lh,
            np.nan
        )

    # ---------------------------------------------------------
    # Overall quality flag
    # ---------------------------------------------------------

    flag_columns = [
        column
        for column in df.columns
        if column.startswith("flag_extreme_")
    ]

    df["has_extreme_value"] = (
        df[flag_columns]
        .any(axis=1)
    )

    return df


def show_flagged_patients(df):

    flagged = df[df["has_extreme_value"]].copy()

    print("\n" + "=" * 70)
    print("FLAGGED PATIENTS")
    print("=" * 70)

    print(f"\nNumber of patients flagged: {len(flagged)}")

    if flagged.empty:
        print("No extreme values detected.")
        return

    columns = [
        "Patient File No.",
        "PCOS (Y/N)",
        "FSH(mIU/mL)",
        "LH(mIU/mL)",
        "AMH(ng/mL)",
        "PRL(ng/mL)",
        "PRG(ng/mL)",
        "TSH (mIU/L)",
        "computed_FSH_LH_ratio",
        "has_extreme_value",
    ]

    columns = [
        column
        for column in columns
        if column in flagged.columns
    ]

    print(
        flagged[columns]
        .to_string(index=False)
    )


def save_cleaned_dataset(df):

    output_path = "data/clinical_dataset_flagged.csv"

    df.to_csv(
        output_path,
        index=False
    )

    print("\n" + "=" * 70)
    print("FLAGGED DATASET SAVED")
    print("=" * 70)

    print(output_path)


def main():

    print("=" * 70)
    print("OVATWIN PHASE 2")
    print("CLINICAL DATA QUALITY / FLAGGING")
    print("=" * 70)

    print("\nLoading clinical dataset...")

    df = load_clinical_data(DATA_PATH)

    print(f"Original dataset shape: {df.shape}")

    print("\nCreating quality flags...")

    df = create_quality_flags(df)

    show_flagged_patients(df)

    save_cleaned_dataset(df)


if __name__ == "__main__":
    main()