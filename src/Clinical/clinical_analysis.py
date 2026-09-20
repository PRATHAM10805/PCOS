import json
from pathlib import Path

import numpy as np
import pandas as pd


TARGET_COLUMN = "PCOS (Y/N)"


PHYSIOLOGICAL_COLUMNS = [
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
    "Cycle length(days)",
]


def calculate_statistics(series):

    series = pd.to_numeric(
        series,
        errors="coerce"
    ).dropna()

    if len(series) == 0:

        return {
            "count": 0,
            "mean": None,
            "median": None,
            "std": None,
            "min": None,
            "max": None,
        }

    return {
        "count": int(len(series)),
        "mean": float(series.mean()),
        "median": float(series.median()),
        "std": float(series.std()),
        "min": float(series.min()),
        "max": float(series.max()),
    }


def calculate_pcos_distribution(df):

    distribution = (
        df[TARGET_COLUMN]
        .value_counts(dropna=False)
        .to_dict()
    )

    return {
        str(key): int(value)
        for key, value in distribution.items()
    }


def calculate_physiological_statistics(df):

    results = {}

    for column in PHYSIOLOGICAL_COLUMNS:

        if column not in df.columns:
            continue

        results[column] = calculate_statistics(
            df[column]
        )

    return results


def calculate_pcos_group_statistics(df):

    results = {}

    for column in PHYSIOLOGICAL_COLUMNS:

        if column not in df.columns:
            continue

        results[column] = {}

        for group, group_df in df.groupby(
            TARGET_COLUMN
        ):

            results[column][str(group)] = (
                calculate_statistics(
                    group_df[column]
                )
            )

    return results


def calculate_derived_variables(df):

    results = {}

    # Total follicle count
    if (
        "Follicle No. (L)" in df.columns
        and
        "Follicle No. (R)" in df.columns
    ):

        total_follicles = (
            df["Follicle No. (L)"]
            +
            df["Follicle No. (R)"]
        )

        results["total_follicle_count"] = (
            calculate_statistics(
                total_follicles
            )
        )

    # Mean follicle size
    if (
        "Avg. F size (L) (mm)" in df.columns
        and
        "Avg. F size (R) (mm)" in df.columns
    ):

        mean_follicle_size = (
            df["Avg. F size (L) (mm)"]
            +
            df["Avg. F size (R) (mm)"]
        ) / 2

        results["mean_follicle_size_mm"] = (
            calculate_statistics(
                mean_follicle_size
            )
        )

    # Recalculate FSH/LH ratio.
    #
    # The original FSH/LH column can contain spreadsheet
    # artefacts such as #NAME?, so we calculate it ourselves.

    if (
        "FSH(mIU/mL)" in df.columns
        and
        "LH(mIU/mL)" in df.columns
    ):

        fsh = df["FSH(mIU/mL)"]
        lh = df["LH(mIU/mL)"]

        valid = (
            fsh.notna()
            &
            lh.notna()
            &
            (lh > 0)
        )

        ratio = pd.Series(
            np.nan,
            index=df.index
        )

        ratio.loc[valid] = (
            fsh.loc[valid]
            /
            lh.loc[valid]
        )

        results["computed_fsh_lh_ratio"] = (
            calculate_statistics(
                ratio
            )
        )

    return results


def analyze_dataset(df):

    analysis = {

        "dataset": {
            "rows": int(df.shape[0]),
            "columns": int(df.shape[1]),
        },

        "missing_values": {
            str(column): int(value)
            for column, value
            in df.isnull().sum().items()
        },

        "pcos_distribution":
            calculate_pcos_distribution(df),

        "physiological_statistics":
            calculate_physiological_statistics(df),

        "pcos_group_statistics":
            calculate_pcos_group_statistics(df),

        "derived_variables":
            calculate_derived_variables(df),
    }

    return analysis


def save_analysis(
    analysis,
    output_path="results/clinical_dataset_analysis.json"
):

    output_path = Path(output_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            analysis,
            file,
            indent=4
        )