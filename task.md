
### `TASK.md`

```markdown
# OvaTwin Task Roadmap

## Legend

- `[x]` Completed
- `[~]` In Progress / Partially Implemented
- `[ ]` Pending
- `[!]` Requires Scientific Validation

---

# Phase 0 — Repository Foundation

- [x] Create modular `src/` architecture
- [x] Separate Clinical, ML, HPO, integration and twin layers
- [x] Add package `__init__.py` files
- [x] Remove obsolete/debug HPO scripts
- [x] Remove generated `__pycache__` directories
- [x] Configure `.gitignore`
- [x] Exclude raw datasets from Git tracking
- [x] Exclude trained model binaries from Git tracking
- [x] Exclude OMEX model package from Git tracking
- [x] Push current implementation to GitHub
- [ ] Finalize root README
- [ ] Add development setup documentation
- [ ] Add contribution guidelines if required
- [ ] Add project license if required
- [ ] Add issue templates if required
- [ ] Add pull-request template
- [ ] Add project versioning strategy

---

# Phase 1 — PCOS Machine Learning Pipeline

## Dataset

- [x] Load questionnaire dataset
- [x] Validate dataset dimensions
- [x] Validate target column
- [x] Analyze target distribution
- [x] Encode categorical variables
- [x] Encode binary variables
- [x] Encode ternary variables
- [x] Encode frequency-related variables
- [x] Perform train/test split
- [x] Apply SMOTE only to training data
- [x] Perform feature selection

## Models

- [x] Train XGBoost
- [x] Train Random Forest
- [x] Evaluate accuracy
- [x] Evaluate precision
- [x] Evaluate recall
- [x] Evaluate F1-score
- [x] Evaluate ROC-AUC
- [x] Track false positives
- [x] Track false negatives
- [x] Compare models
- [x] Generate SHAP summary

## ML Reproducibility

- [ ] Confirm all random seeds are controlled
- [ ] Record preprocessing configuration
- [ ] Record selected feature set
- [ ] Record model hyperparameters
- [ ] Record train/test split
- [ ] Record SMOTE configuration
- [ ] Store experiment metadata
- [ ] Add reproducible model-training command

## ML Validation

- [ ] Add stratified cross-validation
- [ ] Perform leakage audit
- [ ] Evaluate performance variance across folds
- [ ] Evaluate probability calibration
- [ ] Evaluate robustness to preprocessing variation
- [ ] Perform threshold analysis
- [ ] Assess uncertainty where appropriate
- [ ] Test on independent external data if available
- [ ] Document dataset limitations

---

# Phase 2 — 541-Patient Clinical Dataset

## Dataset Analysis

- [x] Load 541-patient clinical dataset
- [x] Validate 45-column structure
- [x] Validate 541 patient records
- [x] Validate PCOS distribution
- [x] Inspect data types
- [x] Inspect missing values
- [x] Inspect cycle variables
- [x] Investigate FSH/LH field
- [x] Identify corrupted `#NAME?` values
- [x] Identify extreme clinical values
- [x] Identify zero measurements
- [x] Identify suspicious records
- [x] Create quality flags

## Clinical Cleaning

- [x] Compute FSH/LH from FSH and LH
- [x] Avoid use of corrupted original FSH/LH values
- [ ] Finalize missing-value treatment
- [ ] Finalize outlier treatment
- [ ] Validate clinical units
- [ ] Validate encoded cycle variables
- [ ] Determine treatment of suspicious values
- [ ] Determine whether extreme values represent measurement errors or valid observations
- [ ] Create auditable preprocessing report
- [ ] Add data provenance
- [ ] Preserve raw dataset separately from processed data
- [ ] Add preprocessing versioning

---

# Phase 3 — HPO Observation Layer

- [x] Implement `HPOPatientValues`
- [x] Implement clinical-to-HPO observation builder
- [x] Compute FSH/LH ratio
- [x] Compute total follicle count
- [x] Compute mean follicle size
- [x] Store clinical observations
- [x] Validate required observations
- [x] Validate all 541 patients
- [x] Keep observations separate from model parameters

## Future

- [ ] Version observation schema
- [ ] Add unit validation
- [ ] Add physiological range validation
- [ ] Add provenance for each observation
- [ ] Add missingness metadata
- [ ] Add quality flags to observations
- [ ] Add observation confidence where appropriate
- [ ] Support longitudinal observations
- [ ] Support repeated observations over time
- [ ] Add observation timestamps if longitudinal data becomes available

---

# Phase 4 — Röblitz HPO Model Integration

- [x] Obtain Röblitz model package
- [x] Identify BioModels model
- [x] Extract SBML from OMEX
- [x] Integrate Tellurium
- [x] Build `RoblitzModelRunner`
- [x] Validate model loading
- [x] Inspect species
- [x] Inspect model parameters
- [x] Inspect model structure
- [x] Create fresh model instances
- [x] Implement baseline simulation
- [x] Run 0–120 day simulation
- [x] Confirm `(1201, 46)` output
- [x] Implement baseline wrapper
- [x] Add model runner test
- [x] Add baseline simulation test
- [x] Document day-91 numerical warning
- [x] Avoid checkpoint/restart continuation as the normal baseline path

## Future

- [ ] Build structured simulation-result object
- [ ] Store time vector
- [ ] Store state trajectories
- [ ] Store simulation metadata
- [ ] Store model version
- [ ] Store model hash
- [ ] Store solver configuration
- [ ] Store simulation configuration
- [ ] Add solver diagnostics
- [ ] Investigate day-91 numerical behavior
- [ ] Test solver configuration changes
- [ ] Validate against reference/published model behavior
- [ ] Add model regression tests
- [ ] Add numerical stability tests

---

# Phase 5 — Röblitz Parameter Mapping

> No unsupported mappings should be introduced.

- [ ] Extract complete list of SBML parameters
- [ ] Build parameter ID → human-readable name dictionary
- [ ] Document parameter definitions
- [ ] Document parameter units where available
- [ ] Document parameter roles
- [ ] Identify production parameters
- [ ] Identify clearance parameters
- [ ] Identify feedback parameters
- [ ] Identify receptor-related parameters
- [ ] Identify follicular parameters
- [ ] Identify luteal parameters
- [ ] Identify cycle-related parameters
- [ ] Record model source for each parameter
- [ ] Record evidence for every proposed clinical mapping

---

# Phase 6 — Patient-Specific Physiological Calibration

> This is the major research component required for a true patient-specific physiological twin.

## Observation-to-State Mapping

- [ ] Identify observations that directly correspond to model variables
- [ ] Identify observations that can constrain model states
- [ ] Identify observations that can constrain model parameters
- [ ] Separate direct measurements from latent states
- [ ] Identify unobservable model variables
- [ ] Define which variables remain fixed
- [ ] Define which variables are patient-specific

## Calibration Method

- [ ] Define calibration objective
- [ ] Define loss function
- [ ] Define parameter bounds
- [ ] Define initial conditions
- [ ] Define optimization variables
- [ ] Select calibration algorithm
- [ ] Select optimization constraints
- [ ] Define stopping criteria
- [ ] Define convergence criteria
- [ ] Define calibration failure handling

## Calibration Experiments

- [ ] Test on synthetic data
- [ ] Test on known/reference trajectories
- [ ] Test on one clinical patient
- [ ] Test on multiple patients
- [ ] Scale calibration to the 541-patient dataset
- [ ] Record patient-specific calibrated parameters
- [ ] Measure calibration quality

## Identifiability

- [ ] Perform parameter sensitivity analysis
- [ ] Perform parameter identifiability analysis
- [ ] Identify non-identifiable parameters
- [ ] Reduce calibration parameter space where justified
- [ ] Estimate parameter uncertainty
- [ ] Evaluate calibration stability

## Validation

- [ ] Compare calibrated simulation with observed FSH
- [ ] Compare calibrated simulation with observed LH
- [ ] Compare calibrated simulation with available hormone measurements
- [ ] Compare relevant follicular observations
- [ ] Compare endometrium where appropriate
- [ ] Evaluate residual errors
- [ ] Evaluate generalization to held-out observations
- [ ] Document calibration assumptions

---

# Phase 7 — Patient Digital Twin

## Completed Foundation

- [x] Implement patient mapping
- [x] Implement patient profile
- [x] Implement `PatientDigitalTwin`
- [x] Implement twin status
- [x] Implement baseline simulation
- [x] Implement scenario registration
- [x] Implement scenario execution
- [x] Implement baseline/scenario comparison
- [x] Use independent model instances for scenarios

## Future

- [ ] Build patient twin from a clinical record
- [ ] Store standardized patient observations
- [ ] Store calibrated physiological state
- [ ] Store calibrated model parameters
- [ ] Store parameter uncertainty
- [ ] Store clinical quality metadata
- [ ] Store model version
- [ ] Store simulation configuration
- [ ] Store calibration configuration
- [ ] Add twin serialization
- [ ] Add twin versioning
- [ ] Add twin state history
- [ ] Add reproducibility metadata
- [ ] Add patient-specific simulation timestamps

---

# Phase 8 — ML + Digital Twin Integration

- [ ] Create stable ML assessment representation
- [ ] Attach PCOS prediction to patient twin
- [ ] Attach PCOS probability
- [ ] Attach SHAP feature contributions
- [ ] Store model name/version
- [ ] Store ML experiment metadata
- [ ] Define how ML outputs are used in personalization
- [ ] Separate predictive features from physiological variables
- [ ] Prevent ML outputs from being interpreted as physiological causality
- [ ] Test ML-to-twin integration
- [ ] Build complete end-to-end pipeline
- [ ] Generate combined patient-level output

Target:

```text
Patient Clinical Data
        |
        +------------------+
        |                  |
        v                  v
   ML Prediction      HPO Observations
        |                  |
        v                  v
PCOS Risk + SHAP    Patient Clinical State
        |                  |
        +--------+---------+
                 |
                 v
        Physiological Calibration
                 |
                 v
         Patient Digital Twin