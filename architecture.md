# OvaTwin Architecture

## 1. Project Overview

OvaTwin is a hybrid AI + physiological simulation framework for PCOS analysis.

The project combines two major computational branches:

1. An AI/ML branch for PCOS prediction and explainability
2. A physiological simulation branch for HPO-axis / menstrual-cycle modeling

These branches are connected through a patient personalization and digital-twin layer.

The long-term goal is to create a patient-specific computational digital twin that can:

- represent a patient's observed clinical state
- incorporate PCOS risk information
- represent relevant physiological states
- simulate a patient-specific baseline
- simulate controlled what-if scenarios
- compare baseline and scenarios
- communicate results through visualizations and reports

> Current limitation: the project currently has a functioning digital-twin software framework and a functioning Röblitz physiological simulation, but patient observations have not yet been converted into a validated patient-specific set of Röblitz kinetic parameters/states. Therefore, the current system should not yet be described as a fully calibrated patient-specific physiological twin.

---

# 2. Conceptual Architecture

```text
                                  OVATWIN
                                     |
              +----------------------+----------------------+
              |                                             |
              v                                             v
        AI / ML BRANCH                            PHYSIOLOGICAL BRANCH
              |                                             |
      Questionnaire Dataset                         Röblitz 2013 Model
              |                                             |
      Data Preprocessing                            SBML / OMEX
              |                                             |
      Feature Selection                             Tellurium
              |                                             |
      XGBoost / Random Forest                             |
              |                                             |
       PCOS Prediction                                     |
              |                                             |
      SHAP Explainability                                  |
              |                                             |
              +----------------------+----------------------+
                                     |
                                     v
                           PERSONALIZATION LAYER
                                     |
                                     v
                           PATIENT DIGITAL TWIN
                                     |
                       +-------------+-------------+
                       |                           |
                       v                           v
                BASELINE SIMULATION          WHAT-IF SCENARIO
                       |                           |
                       +-------------+-------------+
                                     |
                                     v
                           COMPARISON LAYER
                                     |
                                     v
                         VISUALIZATION / REPORT