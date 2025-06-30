# 🏦 Loan Approval Predictor (CLI Based using XGBoost)

A simple yet powerful command-line tool that predicts whether a loan application will be **approved or rejected**, based on applicant details. Built using Python, XGBoost, and Scikit-learn.

---

## 🔧 Features

- CLI interface to train or predict
- XGBoost classifier with high accuracy
- Handles categorical variables using LabelEncoder
- Supports **unseen labels** with fallback encoding
- Example prompts to guide user input
- Saves model and encoders for reuse

---

## 📥 Dataset

Uses [Loan Prediction Dataset](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset).  
Ensure your dataset is named `data.csv` and placed in the same folder as the script.

**Sample columns:**

| Column             | Description                    |
|--------------------|--------------------------------|
| Gender             | Male / Female                  |
| Married            | Yes / No                       |
| Dependents         | 0 / 1 / 2 / 3+                 |
| Education          | Graduate / Not Graduate        |
| Self_Employed      | Yes / No                       |
| ApplicantIncome    | Numeric                        |
| CoapplicantIncome  | Numeric                        |
| LoanAmount         | Numeric (thousands)            |
| Loan_Amount_Term   | Term in months (e.g. 360)      |
| Credit_History     | 1.0 = Good, 0.0 = Bad          |
| Property_Area      | Urban / Semiurban / Rural      |
| Loan_Status        | Target (Y = approved, N = not) |
