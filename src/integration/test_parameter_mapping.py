import pandas as pd

from src.Clinical.hpo_observation_builder import (
    build_hpo_patient_values,
)

from src.twin.parameter_mapping import (
    create_mapping,
)


DATA_PATH = "data/PCOS_data_without_infertility-Full_new.csv"


def main():

    df = pd.read_csv(DATA_PATH)

    patient = build_hpo_patient_values(
        df.iloc[0]
    )

    mapping = create_mapping(patient)

    print("\nPATIENT")
    print("=" * 60)
    print(patient)

    print("\nOBSERVATIONS")
    print("=" * 60)

    for key, value in mapping["observations"].items():
        print(f"{key}: {value}")

    print("\nFOLLICULAR OBSERVATIONS")
    print("=" * 60)

    for key, value in mapping[
        "follicular_observations"
    ].items():
        print(f"{key}: {value}")

    print("\nHPO PARAMETERS")
    print("=" * 60)

    print(mapping["parameters"])

    print("\nSTATUS")
    print("=" * 60)

    print(mapping["status"])


if __name__ == "__main__":
    main()
