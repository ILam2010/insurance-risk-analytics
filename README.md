# insurance-risk-analytics
## Data Version Control (DVC)

This project uses DVC to manage large insurance datasets and ensure reproducibility.

### Initialize DVC

```bash
dvc init
Add Dataset
dvc add data/MachineLearningRating_v3.txt
Push Data to Local Remote Storage
dvc push
Pull Dataset
dvc pull

The actual dataset is not stored directly in GitHub due to GitHub file size limitations. Instead, DVC tracks the dataset version while storing the large file in local remote storage.


---

#  SECOND DATA VERSION
Task 2 asks for TWO versions:
- raw
- cleaned

So after cleaning:

Save cleaned dataset:

```python id="x5v2nc"
df.to_csv("data/cleaned_insurance_data.csv", index=False)

Then track it:

dvc add data/cleaned_insurance_data.csv

Commit:

git add .

git commit -m "Add cleaned dataset version"

Push:

dvc push