import pandas as pd

from .clinical_loader import load_clinical_data, validate_dataset


DATA_PATH = "data/PCOS_data_without_infertility-Full_new.csv"


def show_extreme_values(df):
    print("\n" + "=" * 70)
    print("EXTREME PHYSIOLOGICAL VALUES")
    print("=" * 70)

    columns_to_check = [
        "FSH(mIU/mL)",
        "LH(mIU/mL)",
        "AMH(ng/mL)",
        "PRL(ng/mL)",
        "PRG(ng/mL)",
        "TSH (mIU/L)",
    ]

    for column in columns_to_check:

        if column not in df.columns:
            continue

        print("\n" + "-" * 70)
        print(column)
        print("-" * 70)

        numeric = pd.to_numeric(df[column], errors="coerce")

        # Show top 10 largest values
        extreme_indices = numeric.nlargest(10).index

        display_columns = [
            "Patient File No.",
            "PCOS (Y/N)",
            column,
            "Age (yrs)",
            "Cycle(R/I)",
            "Cycle length(days)",
            "AMH(ng/mL)",
            "FSH(mIU/mL)",
            "LH(mIU/mL)",
        ]

        display_columns = [
            c for c in display_columns
            if c in df.columns
        ]

        print(
            df.loc[
                extreme_indices,
                display_columns
            ].to_string(index=False)
        )


def inspect_cycle_length(df):

    print("\n" + "=" * 70)
    print("CYCLE LENGTH INSPECTION")
    print("=" * 70)

    print("\nUnique values:")
    print(
        sorted(
            df["Cycle length(days)"]
            .dropna()
            .unique()
            .tolist()
        )
    )

    print("\nValue counts:")
    print(
        df["Cycle length(days)"]
        .value_counts()
        .sort_index()
        .to_string()
    )

    print("\nCycle regularity vs cycle length:")
    print(
        pd.crosstab(
            df["Cycle(R/I)"],
            df["Cycle length(days)"]
        )
    )


def inspect_zero_values(df):

    print("\n" + "=" * 70)
    print("ZERO-VALUE INSPECTION")
    print("=" * 70)

    columns = [
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

    for column in columns:

        if column not in df.columns:
            continue

        numeric = pd.to_numeric(df[column], errors="coerce")

        zero_count = (numeric == 0).sum()

        print(
            f"{column:<30} "
            f"zeros = {zero_count}"
        )


def inspect_missing_values(df):

    print("\n" + "=" * 70)
    print("MISSING VALUES")
    print("=" * 70)

    missing = df.isnull().sum()

    missing = missing[missing > 0]

    if len(missing) == 0:
        print("No missing values found.")
    else:
        print(missing.to_string())


def main():

    print("=" * 70)
    print("OVATWIN PHASE 2")
    print("CLINICAL DATA QUALITY CHECK")
    print("=" * 70)

    print("\nLoading dataset...")

    df = load_clinical_data(DATA_PATH)

    print(f"Dataset shape: {df.shape}")

    print("\nValidating dataset...")

    validate_dataset(df)

    print("Validation: PASSED")

    inspect_missing_values(df)

    show_extreme_values(df)

    inspect_cycle_length(df)

    inspect_zero_values(df)

    print("\n" + "=" * 70)
    print("QUALITY CHECK COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()