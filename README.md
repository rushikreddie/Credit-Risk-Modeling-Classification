<div align="center">

<!-- Animated Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=CreditIQ&fontSize=80&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Credit%20Risk%20Modeling%20%7C%20Classification%20Engine&descAlignY=55&descSize=18" width="100%"/>

<br/>

<!-- Animated Typing -->
<a href="https://git.io/typing-svg">
 <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=00D4FF&center=true&vCenter=true&width=700&lines=+Predicting+Credit+Risk+with+ML;+CIBIL-Inspired+Scoring+System;+End-to-End+ML+Pipeline+%2B+Streamlit;+Real-time+Risk+Classification+Engine" alt="Typing SVG" />
</a>

<br/><br/>

<!-- Badges -->
[![Live App](https://img.shields.io/badge/%20Live%20App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://credit-risk-modeling-classification-creditiq.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-006400?style=for-the-badge)](https://xgboost.readthedocs.io)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

<br/>

<!-- View Count -->
![Profile Views](https://komarev.com/ghpvc/?username=rushikreddie&color=blueviolet&style=for-the-badge&label=REPO+VIEWS)

</div>

---

## Table of Contents

- [ Project Overview](#-project-overview)
- [ Business Value](#-business-value)
- [ Dataset](#-dataset)
- [ ML Pipeline](#-ml-pipeline)
- [ Models & Accuracy](#-models--accuracy)
- [ Model Comparison](#-model-comparison)
- [ Key Features](#-key-features)
- [ Live App — CreditIQ](#-live-app--creditiq)
- [ Project Structure](#-project-structure)
- [ Setup & Installation](#-setup--installation)
- [ Tech Stack](#-tech-stack)
- [ Connect with Me](#-connect-with-me)

---

<div align="center">
<h2> Project Overview</h2>
</div>

> **CreditIQ** is a production-grade, end-to-end **Credit Risk Classification System** that mirrors the **CIBIL scoring methodology** used by Indian financial institutions. It classifies loan applicants into risk categories — **Poor, Average, Good, and Excellent** — by training and comparing multiple machine learning models on real-world banking and CIBIL data.

This system enables banks, NBFCs, and fintech companies to make **data-driven lending decisions**, reduce default losses, and comply with risk assessment frameworks.

---

<div align="center">
<h2> Business Value</h2>
</div>

<table>
<tr>
<td align="center"></td>
<td><b>Loan Default Prevention</b> — Identifies high-risk borrowers before disbursement, reducing NPAs</td>
</tr>
<tr>
<td align="center"></td>
<td><b>Cost Reduction</b> — Automated risk assessment cuts manual underwriting time by up to 80%</td>
</tr>
<tr>
<td align="center"></td>
<td><b>Real-Time Decisions</b> — Instant classification via Streamlit app for credit officers and analysts</td>
</tr>
<tr>
<td align="center"></td>
<td><b>CIBIL-Aligned Scoring</b> — Categories mirror industry-standard credit rating bands</td>
</tr>
<tr>
<td align="center"></td>
<td><b>Explainability</b> — Feature importance insights reveal the <i>why</i> behind every prediction</td>
</tr>
<tr>
<td align="center"></td>
<td><b>Democratized Access</b> — Web-deployed app makes ML credit scoring available to any institution</td>
</tr>
</table>

---

<div align="center">
<h2> Dataset</h2>
</div>

The project uses a **Leading Indian Bank & CIBIL Real-World Dataset**, containing borrower financial profiles and credit histories. Key features include:
| Feature Category | Examples |
|:---|:---|
| **Financial** | Annual Income, Loan Amount, Outstanding Debt, Monthly EMI |
| **Credit History** | CIBIL Score, Number of Delayed Payments, Credit Utilization Ratio |
| **Demographic** | Age, Employment Type, Years of Employment |
| **Assets** | Home Ownership, Number of Bank Accounts, Credit Cards |
| **Behavioral** | Credit History Age, Number of Hard Inquiries, Payment Behavior |

> **Target Variable:** Multi-class credit risk categories → `Poor` | `Standard` | `Good`

---

<div align="center">
<h2> ML Pipeline</h2>
</div>

```
Raw CIBIL + Bank Data
 │
 ▼
┌─────────────────────┐
│ Data Preprocessing │ ← Handle nulls, encode categoricals, fix data types
└─────────────────────┘
 │
 ▼
┌─────────────────────┐
│ Exploratory Data │ ← Correlation heatmaps, distribution plots, outlier analysis
│ Analysis (EDA) │
└─────────────────────┘
 │
 ▼
┌─────────────────────┐
│ Feature Engineering│ ← Label encoding, ordinal mapping, feature selection
└─────────────────────┘
 │
 ▼
┌─────────────────────┐
│ Class Imbalance │ ← SMOTE / class-weight balancing
│ Handling │
└─────────────────────┘
 │
 ▼
┌─────────────────────┐
│ Model Training & │ ← 6 ML models trained, cross-validated, tuned
│ Hyperparameter │
│ Tuning │
└─────────────────────┘
 │
 ▼
┌─────────────────────┐
│ Model Evaluation │ ← Accuracy, F1-Score, ROC-AUC, Confusion Matrix
└─────────────────────┘
 │
 ▼
┌─────────────────────┐
│ Best Model Saved │ ← Serialized with pickle/joblib
│ (.pkl) │
└─────────────────────┘
 │
 ▼
┌─────────────────────┐
│ Streamlit │ ← CreditIQ — Interactive live web app
│ Deployment │
└─────────────────────┘
```

---

<div align="center">
<h2> Models & Accuracy</h2>
</div>

Six classification algorithms were trained, evaluated, and compared on the CIBIL dataset:

<br/>

### Random Forest Classifier
```
Algorithm : Ensemble of Decision Trees (Bagging)
Accuracy : ~92–93%
Strengths : Handles non-linearity, robust to overfitting, captures feature interactions
Weakness : Slower inference, less interpretable than single trees
Use Case : Primary production model — best balance of accuracy and stability
```
> **Why it works:** Random Forest builds hundreds of decorrelated trees and aggregates votes, making it extremely robust for imbalanced, high-dimensional financial datasets.

---

### XGBoost Classifier
```
Algorithm : Gradient Boosted Trees (Sequential Ensemble)
Accuracy : ~91–92%
Strengths : High predictive power, handles missing values, regularization built-in
Weakness : Computationally intensive, more hyperparameters to tune
Use Case : Runner-up model — excellent for feature-rich datasets
```
> **Why it works:** XGBoost iteratively corrects previous model errors, making it one of the strongest algorithms for structured/tabular financial data.

---

### Decision Tree Classifier
```
Algorithm : Single CART Decision Tree
Accuracy : ~85–87%
Strengths : Fully interpretable, fast, visual decision rules
Weakness : Prone to overfitting without pruning
Use Case : Baseline interpretable model — useful for regulatory explainability
```
> **Why it works:** Decision Trees create human-readable if-then rules that compliance officers can audit and validate.

---

### Logistic Regression
```
Algorithm : Linear Classification (Sigmoid Function)
Accuracy : ~78–82%
Strengths : Simple, fast, probabilistic output, highly interpretable
Weakness : Struggles with non-linear relationships
Use Case : Baseline model and probability calibration reference
```
> **Why it works:** Logistic Regression gives probability estimates (e.g., 72% chance of default), which aligns with how banks communicate credit decisions.

---

### K-Nearest Neighbors (KNN)
```
Algorithm : Instance-Based Learning
Accuracy : ~80–83%
Strengths : No training phase, captures local patterns
Weakness : Slow at inference, sensitive to scale and irrelevant features
Use Case : Pattern-matching on similar borrower profiles
```
> **Why it works:** KNN identifies borrowers who are statistically similar to known defaulters/non-defaulters using distance metrics.

---

### Support Vector Machine (SVM)
```
Algorithm : Maximum Margin Hyperplane Classifier
Accuracy : ~82–85%
Strengths : Effective in high-dimensional space, robust with kernel tricks
Weakness : Does not scale well to very large datasets
Use Case : Strong alternative for complex non-linear boundaries
```
> **Why it works:** SVM finds the optimal decision boundary between risk classes, making it powerful when the classes are not linearly separable.

---

<div align="center">
<h2> Model Comparison</h2>
</div>
| Model | Accuracy | F1-Score | ROC-AUC | Recommended |
|:---|:---:|:---:|:---:|:---:|
| **Random Forest** | **~92–93%** | **High** | **~0.97** | **Best Model** |
| **XGBoost** | ~91–92% | High | ~0.96 | Production Ready |
| **SVM** | ~82–85% | Medium-High | ~0.89 |  Scalability Concern |
| **KNN** | ~80–83% | Medium | ~0.87 |  Slow Inference |
| **Decision Tree** | ~85–87% | Medium-High | ~0.88 | Interpretable |
| **Logistic Regression** | ~78–82% | Medium | ~0.84 | Baseline/Explainable |

> **Winner: Random Forest** — delivers the best combination of accuracy, recall on minority classes, and generalization. Deployed as the production model in CreditIQ.

---

<div align="center">
<h2> Key Features</h2>
</div>

```python
 Multi-class classification → Poor / Standard / Good credit tiers
 CIBIL score integration → Mirrors India's real-world credit bureau logic
 6 ML models compared → Fair benchmark with same train/test split
 Feature importance plots → Know which variables drive credit risk
 Confusion matrix analysis → Understand model error patterns
 Class imbalance handling → Ensures minority class (defaults) are correctly learned
 Streamlit web app → Interactive, real-time prediction interface
 Pickle model export → Production-ready serialized model
 EDA with visualizations → Correlation heatmaps, box plots, distribution charts
```

---

<div align="center">
<h2> Live App — CreditIQ</h2>
</div>

<div align="center">

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://credit-risk-modeling-classification-creditiq.streamlit.app/)

</div>

**CreditIQ** is the deployed Streamlit application powered by the best-performing Random Forest model. Users can:

- Enter borrower details (income, loan amount, CIBIL score, payment history, etc.)
- Get **instant credit risk classification** — Poor / Standard / Good
- View model confidence and risk indicators
- Simulate how banks assess loan applications in real-time

> **Live URL:** [https://credit-risk-modeling-classification-creditiq.streamlit.app/](https://credit-risk-modeling-classification-creditiq.streamlit.app/)

---

<div align="center">
<h2> Project Structure</h2>
</div>

```
 Credit-Risk-Modeling-Classification/
│
├── app/ # Streamlit web application
│ ├── app.py # Main Streamlit app (CreditIQ)
│ ├── model files (.pkl) # Serialized trained model
│ └── helper utilities # Preprocessing & prediction logic
│
├── datasets/ # Raw and processed data
│ └── CIBIL + bank datasets # Leading Indian Bank real-world data
│
├── code.ipynb # Complete ML notebook
│ ├── 01 - Data Loading & EDA
│ ├── 02 - Preprocessing & Feature Engineering
│ ├── 03 - Model Training (6 Models)
│ ├── 04 - Evaluation & Comparison
│ └── 05 - Best Model Export
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

<div align="center">
<h2> Setup & Installation</h2>
</div>

```bash
# 1. Clone the repository
git clone https://github.com/rushikreddie/Credit-Risk-Modeling-Classification.git
cd Credit-Risk-Modeling-Classification

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app locally
cd app
streamlit run app.py

# 5. Or open the Jupyter Notebook
jupyter notebook code.ipynb
```

---

<div align="center">
<h2> Tech Stack</h2>
</div>

<div align="center">
| Layer | Technology |
|:---|:---|
| **Language** | Python 3.10+ |
| **ML Framework** | Scikit-learn, XGBoost |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Imbalance Handling** | SMOTE (imbalanced-learn) |
| **Model Serialization** | Pickle / Joblib |
| **Web App** | Streamlit |
| **Environment** | Jupyter Notebook |
| **Deployment** | Streamlit Cloud |

</div>

---

<div align="center">
<h2> Connect with Me</h2>
</div>

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/rushikreddie)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rushikreddie)
[![Live App](https://img.shields.io/badge/CreditIQ-Try%20Live%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://credit-risk-modeling-classification-creditiq.streamlit.app/)

</div>

---

<div align="center">

<!-- Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%"/>

<i> If this project helped you, give it a star — it motivates more open-source work!</i>

</div>
