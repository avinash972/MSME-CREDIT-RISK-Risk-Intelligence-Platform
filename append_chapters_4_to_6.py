with open('/Users/avinashsharma/msme_credit_risk_assistant/generate_expanded_final_report.py', 'a') as f:
    f.write('''
# ==============================================================================
# CHAPTER 4: PROJECT PLAN & PROCESS MODEL
# ==============================================================================
doc.add_page_break()
add_heading1("CHAPTER 4: PROJECT PLAN & PROCESS MODEL")

add_heading2("4.1 SOFTWARE ENGINEERING PROCESS MODEL (HYBRID WATERFALL-AGILE)")
add_body("The engineering of financial machine learning software requires both structural predictability (for regulatory compliance, statistical rigor, and strict data leakage prevention) and iterative flexibility (for hyperparameter tuning, user interface usability, and feedback integration). To reconcile these dual objectives, this project adopted an Iterative Waterfall-Agile Hybrid Process Model.")

add_figure(f"{DIAG_DIR}/diag_hybrid_process.png", "Figure 4.1: Iterative Waterfall-Agile Hybrid Process Model Flowchart", width=5.2)

add_body("The hybrid methodology partitions the development lifecycle into two complementary operating regimes:")

add_bullet("1. Waterfall Governance for the Machine Learning Core:", "The foundational components of the machine learning pipeline—including mathematical ratio formulation, data schema definitions, train/test splitting, and ColumnTransformer pipeline creation—followed a disciplined sequential Waterfall progression. Because data leakage can silently invalidate empirical conclusions, the training and evaluation splits were established and frozen at the beginning of development, ensuring that test sets remained 100% untouched throughout all subsequent iterations.")

add_bullet("2. Agile Scrum Sprints for the Interactive Web Application:", "The user-facing software modules—including the Streamlit multi-page interface, Plotly interactive radar charts, real-time What-If scenario sliders, and automated ReportLab PDF compilation—were developed across six bi-weekly Agile sprints. Each sprint delivered an end-to-end working increment that was demonstrated, critiqued, and refined based on user feedback.")

add_figure(f"{DIAG_DIR}/diag3_methodology.png", "Figure 4.2: End-to-End Machine Learning Pipeline and Methodology Flowchart", width=5.2)

add_heading2("4.2 WORK BREAKDOWN STRUCTURE (WBS) & 6-SPRINT ROADMAP")
add_body("The development lifecycle was structured into six distinct, two-week Agile sprints spanning a cumulative 24-week engineering timeframe:")

add_bullet("Sprint 1 (Weeks 1–4): Requirements Formulation & Data Synthesis:", "Conducted foundational literature review of base paper (Bussmann et al., 2021); established problem definition and scope; designed synthetic dataset generator with log-normal revenue distributions, exponential debt ratios, and correlated expenses.")

add_bullet("Sprint 2 (Weeks 5–8): Feature Engineering & Zero-Leakage Preprocessing:", "Implemented mathematical formulas for DTI, Profit Margin, LTI, and Cash Flow Coverage with zero-division protections; built Scikit-Learn ColumnTransformer pipeline integrating SimpleImputer and StandardScaler; verified zero-leakage splitting.")

add_bullet("Sprint 3 (Weeks 9–14): Resampling & Stratified Cross-Validation Benchmarking:", "Integrated SMOTE and ADASYN resampling algorithms; executed Stratified 5-Fold Cross-Validation across candidate classifiers (Multinomial Logistic Regression, Decision Trees, Random Forests, XGBoost); selected champion calibrated estimator.")

add_bullet("Sprint 4 (Weeks 15–18): Explainable AI & Financial Health Engine:", "Integrated SHAP (SHapley Additive exPlanations) LinearExplainer; formulated deterministic 5-Pillar Financial Health Index (0–100) across Debt, Cash Flow, Margins, Repayment, and Stability pillars; validated scoring independence.")

add_bullet("Sprint 5 (Weeks 19–22): What-If Simulation Engine & Streamlit Dashboard:", "Engineered real-time counterfactual simulation engine; developed 9-page responsive Streamlit dashboard featuring dark/light theme adaptability, Plotly KPI gauges, and polar radar charts; integrated ACID-compliant SQLite 3 persistence store.")

add_bullet("Sprint 6 (Weeks 23–24): Automated Testing, PDF Compilation & Final Documentation:", "Constructed PyTest automated unit and integration testing suite covering 7 test modules; implemented ReportLab dynamic multi-page PDF credit assessment report generator; compiled complete project dissertation.")

add_heading2("4.3 GANTT CHART & MILESTONE TIMELINE")
add_body("Table 4.1 details the Work Breakdown Structure (WBS), assigned sprint milestones, scheduled technical activities, and completion status across the 24-week lifecycle:")

t_wbs = doc.add_table(rows=1, cols=4)
style_table(t_wbs, [1.2, 1.6, 3.2, 1.0], ["Sprint / Period", "Milestone / Deliverable", "Core Technical Activities & Scope", "Status"], [
    ["Sprint 1 (W1-W4)", "Requirements & Dataset Design", "Literature survey, base paper review, synthetic dataset generator script", "Completed"],
    ["Sprint 2 (W5-W8)", "Feature Engineering & Preprocessing", "Financial ratio formulations, ColumnTransformer pipeline, unit test fixtures", "Completed"],
    ["Sprint 3 (W9-W14)", "Model Training & Cross-Validation", "SMOTE & ADASYN evaluation inside 5-Fold CV, model selection & tuning", "Completed"],
    ["Sprint 4 (W15-W18)", "XAI & Health Score Engines", "SHAP integration, 5-Pillar health score formulation, What-If simulator", "Completed"],
    ["Sprint 5 (W19-W22)", "UI & Database Architecture", "Streamlit dashboard, SQLite 3NF relational schema, batch upload engine", "Completed"],
    ["Sprint 6 (W23-W24)", "Testing, PDF & Final Report", "PyTest 7 test suites, ReportLab PDF generator, dissertation compilation", "Completed"]
])

add_heading2("4.4 HARDWARE, SOFTWARE & DEVELOPMENT ENVIRONMENT SPECIFICATIONS")
add_body("To ensure complete technical reproducibility and consistent execution, development and benchmarking were conducted under standardized computing environments:")

add_body("Table 4.2 specifies the hardware architecture, operating system platforms, Python runtime, and core dependencies utilized:")

t_env = doc.add_table(rows=1, cols=3)
style_table(t_env, [2.0, 2.2, 2.8], ["Environment Layer", "Specification / Tool", "Technical Version & Configuration"], [
    ["Processor (CPU)", "Apple Silicon M-Series / Intel Core i7", "8-Core CPU with hardware vector extensions"],
    ["Memory & Storage", "16 GB Unified Memory / 512 GB SSD", "Read/Write speeds > 2,500 MB/s; swap enabled"],
    ["Operating System", "macOS Sonoma / Linux Ubuntu 22.04 LTS", "UNIX POSIX-compliant terminal environments"],
    ["Python Runtime", "Python 3.14+ (Virtual Environment `venv`)", "Isolated dependency management via pip"],
    ["Machine Learning Core", "Scikit-Learn 1.9+ & Imbalanced-Learn 0.14+", "ColumnTransformer, StandardScaler, SMOTE, ADASYN"],
    ["Explainable AI", "SHAP 0.52+ (Shapley Additive explanations)", "LinearExplainer, TreeExplainer, Explanations API"],
    ["User Interface", "Streamlit 1.64+ & Plotly 7.1+", "Theme-adaptive wide-layout reactive dashboard"],
    ["Persistence & Reports", "SQLite 3 (Standard Library) & ReportLab 5.0+", "ACID-compliant relational store & PDF flowables"],
    ["Software Testing", "PyTest 9.1+", "Automated unit and integration test runner"]
])

add_heading2("4.5 RISK ASSESSMENT & MITIGATION STRATEGY")
add_body("Developing financial decision-support software involves multiple technical, statistical, and operational risks. Table 4.3 outlines the comprehensive risk matrix, assessing likelihood, potential impact, and engineered mitigation protocols:")

t_risk = doc.add_table(rows=1, cols=4)
style_table(t_risk, [1.5, 1.2, 1.5, 2.8], ["Identified Risk Category", "Severity / Likelihood", "Potential Failure Mode", "Engineered Mitigation Strategy"], [
    ["Data Leakage Risk", "Critical / Medium", "Feature scaling or SMOTE applied prior to train/test split, causing optimistic bias.", "Enforced strict chronological isolation: split data first; fit ColumnTransformer only on train split."],
    ["Numerical Overflow / Zero Division", "High / High", "Pre-revenue or debt-free applicants triggering division-by-zero exceptions in ratios.", "Implemented np.maximum(denominator, 1.0) safeguards across all 7 engineered ratio transformers."],
    ["Class Imbalance Bias", "High / High", "Classifier predicting only majority LOW risk class, missing high-risk defaults.", "Evaluated SMOTE and ADASYN strictly inside 5-Fold CV loops; monitored Macro F1 and Recall."],
    ["Regulatory Black-Box Violation", "Critical / Low", "Supervisory rejection due to inability to explain individual loan denials.", "Integrated game-theoretic SHAP local attributions providing signed mathematical risk drivers."],
    ["UI Bounds Exceptions", "Medium / High", "Out-of-bounds input values crashing Streamlit number_input and slider widgets.", "Engineered safe dynamic clamping (max/min guards) across all interactive input controls."]
])

# ==============================================================================
# CHAPTER 5: SOFTWARE REQUIREMENT SPECIFICATION (SRS)
# ==============================================================================
doc.add_page_break()
add_heading1("CHAPTER 5: SOFTWARE REQUIREMENT SPECIFICATION (SRS)")

add_heading2("5.1 PROJECT SCOPE & SYSTEM BOUNDARY SPECIFICATION")
add_body("The Software Requirement Specification (SRS) establishes the complete functional and non-functional contracts governing the AI-Based MSME Credit Risk Assistant platform. The software operates as an interactive, web-based analytics and decision-support tool capable of evaluating individual enterprise profiles, processing large batch datasets, explaining risk predictions, simulating counterfactual financial scenarios, and generating verifiable audit reports.")

add_body("System boundaries are strictly delineated: the software ingests validated accounting inputs and outputs calibrated classifications, health scores, and explainability attributions. It does not interface directly with bank core banking ledgers for automatic loan disbursement, nor does it conduct automated credit bureau scraping.")

add_heading2("5.2 USER CLASSES & STAKEHOLDER PERSONA ANALYSIS")
add_body("The software caters to three primary user classes with distinct operational responsibilities:")

add_bullet("1. Commercial Credit Underwriters & Loan Officers:", "Financial analysts requiring rapid, objective credit risk stratification (LOW, MEDIUM, HIGH), calibrated default probabilities, and transparent SHAP explanations to substantiate loan recommendations before credit committees.")

add_bullet("2. Enterprise Risk Managers & Compliance Auditors:", "Supervisory personnel responsible for monitoring portfolio-level risk distributions, default trends, model calibration curves, and ensuring that automated credit decisions comply with RBI and Basel supervisory mandates.")

add_bullet("3. MSME Borrowers & Financial Advisors:", "Small business owners seeking diagnostic insights into their creditworthiness and utilizing the What-If simulation engine to discover concrete operational adjustments (e.g., debt reduction) that enhance credit eligibility.")

add_heading2("5.3 DETAILED FUNCTIONAL REQUIREMENTS (FR-01 TO FR-12)")
add_body("The software implements twelve formal functional requirements. Table 5.1 details the functional requirements specification matrix, specifying input data, processing logic, expected output, and exception handling protocols:")

t_fr = doc.add_table(rows=1, cols=4)
style_table(t_fr, [1.2, 1.8, 2.2, 1.8], ["Req ID & Name", "Input Parameters", "Internal Processing Logic", "Expected System Output"], [
    ["FR-01: Input Validation", "Raw business profile & financial values", "Validates positive boundaries, non-negative bounds, and non-empty strings", "Validated input dictionary or descriptive validation error list"],
    ["FR-02: Ratio Engineering", "Revenue, expenses, debt, loan, cash flow", "Computes DTI, Profit Margin, LTI, Cash Flow Coverage with zero-division clamps", "Transformed dictionary containing 7 standardized financial ratios"],
    ["FR-03: Preprocessing Pipeline", "Raw and engineered feature vector", "Applies SimpleImputer and StandardScaler via serialized ColumnTransformer", "Normalized 18-dimensional numeric NumPy feature array"],
    ["FR-04: Risk Classification", "Normalized feature array", "Passes feature array through champion calibrated Logistic Regression model", "Multi-class classification (LOW, MED, HIGH) & calibrated probabilities"],
    ["FR-05: SHAP Explainability", "Normalized feature array & model", "Computes local Shapley values via LinearSHAP explainer", "Signed directional risk attributions & global feature importance rankings"],
    ["FR-06: Financial Health Scoring", "Financial statement metrics", "Calculates deterministic 0-100 score across 5 operational pillars", "Total health score, pillar breakdown (0-25), and assigned letter grade"],
    ["FR-07: What-If Simulation", "Modified parameter dictionary", "Updates input vector, recomputes ratios, and evaluates delta predictions", "Instantaneous probability deltas & financial health score shift"],
    ["FR-08: Actionable Insights", "SHAP values & health scores", "Maps negative SHAP attributions to operational recommendations", "Bulleted turnaround roadmap targeting high-impact risk amplifiers"],
    ["FR-09: Batch Ingestion", "Uploaded CSV or Excel spreadsheet", "Validates columns, standardizes headers, and vectorizes batch inference", "Batch summary metrics, risk distribution chart, and downloadable CSV"],
    ["FR-10: Schema Normalization", "Heterogeneous external CSV columns", "Fuzzy header matching and standard schema translation", "Standardized DataFrame ready for vectorized ML inference"],
    ["FR-11: Database Persistence", "Enterprise profile & prediction state", "Executes parameterized SQLite INSERT into 3NF normalized tables", "Unique auto-incremented business_id and foreign-key audit log"],
    ["FR-12: PDF Report Compilation", "Assessment payload & business data", "Compiles styled ReportLab flowables, tables, and disclaimers into PDF", "Downloadable, institutional-grade multi-page PDF credit assessment report"]
])

add_heading2("5.4 COMPREHENSIVE NON-FUNCTIONAL REQUIREMENTS (NFR-01 TO NFR-08)")
add_body("Table 5.2 defines the non-functional performance, security, and quality requirements governing the system:")

t_nfr = doc.add_table(rows=1, cols=3)
style_table(t_nfr, [1.5, 2.2, 3.3], ["Req ID & Parameter", "Target Metric / Specification", "Architectural Compliance Verification"], [
    ["NFR-01: Inference Latency", "< 500 milliseconds for single assessment", "Empirically verified in Chapter 8: average CPU inference latency is 42 ms."],
    ["NFR-02: Zero Data Leakage", "100% isolation of test and validation splits", "ColumnTransformer fitted strictly on train split; resampling applied inside CV."],
    ["NFR-03: Security & Injection", "Zero SQL injection vulnerability; no secrets", "100% parameterized queries via Python sqlite3; zero hardcoded secrets."],
    ["NFR-04: Batch Scalability", "Process 250,000+ records in < 1.0 second", "Vectorized inference engine processes 272,650 rows in 0.12 seconds."],
    ["NFR-05: Theme Adaptability", "Seamless Dark and Light theme rendering", "CSS variables and theme-adaptive Plotly charts configured in Streamlit."],
    ["NFR-06: Audit Traceability", "Complete historical state preservation", "Complete input feature vector persisted as serialized JSON in predictions table."],
    ["NFR-07: Cross-Platform Support", "macOS, Linux Ubuntu, Windows 11", "Fully compatible with standard Python virtual environments (`venv`)."],
    ["NFR-08: Code Maintainability", "Modular architecture with > 90% test coverage", "PyTest 7 test suites passing in 0.76 seconds across all core packages."]
])

add_heading2("5.5 EXTERNAL INTERFACE REQUIREMENTS")
add_body("The software implements well-defined external interface specifications:")

add_bullet("• User Interfaces:", "Streamlit 1.64+ browser interface delivering a responsive dashboard layout with Plus Jakarta Sans typography, metric KPI cards, semi-circular gauges, polar radar charts, and interactive parameter sliders.")

add_bullet("• Hardware Interfaces:", "Standard multi-core x86-64 and Apple Silicon ARM64 processors with minimum 4 GB RAM and 100 MB free disk space.")

add_bullet("• Software & Storage Interfaces:", "SQLite 3 file-based relational database store operating with ACID guarantees and WAL (Write-Ahead Logging) journaling.")

# ==============================================================================
# CHAPTER 6: SYSTEM DESIGN & ARCHITECTURE
# ==============================================================================
doc.add_page_break()
add_heading1("CHAPTER 6: SYSTEM DESIGN & ARCHITECTURE")

add_heading2("6.1 MULTI-TIER ENTERPRISE SOFTWARE ARCHITECTURE")
add_body("The software implements a modular, multi-tier software architecture enforcing strict separation of concerns between presentation, business logic, machine learning inference, and data persistence layers:")

add_figure(f"{DIAG_DIR}/diag2_architecture.png", "Figure 6.1: Multi-Tier Software and Architectural Block Diagram", width=5.2)

add_body("The four decoupled architectural tiers operate as follows:")

add_bullet("1. Presentation Tier (Streamlit Reactive Engine):", "Delivers an interactive browser-based dashboard utilizing responsive layout primitives, custom financial KPI cards, Plotly semi-circular gauges, 5-pillar radar charts, and reactive parameter sliders.")

add_bullet("2. Business Logic & Feature Pipeline Tier:", "Validates raw accounting inputs, applies zero-division protected ratio transformations, and feeds data into serialized Scikit-Learn ColumnTransformer pipelines.")

add_bullet("3. Machine Learning & Explainability Tier:", "Houses the champion calibrated multinomial logistic estimator (`model.pkl`), the SHAP LinearExplainer, the 5-pillar health score engine, and the What-If counterfactual delta calculator.")

add_bullet("4. Persistence & Output Tier:", "Consists of an ACID-compliant SQLite 3 database operating in Third Normal Form (3NF) and the ReportLab PDF compilation engine.")

add_heading2("6.2 DATA FLOW DIAGRAMS (DFD LEVEL 0, LEVEL 1, LEVEL 2)")
add_body("The flow of information through the system is formally specified across three hierarchical Data Flow Diagram levels:")

add_figure(f"{DIAG_DIR}/diag_dfd_level0.png", "Figure 6.2: Data Flow Diagram Level 0 (Context Level Diagram)", width=5.2)

add_body("The Level 0 Context Diagram depicts the primary external entity (Underwriter / Borrower) submitting financial metrics and receiving calibrated risk classifications, SHAP explanations, health scores, and PDF audit reports, with bidirectional communication to the SQLite Audit Database.")

add_body("In the Level 1 Subsystem Flow, incoming financial data traverses three sequential processing subsystems: (1) Input Validation & Ratio Engineering Subsystem, (2) ML Inference & Explainability Subsystem, and (3) Reporting & Database Persistence Subsystem. Each subsystem performs isolated transformations and passes typed payloads to downstream modules.")

add_heading2("6.3 UML DESIGN (USE CASE & SEQUENCE DIAGRAMS)")
add_body("The behavioral interactions between system actors and software components are formalized through UML Use Case and Sequence diagrams:")

add_figure(f"{DIAG_DIR}/diag_use_case.png", "Figure 6.3: UML Use Case Diagram for Primary System Actors", width=5.2)

add_body("Figure 6.3 details the seven core use cases (UC-1 to UC-7) mapped across Credit Underwriters, MSME Borrowers, and Risk Managers. In the primary Single Assessment Sequence Workflow, the loan officer enters applicant metrics into the Streamlit form; the interface dispatches the data to `src/preprocessing.py`; the engineered feature array is evaluated concurrently by `src/predict.py` (for default probability) and `src/financial_health.py` (for the 0–100 index); `src/explain.py` computes Shapley attributions; and the combined assessment payload is persisted to SQLite and rendered on screen.")

add_heading2("6.4 RELATIONAL DATABASE DESIGN (3NF SCHEMA)")
add_body("The persistence layer is structured across three normalized relational tables in Third Normal Form (3NF) to eliminate data redundancy and preserve complete audit traceability:")

add_figure(f"{DIAG_DIR}/diag4_er_schema.png", "Figure 6.4: Database Entity-Relationship (ER) Relational Schema (3NF)", width=5.2)

add_body("Table 6.1 details the database data dictionary, documenting table structures, column data types, key constraints, and business integrity rules:")

t_dd = doc.add_table(rows=1, cols=4)
style_table(t_dd, [1.4, 1.4, 1.4, 2.8], ["Table Name", "Column Name", "Data Type", "Constraints & Description"], [
    ["businesses", "business_id", "INTEGER", "PRIMARY KEY, AUTOINCREMENT. Unique enterprise identifier."],
    ["businesses", "business_name", "VARCHAR(255)", "NOT NULL. Official registered name of the enterprise."],
    ["businesses", "business_age", "REAL", "NOT NULL, CHECK (business_age >= 0.0). Operating years."],
    ["businesses", "num_employees", "INTEGER", "NOT NULL, CHECK (num_employees >= 1). Total headcount."],
    ["businesses", "created_at", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP. Registration timestamp."],
    ["financial_data", "financial_id", "INTEGER", "PRIMARY KEY, AUTOINCREMENT. Unique financial record ID."],
    ["financial_data", "business_id", "INTEGER", "FOREIGN KEY REFERENCES businesses(business_id) ON DELETE CASCADE."],
    ["financial_data", "annual_revenue", "REAL", "NOT NULL, CHECK (annual_revenue >= 0.0). Gross annual turnover."],
    ["financial_data", "annual_expenses", "REAL", "NOT NULL, CHECK (annual_expenses >= 0.0). Operating expenses."],
    ["financial_data", "existing_debt", "REAL", "NOT NULL, CHECK (existing_debt >= 0.0). Total bank liabilities."],
    ["financial_data", "requested_loan", "REAL", "NOT NULL, CHECK (requested_loan >= 0.0). Applied facility quantum."],
    ["financial_data", "monthly_cash_flow", "REAL", "NOT NULL. Net operational monthly cash flow."],
    ["financial_data", "credit_history_months", "INTEGER", "NOT NULL, CHECK (credit_history_months >= 0). Bureau history."],
    ["financial_data", "previous_defaults", "INTEGER", "NOT NULL, CHECK (previous_defaults >= 0). Prior default count."],
    ["financial_data", "repayment_score", "REAL", "NOT NULL, CHECK (repayment_score BETWEEN 0.0 AND 100.0)."],
    ["financial_data", "credit_utilization", "REAL", "NOT NULL, CHECK (credit_utilization BETWEEN 0.0 AND 1.0)."],
    ["predictions", "prediction_id", "INTEGER", "PRIMARY KEY, AUTOINCREMENT. Unique prediction audit ID."],
    ["predictions", "business_id", "INTEGER", "FOREIGN KEY REFERENCES businesses(business_id) ON DELETE CASCADE."],
    ["predictions", "risk_category", "VARCHAR(20)", "NOT NULL, CHECK (risk_category IN ('LOW', 'MEDIUM', 'HIGH'))."],
    ["predictions", "prob_low", "REAL", "NOT NULL, CHECK (prob_low BETWEEN 0.0 AND 1.0). Calibrated prob."],
    ["predictions", "prob_medium", "REAL", "NOT NULL, CHECK (prob_medium BETWEEN 0.0 AND 1.0). Calibrated prob."],
    ["predictions", "prob_high", "REAL", "NOT NULL, CHECK (prob_high BETWEEN 0.0 AND 1.0). Calibrated prob."],
    ["predictions", "health_score", "REAL", "NOT NULL, CHECK (health_score BETWEEN 0.0 AND 100.0). 5-pillar score."],
    ["predictions", "model_version", "VARCHAR(50)", "NOT NULL. Model version tag (e.g., '1.0.0')."],
    ["predictions", "raw_input_json", "TEXT", "NOT NULL. Complete serialized JSON snapshot of all inputs."],
    ["predictions", "created_at", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP. Inference audit timestamp."]
])

add_heading2("6.5 ZERO-LEAKAGE MACHINE LEARNING PIPELINE DESIGN ARCHITECTURE")
add_body("A pivotal software engineering achievement of this project is the rigorous elimination of data leakage across the machine learning lifecycle. In conventional flawed machine learning implementations, preprocessing transformations (such as computing feature means and standard deviations) and synthetic oversampling algorithms (such as SMOTE) are inadvertently executed on the entire dataset prior to splitting. This fatally contaminates the training distribution with statistical parameters from the validation and test sets, yielding overly optimistic evaluation metrics that collapse in production environments.")

add_figure(f"{DIAG_DIR}/diag_zero_leakage.png", "Figure 6.5: Zero-Leakage Training and Resampling Architecture", width=5.2)

add_body("Our architecture enforces a strict three-phase chronological isolation protocol:")

add_bullet("Phase 1: Stratified Train/Test Partitioning:", "The raw dataset (N=1,500) is partitioned into an 80% training set (N=1,200) and a 20% test set (N=300) using Stratified K-Fold sampling based on target risk tiers. The 300 test samples are immediately quarantined on disk and remain 100% untouched until final benchmarking.")

add_bullet("Phase 2: Training Split ColumnTransformer Fitting:", "The Scikit-Learn ColumnTransformer pipeline (incorporating median SimpleImputer and StandardScaler) is fitted strictly and solely on the 1,200 training instances. The resulting transformer is serialized to `models/preprocessing.pkl`.")

add_bullet("Phase 3: Resampling Encapsulated Strictly Inside Cross-Validation:", "During Stratified 5-Fold Cross-Validation, SMOTE and ADASYN synthetic oversampling are applied exclusively to the training folds of each iteration. Validation folds and the final test set are never subjected to synthetic oversampling, guaranteeing zero data leakage and empirically valid generalization metrics.")

print("Chapters 4 to 6 appended successfully.")
''')
print("Successfully wrote append_chapters_4_to_6.py")
