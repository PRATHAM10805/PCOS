import numpy as np
import pandas as pd

from .clinical_loader import load_clinical_data


DATA_PATH = "data/PCOS_data_without_infertility-Full_new.csv"


def preprocess_clinical_data(df):
    """
    Prepare the clinical dataset for downstream
    patient parameter extraction.

    Important:
    - Original measurements are preserved.
    - Extreme values are flagged, not deleted.
    - Corrupted FSH/LH column is replaced by a
      calculated ratio.
    - Encoded cycle variables are retained as
      categorical/clinical information but are NOT
      interpreted as literal menstrual-cycle days.
    """

    df = df.copy()

    # ---------------------------------------------------------
    # Convert physiological columns to numeric
    # ---------------------------------------------------------

    numeric_columns = [
        "Age (yrs)",
        "Weight (Kg)",
        "Height(Cm)",
        "BMI",
        "FSH(mIU/mL)",
        "LH(mIU/mL)",
        "AMH(ng/mL)",
        "PRL(ng/mL)",
        "PRG(ng/mL)",
        "TSH (mIU/L)",
        "Follicle No. (L)",
        "Follicle No. (R)",
        "Avg. F size (L) (mm)",
        "Avg. F size (R) (mm)",
        "Endometrium (mm)",
    ]

    for column in numeric_columns:

        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    # ---------------------------------------------------------
    # Calculate FSH/LH ourselves
    # ---------------------------------------------------------

    df["FSH_LH_ratio"] = np.where(
        df["LH(mIU/mL)"] > 0,
        df["FSH(mIU/mL)"] / df["LH(mIU/mL)"],
        np.nan
    )

    # ---------------------------------------------------------
    # Total follicle count
    # ---------------------------------------------------------

    df["total_follicle_count"] = (
        df["Follicle No. (L)"]
        + df["Follicle No. (R)"]
    )

    # ---------------------------------------------------------
    # Mean follicle size
    # ---------------------------------------------------------

    df["mean_follicle_size_mm"] = (
        df["Avg. F size (L) (mm)"]
        + df["Avg. F size (R) (mm)"]
    ) / 2

    # ---------------------------------------------------------
    # Extreme-value flags
    #
    # These do NOT modify the original measurements.
    # ---------------------------------------------------------

    thresholds = {
        "FSH(mIU/mL)": 50,
        "LH(mIU/mL)": 50,
        "AMH(ng/mL)": 30,
        "PRL(ng/mL)": 100,
        "PRG(ng/mL)": 20,
        "TSH (mIU/L)": 20,
    }

    for column, threshold in thresholds.items():

        if column in df.columns:

            flag_name = (
                "flag_extreme_"
                + column
                .replace("(", "")
                .replace(")", "")
                .replace("/", "_")
                .replace(" ", "_")
                .replace(".", "")
            )

            df[flag_name] = (
                df[column].abs() > threshold
            )

    # ---------------------------------------------------------
    # Overall extreme-value flag
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

    # ---------------------------------------------------------
    # Do NOT use these as literal cycle days.
    #
    # We retain them for clinical information,
    # but explicitly create a flag showing that
    # they require encoding interpretation.
    # ---------------------------------------------------------

    df["cycle_encoding_requires_review"] = True

    # ---------------------------------------------------------
    # Remove corrupted original FSH/LH column
    # from the modeling representation.
    #
    # We retain the original dataset separately.
    # ---------------------------------------------------------

    if "FSH/LH" in df.columns:

        df = df.drop(
            columns=["FSH/LH"]
        )

    return df


def print_preprocessing_summary(df):

    print("\n" + "=" * 70)
    print("CLINICAL PREPROCESSING SUMMARY")
    print("=" * 70)

    print(f"\nPatients: {len(df)}")
    print(f"Columns after preprocessing: {len(df.columns)}")

    print("\nCalculated variables:")
    print("- FSH_LH_ratio")
    print("- total_follicle_count")
    print("- mean_follicle_size_mm")

    print("\nExtreme-value patients:")

    flagged_count = df["has_extreme_value"].sum()

    print(f"{flagged_count} patients flagged")

    print("\nCycle variables:")
    print("- Cycle(R/I) retained")
    print("- Cycle length(days) retained")
    print("- Neither is interpreted as literal cycle duration")

    print("\nMissing values in important physiological variables:")

    important_columns = [
        "FSH(mIU/mL)",
        "LH(mIU/mL)",
        "AMH(ng/mL)",
        "PRL(ng/mL)",
        "PRG(ng/mL)",
        "TSH (mIU/L)",
        "Follicle No. (L)",
        "Follicle No. (R)",
        "Avg. F size (L) (mm)",
        "Avg. F size (R) (mm)",
        "Endometrium (mm)",
    ]

    for column in important_columns:

        if column in df.columns:

            missing = df[column].isna().sum()

            print(
                f"{column:<30}: {missing}"
            )


def save_preprocessed_data(df):

    output_path = "data/clinical_dataset_preprocessed.csv"

    df.to_csv(
        output_path,
        index=False
    )

    print("\nSaved:")
    print(output_path)


def main():

    print("=" * 70)
    print("OVATWIN PHASE 2")
    print("CLINICAL PREPROCESSING")
    print("=" * 70)

    df = load_clinical_data(DATA_PATH)

    print(f"\nOriginal shape: {df.shape}")

    df = preprocess_clinical_data(df)

    print_preprocessing_summary(df)

    save_preprocessed_data(df)


if __name__ == "__main__":
    main()