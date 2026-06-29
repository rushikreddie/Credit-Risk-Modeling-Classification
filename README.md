<div align="center">

<!-- Animated Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=CreditIQ&fontSize=80&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Credit%20Risk%20Modeling%20%7C%20Loan%20Default%20Prediction%20Engine&descAlignY=55&descSize=18" width="100%"/>

<br/>

<!-- Animated Typing -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=00D4FF&center=true&vCenter=true&width=700&lines=Predicting+Loan+Default+with+ML;WOE%2FIV+%2B+VIF+Feature+Selection;SMOTETomek+%2B+Optuna+Hyperparameter+Tuning;KS+Statistic+%7C+Gini+%7C+Decile+Analysis" alt="Typing SVG" />
</a>

<br/><br/>

<!-- Badges -->
[![Live App](https://img.shields.io/badge/Live%20App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://credit-risk-modeling-classification-creditiq.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Optuna](https://img.shields.io/badge/Optuna-Hyperparameter%20Tuning-6C3AE9?style=for-the-badge)](https://optuna.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=rushikreddie&color=blueviolet&style=for-the-badge&label=REPO+VIEWS)

</div>

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Value](#business-value)
- [Dataset](#dataset)
- [ML Pipeline](#ml-pipeline)
- [Feature Engineering](#feature-engineering)
- [Feature Selection](#feature-selection)
- [Model Training](#model-training)
- [Model Results](#model-results)
- [Model Evaluation](#model-evaluation)
- [Key Features](#key-features)
- [Live App — CreditIQ](#live-app--creditiq)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Tech Stack](#tech-stack)
- [Connect with Me](#connect-with-me)

---

<div align="center">
<h2>Project Overview</h2>
</div>

> **CreditIQ** is a production-grade, end-to-end **Loan Default Prediction System** built on real-world Indian banking and credit bureau data. It predicts whether a loan applicant will **default or not** — using a rigorous ML pipeline that includes feature engineering, VIF-based multicollinearity removal, WOE/IV-based feature selection, class imbalance handling, and Optuna hyperparameter tuning.

The final deployed model is a **Logistic Regression** tuned with Optuna and trained on SMOTETomek-balanced data — achieving an **AUC of 0.98**, **Gini of 0.96**, and a **KS Statistic of 85.98%**.

---

<div align="center">
<h2>Business Value</h2>
</div>

| | |
|:---:|:---|
| **Loan Default Prevention** | Identifies high-risk borrowers before disbursement, reducing NPAs |
| **Cost Reduction** | Automated risk assessment cuts manual underwriting time significantly |
| **Real-Time Decisions** | Instant classification via Streamlit app for credit officers and analysts |
| **Industry-Standard Evaluation** | KS Statistic, Gini Coefficient, and Decile Analysis mirror real banking model validation |
| **Explainability** | Logistic Regression coefficients reveal the exact weight of each feature |
| **Democratized Access** | Web-deployed app makes ML credit scoring available to any institution |

---

<div align="center">
<h2>Dataset</h2>
</div>

Three real-world datasets were merged to build the final feature set:

| Dataset | Key Information |
|:---|:---|
| **customers.csv** | Age, income, gender, marital status, employment, residence type, city, state |
| **loans.csv** | Loan amount, sanction amount, processing fee, GST, tenure, disbursal date, loan purpose/type |
| **bureau_data.csv** | Open/closed accounts, total loan months, delinquent months, total DPD, enquiry count, credit utilization ratio |

> **Target Variable:** Binary — `default` (1 = defaulted, 0 = did not default)

---

<div align="center">
<h2>ML Pipeline</h2>
</div>

```
customers.csv + loans.csv + bureau_data.csv
                    │
                    ▼
        ┌─────────────────────┐
        │   Data Merging      │  ← Merged on cust_id across all 3 datasets
        └─────────────────────┘
                    │
                    ▼
        ┌─────────────────────┐
        │  Train/Test Split   │  ← 75/25 stratified split (random_state=42)
        └─────────────────────┘
                    │
                    ▼
        ┌─────────────────────┐
        │   Preprocessing     │  ← Impute residence_type (mode), fix typo
        │                     │    'Personaal' → 'Personal', remove outliers
        │                     │    (processing_fee/loan_amount >= 0.3)
        └─────────────────────┘
                    │
                    ▼
        ┌─────────────────────┐
        │  Feature Engineering│  ← Loan-to-Income, Delinquency Ratio,
        │                     │    Avg DPD per Delinquency
        └─────────────────────┘
                    │
                    ▼
        ┌─────────────────────┐
        │  Feature Selection  │  ← VIF (remove multicollinearity)
        │                     │    + WOE/IV (keep IV > 0.02)
        └─────────────────────┘
                    │
                    ▼
        ┌─────────────────────┐
        │  Scaling + Encoding │  ← MinMaxScaler + pd.get_dummies
        └─────────────────────┘
                    │
                    ▼
        ┌─────────────────────┐
        │  Class Imbalance    │  ← SMOTETomek (combined over+under sampling)
        │  Handling           │
        └─────────────────────┘
                    │
                    ▼
        ┌─────────────────────┐
        │  Model Training     │  ← 4 training attempts with different
        │  (4 Attempts)       │    strategies and models
        └─────────────────────┘
                    │
                    ▼
        ┌─────────────────────┐
        │  Model Evaluation   │  ← ROC-AUC, KS Statistic, Gini,
        │                     │    Decile Analysis, Classification Report
        └─────────────────────┘
                    │
                    ▼
        ┌─────────────────────┐
        │  Best Model Saved   │  ← Serialized with joblib
        │  (joblib)           │    artifacts/model_data.joblib
        └─────────────────────┘
                    │
                    ▼
        ┌─────────────────────┐
        │  Streamlit          │  ← CreditIQ — Interactive live web app
        │  Deployment         │
        └─────────────────────┘
```

---

<div align="center">
<h2>Feature Engineering</h2>
</div>

Three new features were created from existing columns to improve predictive power:

| Feature | Formula | Insight |
|:---|:---|:---|
| **loan_to_income** | `loan_amount / income` | Higher LTI = higher risk loan |
| **delinquency_ratio** | `(delinquent_months * 100) / total_loan_months` | % of loan months with missed payments |
| **avg_dpd_per_delinquency** | `total_dpd / delinquent_months` (0 if delinquent_months = 0) | Average severity of each missed payment |

> `np.where` was used for `avg_dpd_per_delinquency` to avoid NaN when `delinquent_months = 0`

---

<div align="center">
<h2>Feature Selection</h2>
</div>

### Step 1 — Remove ID Columns
`cust_id` and `loan_id` dropped — no predictive value.

### Step 2 — Remove Business-Specified Columns
Removed per business team guidance: `disbursal_date`, `installment_start_dt`, `loan_amount`, `income`, `total_loan_months`, `delinquent_months`, `total_dpd`

### Step 3 — VIF (Variance Inflation Factor)
Removed highly multicollinear features:

| Removed Feature | Reason |
|:---|:---|
| sanction_amount | High VIF |
| processing_fee | High VIF |
| gst | High VIF |
| net_disbursement | High VIF |
| principal_outstanding | High VIF |

### Step 4 — WOE / IV (Information Value)
Only features with **IV > 0.02** were retained for model training.

---

<div align="center">
<h2>Model Training</h2>
</div>

Four training attempts were made, progressively improving on class imbalance and tuning:

| Attempt | Models | Imbalance Handling | Tuning |
|:---|:---|:---|:---|
| **Attempt 1** | Logistic Regression, Random Forest, XGBoost | None | RandomizedSearchCV |
| **Attempt 2** | Logistic Regression, XGBoost | RandomUnderSampler | Best params from Attempt 1 |
| **Attempt 3** | Logistic Regression | SMOTETomek | Optuna (50 trials) |
| **Attempt 4** | XGBoost | SMOTETomek | Optuna (50 trials) |

---

<div align="center">
<h2>Model Results</h2>
</div>

### 🥇 Deployed Model — Logistic Regression (Attempt 3)

```
Algorithm        : Logistic Regression
Imbalance Fix    : SMOTETomek (combined over + under sampling)
Tuning           : Optuna — 50 trials, maximizing macro F1
AUC              : 0.98
Gini Coefficient : 0.96
KS Statistic     : 85.98% (at Decile 8)
Top Decile Rate  : 72% event rate in Decile 9
Serialized via   : joblib → artifacts/model_data.joblib
```

> **Why Logistic Regression?** With proper feature engineering (WOE/IV, VIF), imbalance handling (SMOTETomek), and tuning (Optuna), Logistic Regression delivered outstanding results — AUC 0.98 — while remaining fully interpretable via coefficients. In credit risk, interpretability matters as much as accuracy.

---

<div align="center">
<h2>Model Evaluation</h2>
</div>

### ROC-AUC

| Metric | Value |
|:---|:---:|
| **AUC** | **0.98** |
| **Gini Coefficient** | **0.96** |

> AUC of 0.98 means the model is near-perfect at distinguishing defaulters from non-defaulters. Gini of 0.96 confirms excellent rank-ordering capability.

---

### KS Statistic & Decile Analysis

| Decile | Event Rate | Cum Event Rate | KS Statistic |
|:---:|:---:|:---:|:---:|
| 9 (Top) | 72.00% | 72.6% | — |
| 8 | 12.72% | 98.6% | **85.98% ← Max** |
| 7 and below | Near 0% | ~100% | Decreasing |

**Key Insights:**
- The model concentrates **98.6% of all defaults** within just the **top 2 deciles** — exactly what a production credit risk model needs
- **KS Statistic of 85.98%** at Decile 8 — KS in top 3 deciles and above 40 = strong predictive model ✅
- Deciles 5–0 show **zero events** — the model cleanly separates safe borrowers

---

### Feature Importance

Feature importance was derived from **Logistic Regression coefficients** — showing the exact direction and magnitude of each feature's influence on default probability.

---

<div align="center">
<h2>Key Features</h2>
</div>

```
[+]  Binary classification       →  Default / No Default
[+]  3-dataset merge             →  customers + loans + bureau data
[+]  Business-driven outlier removal → processing_fee/loan_amount >= 0.3
[+]  3 engineered features       →  LTI, Delinquency Ratio, Avg DPD
[+]  VIF-based feature removal   →  Eliminates multicollinearity
[+]  WOE/IV feature selection    →  Keeps only predictive features (IV > 0.02)
[+]  SMOTETomek imbalance fix    →  Combined over + under sampling
[+]  Optuna hyperparameter tuning →  50 trials, macro F1 objective
[+]  Decile/KS/Gini evaluation   →  Industry-standard credit model validation
[+]  Streamlit web app           →  Interactive, real-time prediction interface
[+]  Joblib model export         →  Production-ready serialized model
```

---

<div align="center">
<h2>Live App — CreditIQ</h2>
</div>

<div align="center">

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://credit-risk-modeling-classification-creditiq.streamlit.app/)

</div>

**CreditIQ** is the deployed Streamlit application powered by the Optuna-tuned Logistic Regression model. Users can:

- Enter borrower details (income, loan amount, credit profile, DPD, delinquency data, etc.)
- Get **instant default risk prediction**
- View model confidence via predicted probability
- Simulate how banks assess loan applications in real-time

> **Live URL:** [https://credit-risk-modeling-classification-creditiq.streamlit.app/](https://credit-risk-modeling-classification-creditiq.streamlit.app/)

---

<div align="center">
<h2>Project Structure</h2>
</div>

```
Credit-Risk-Modeling-Classification/
│
├── app/                          # Streamlit web application
│   ├── app.py                    # Main Streamlit app (CreditIQ)
│   └── artifacts/
│       └── model_data.joblib     # Serialized model + scaler + features
│
├── datasets/                     # Raw input data
│   ├── customers.csv
│   ├── loans.csv
│   └── bureau_data.csv
│
├── code.ipynb                    # Complete ML notebook
│   ├── 01 - Data Loading & Merging
│   ├── 02 - Preprocessing & EDA
│   ├── 03 - Feature Engineering (LTI, Delinquency Ratio, Avg DPD)
│   ├── 04 - Feature Selection (VIF + WOE/IV)
│   ├── 05 - Model Training (4 Attempts)
│   ├── 06 - Evaluation (AUC, KS, Gini, Decile Analysis)
│   └── 07 - Model Export (joblib)
│
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

<div align="center">
<h2>Setup & Installation</h2>
</div>

```bash
# 1. Clone the repository
git clone https://github.com/rushikreddie/Credit-Risk-Modeling-Classification.git
cd Credit-Risk-Modeling-Classification

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app locally
streamlit run app/app.py

# 5. Or open the Jupyter Notebook
jupyter notebook code.ipynb
```

---

<div align="center">
<h2>Tech Stack</h2>
</div>

<div align="center">

| Layer | Technology |
|:---|:---|
| **Language** | Python 3.10+ |
| **ML Framework** | Scikit-learn, XGBoost |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Imbalance Handling** | SMOTETomek (imbalanced-learn) |
| **Hyperparameter Tuning** | Optuna |
| **Statistical Analysis** | Statsmodels (VIF) |
| **Model Serialization** | Joblib |
| **Web App** | Streamlit |
| **Environment** | Jupyter Notebook |
| **Deployment** | Streamlit Cloud |

</div>

---

<div align="center">
<h2>Connect with Me</h2>
</div>

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/rushikreddie)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rushikreddie)
[![Live App](https://img.shields.io/badge/CreditIQ-Try%20Live%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://credit-risk-modeling-classification-creditiq.streamlit.app/)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%"/>

<i>If this project helped you, consider leaving a star — it motivates more open-source work.</i>

</div>
