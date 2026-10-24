# AI-Based MSME Credit Risk Assistant

> **Final-Year B.Tech Computer Engineering Project**  
> **Differentiating Concept:** PREDICT → EXPLAIN → SIMULATE → IMPROVE

---

## 📌 Project Overview & Problem Statement

Micro, Small, and Medium Enterprises (MSMEs) form the backbone of economic development but frequently face severe credit access bottlenecks. Traditional credit assessment models rely heavily on standardized corporate collateral, audited financial histories, and credit bureau scores, which many MSMEs lack or present in non-standard formats.

This project delivers a **functional, data-driven, and explainable AI decision-support platform** designed specifically for MSME credit risk classification (**LOW**, **MEDIUM**, **HIGH**). Rather than presenting a black-box classification, the system equips credit underwriters and analysts with:
1. **Explainable AI via SHAP** (SHapley Additive exPlanations) for local and global model transparency.
2. **Independent Financial Health Score (0–100)** across 5 operational pillars.
3. **What-If Scenario Simulation Engine** to model parameter modifications (e.g. debt reduction) in real time.
4. **Actionable Risk Improvement Insights** to guide enterprises on creditworthiness enhancement.
5. **SQLite Database Storage** for historical tracking and auditing.
6. **Automated PDF Assessment Report Generation** via ReportLab.

---

## 🌟 Key Differentiating Concept: PREDICT → EXPLAIN → SIMULATE → IMPROVE

```
[ Financial Data Input ]
         ↓
  [ PREDICT RISK ]  ──> Machine Learning Classifier (Logistic Regression / Tree / Forest)
         ↓
  [ EXPLAIN SHAP ]  ──> Local & Global Feature Importance Contributions
         ↓
 [ SIMULATE SCENARIO ] ─> Real-Time Parameter Modification Engine
         ↓
 [ IMPROVE INSIGHTS ] ─> Rule-Based & SHAP-Guided Actionable Recommendations
```

---

## ⚙️ Technology Stack

- **Programming Language:** Python 3.14+
- **Frontend / Web Dashboard:** Streamlit
- **Machine Learning & Preprocessing:** Scikit-Learn, Imbalanced-Learn (`imblearn`)
- **Explainable AI (XAI):** SHAP (SHapley Additive exPlanations)
- **Data Manipulation & Visualization:** Pandas, NumPy, Plotly Express, Matplotlib
- **Database Storage:** SQLite 3
- **Document Generation:** ReportLab (PDF Engine)
- **Unit Testing Suite:** PyTest

---

## 📊 Dataset & Preprocessing

- **Dataset Source:** Synthetic MSME Financial Dataset (1,500 enterprise records) generated via `data/synthetic/generate_dataset.py`.
- **Target Variable:** `risk_category` (**LOW**: 58%, **MEDIUM**: 27%, **HIGH**: 15%).
- **Raw Features:** `business_age`, `annual_revenue`, `annual_expenses`, `existing_debt`, `requested_loan_amount`, `monthly_cash_flow`, `num_employees`, `credit_history_months`, `previous_defaults`, `repayment_history_score`, `credit_utilization_ratio`.
- **Engineered Ratios:**
  - **Debt-to-Income (DTI):** `existing_debt / annual_revenue`
  - **Net Profit & Profit Margin:** `(annual_revenue - annual_expenses) / annual_revenue`
  - **Loan-to-Income:** `requested_loan_amount / annual_revenue`
  - **Debt Ratio:** `existing_debt / annual_revenue`
  - **Cash Flow Coverage:** `(monthly_cash_flow * 12) / requested_loan_amount`
- **Data Leakage Safeguard:** Preprocessing `ColumnTransformer` (StandardScaler & SimpleImputer) is fitted **strictly on training splits**.

---

## ⚖️ Class Imbalance & Resampling

To evaluate minority risk class recall (HIGH Risk: 15%), candidate pipelines were tested with:
- **No Resampling**
- **SMOTE** (Synthetic Minority Over-sampling Technique)
- **ADASYN** (Adaptive Synthetic Sampling)

Resampling is applied **strictly to training folds inside Stratified K-Fold Cross Validation**, leaving test evaluation sets untouched.

---

## 📈 Empirical Model Comparison Results

All metrics are calculated directly from model evaluation scripts on the untouched test set:

| Model Candidate | Resampling Strategy | CV F1-Macro | CV Accuracy | Test Accuracy | Test F1-Macro | Test Precision | Test Recall | Test ROC-AUC |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | **NONE (Selected)** | **0.8671** | **0.8892** | **86.33%** | **0.8344** | **0.8468** | **0.8236** | **0.9680** |
| Logistic Regression | SMOTE | 0.8555 | 0.8708 | — | — | — | — | — |
| Logistic Regression | ADASYN | 0.8533 | 0.8700 | — | — | — | — | — |
| Decision Tree | NONE | 0.7559 | 0.8000 | — | — | — | — | — |
| Decision Tree | ADASYN | 0.7799 | 0.8092 | — | — | — | — | — |
| Random Forest | NONE | 0.8094 | 0.8392 | — | — | — | — | — |
| Random Forest | ADASYN | 0.8040 | 0.8283 | — | — | — | — | — |

---

## 🚀 Installation & Setup Instructions

### 1. Clone & Setup Virtual Environment
```bash
git clone https://github.com/your-username/msme-credit-risk-assistant.git
cd msme-credit-risk-assistant

# Create virtual environment
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate Dataset & Train ML Pipeline
```bash
# Generate synthetic dataset
python data/synthetic/generate_dataset.py

# Train models and save artifacts
python src/train.py
```

### 4. Run PyTest Unit Test Suite
```bash
PYTHONPATH=. pytest
```

### 5. Launch Streamlit Application
```bash
streamlit run app.py
```

---

## 🛡️ Responsible AI & Legal Disclaimer

> **ACADEMIC RESEARCH PROTOTYPE DISCLAIMER:**  
> This application is developed strictly as a B.Tech Computer Engineering final-year research decision-support prototype. It does **NOT** constitute professional financial advice, banking credit underwriting authorization, or institutional loan sanctioning. It does **NOT** automatically approve or reject credit applications. Human underwriting oversight is mandatory.

---

## 📝 License & Citation

Refer to `ACADEMIC_DOCUMENTATION.md` for complete literature review, base paper analysis (Bussmann et al., 2021), methodology, ER diagrams, and viva voce question bank.
