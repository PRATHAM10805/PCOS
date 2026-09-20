import pandas as pd


def predict_patient(model, patient_data):

    patient_df = pd.DataFrame([patient_data])

    prediction = model.predict(patient_df)[0]

    probability = model.predict_proba(
        patient_df
    )[0][1]

    result = {
        "prediction": (
            "PCOS" if prediction == 1
            else "Non-PCOS"
        ),
        "risk_probability": float(probability)
    }

    return result