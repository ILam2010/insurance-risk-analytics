# Insurance Risk Analytics

## Project Overview

This project is an end-to-end insurance risk analytics pipeline focused on:
- Data version control (DVC)
- Exploratory Data Analysis (EDA)
- Hypothesis testing
- Predictive modeling for risk-based pricing

The goal is to build a reproducible and auditable machine learning workflow for insurance claim prediction and pricing optimization.

---

## Data Version Control (DVC)

This project uses Data Version Control (DVC) to ensure reproducibility and proper tracking of large datasets.

DVC allows us to version datasets without storing large files directly in GitHub.

---

##  Data Pipeline

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd insurance-risk-analytics
````

---

### 2. Create Virtual Environment 

```bash
python -m venv venv
venv\Scripts\activate   
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Initialize DVC (if not already initialized)

```bash
dvc init
```

---

### 5. Pull Data from DVC Storage

This restores the dataset from local remote storage:

```bash
dvc pull
```

---

## Dataset Versions

This project maintains two dataset versions:

### Raw Dataset

```text
data/MachineLearningRating_v3.txt
```

Tracked using:

```bash
dvc add data/MachineLearningRating_v3.txt
```

---

### Cleaned Dataset

After preprocessing and handling missing values:

```text
data/cleaned_insurance_data.csv
```

Tracked using:

```bash
dvc add data/cleaned_insurance_data.csv
```

---

## Push Data to DVC Storage

To store dataset versions in local remote storage:

```bash
dvc push
```

---

## Why DVC is Used

* Enables reproducibility of experiments
* Tracks multiple dataset versions (raw and cleaned)
* Prevents large files from being pushed to GitHub
* Supports audit-friendly workflows required in insurance analytics

---

## Project Structure

```
insurance-risk-analytics/
│
├── data/                         # DVC-tracked datasets
├── notebooks/                    # EDA, modeling, hypothesis testing
├── src/                          # Reusable Python modules
├── .dvc/                         # DVC configuration
├── .github/workflows/ci.yml     # CI pipeline
├── dvc.yaml                      # Pipeline definition
├── requirements.txt
└── README.md
```

---

## Notes

* The dataset is NOT stored in GitHub due to size limitations.
* All data is managed using DVC for reproducibility.
* This ensures compliance with real-world insurance data engineering practices.





