import sys
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

TEMPLATE_PATH = '/Users/avinashsharma/.gemini/antigravity/brain/b298ac1f-7377-49f3-aa32-b17f7ce447fb/.user_uploaded/media_1792495787257_abbc31cd.pptx'
OUTPUT_PROJECT = '/Users/avinashsharma/msme_credit_risk_assistant/MSME_Credit_Risk_Assistant_Presentation.pptx'
OUTPUT_DESKTOP = '/Users/avinashsharma/Desktop/MSME_Credit_Risk_Assistant_Presentation.pptx'

prs = pptx.Presentation(TEMPLATE_PATH)

def format_paragraph(p, text, font_size=Pt(16), bold=False, color=RGBColor(30, 41, 59), space_after=Pt(8), level=0):
    p.text = text
    p.font.name = 'Arial'
    p.font.size = font_size
    p.font.bold = bold
    p.font.color.rgb = color
    p.space_after = space_after
    p.level = level

# ==========================================
# SLIDE 1: Title Slide
# ==========================================
s1 = prs.slides[0]
for shp in s1.shapes:
    if shp.name == 'TextBox 8': # Project Title
        tf = shp.text_frame
        tf.clear()
        p = tf.paragraphs[0]
        format_paragraph(p, "AI-BASED MSME CREDIT RISK ASSISTANT", font_size=Pt(28), bold=True, color=RGBColor(26, 54, 93), space_after=Pt(4))
        p2 = tf.add_paragraph()
        format_paragraph(p2, "An Explainable Machine Learning & Financial Health Decision-Support System", font_size=Pt(16), bold=False, color=RGBColor(71, 85, 105), space_after=Pt(0))
    elif shp.name == 'TextBox 9': # Submitted by
        tf = shp.text_frame
        tf.clear()
        p = tf.paragraphs[0]
        format_paragraph(p, "Submitted by:", font_size=Pt(14), bold=True, color=RGBColor(30, 41, 59), space_after=Pt(2))
        p2 = tf.add_paragraph()
        format_paragraph(p2, "Avinash Sharma – [PRN]", font_size=Pt(14), bold=False, color=RGBColor(71, 85, 105), space_after=Pt(2))
        p3 = tf.add_paragraph()
        format_paragraph(p3, "[Project Partner Name] – [PRN]", font_size=Pt(14), bold=False, color=RGBColor(71, 85, 105), space_after=Pt(0))
    elif shp.name == 'TextBox 10': # Guide
        tf = shp.text_frame
        tf.clear()
        p = tf.paragraphs[0]
        format_paragraph(p, "Project Guide:", font_size=Pt(14), bold=True, color=RGBColor(30, 41, 59), space_after=Pt(2))
        p2 = tf.add_paragraph()
        format_paragraph(p2, "[Guide Name]", font_size=Pt(14), bold=False, color=RGBColor(71, 85, 105), space_after=Pt(2))
        p3 = tf.add_paragraph()
        format_paragraph(p3, "Academic Year: 2025–2026", font_size=Pt(14), bold=False, color=RGBColor(71, 85, 105), space_after=Pt(0))
    elif shp.name == 'TextBox 11': # Presentation review
        tf = shp.text_frame
        tf.clear()
        p = tf.paragraphs[0]
        format_paragraph(p, "B.Tech. Major Project Presentation | Final Stage Review", font_size=Pt(13), bold=True, color=RGBColor(100, 116, 139), space_after=Pt(0))

# ==========================================
# SLIDES 2 to 21 DATA DEFINITION
# ==========================================
slide_content = {
    2: {
        "title": "Presentation Roadmap",
        "bullets": [
            ("01. Introduction & Domain Background", "Socio-economic relevance of MSMEs, credit rationing challenges, and the need for explainability."),
            ("02. Problem Statement, Objectives & Scope", "Addressing class imbalance, lack of interpretability, and formalizing measurable project goals."),
            ("03. Literature Review & Research Gap", "Comparative study of credit scoring literature, base paper foundation, and identified research gap."),
            ("04. Proposed System & Architecture", "The PREDICT -> EXPLAIN -> SIMULATE -> IMPROVE paradigm and multi-tiered software architecture."),
            ("05. Methodology & Feature Engineering", "Zero-leakage data preprocessing, financial ratio formulations, and SMOTE/ADASYN resampling inside CV."),
            ("06. Empirical Results & Discussion", "Cross-validation benchmarks, champion model selection, test set metrics, and confusion matrix analysis."),
            ("07. Explainable AI (SHAP) & What-If Engine", "Global feature rankings, local instance Shapley attribution, and counterfactual simulation modeling."),
            ("08. Conclusion & Future Directions", "Key research contributions, practical limitations, and high-impact future enhancements.")
        ]
    },
    3: {
        "title": "Introduction / Background",
        "bullets": [
            ("Significance of the MSME Sector:", "Micro, Small, and Medium Enterprises (MSMEs) drive ~30% of India's GDP, 45% of manufacturing exports, and employ 110M+ individuals."),
            ("The Credit Rationing Dilemma:", "Despite their economic vitality, over 70% of viable MSMEs suffer from formal credit rationing due to non-standard accounting and collateral deficits."),
            ("Information Asymmetry in Lending:", "Traditional banking credit underwriting mandates audited multi-year statements, penalizing nascent and informal enterprises."),
            ("The Black-Box AI Challenge:", "Modern automated machine learning algorithms often lack interpretability, violating financial compliance (RBI / Basel III) and rejecting credit without justification."),
            ("Proposed Decision-Support Solution:", "Develop an explainable AI/ML decision-support system that predicts risk, explains mathematical drivers, simulates scenarios, and guides turnaround.")
        ]
    },
    4: {
        "title": "Problem Statement & Motivation",
        "bullets": [
            ("Core Problem Statement:", "Automated credit risk assessment for MSMEs suffers from severe class imbalance (few historical defaults), data heterogeneity, and a complete absence of transparent interpretability."),
            ("Limitations of Existing Solutions:", "Traditional credit bureau scores (e.g. CIBIL) are backward-looking and static; commercial AI scoring models act as opaque 'black boxes' offering zero actionable borrower feedback."),
            ("The Underwriting Gap:", "Loan underwriters are forced to choose between slow, subjective manual verification and unexplainable automated algorithmic decisions."),
            ("Project Motivation:", "Bridge the divide between high predictive accuracy and regulatory explainability while providing counterfactual guidance for enterprise credit improvement."),
            ("Expected Project Impact:", "Accelerates appraisal turnaround time, eliminates underwriter bias, guarantees regulatory compliance via SHAP, and reduces non-performing assets (NPAs).")
        ]
    },
    5: {
        "title": "Aim, Objectives & Scope",
        "bullets": [
            ("Project Aim:", "To design, develop, and empirically validate an explainable machine learning decision-support platform for multi-class MSME credit risk classification and simulation."),
            ("Objective 1 (Data & Feature Pipeline):", "Formulate domain-specific financial ratios (DTI, Profit Margin, Cash Flow Coverage) with zero-division safeguards."),
            ("Objective 2 (Leakage-Free Resampling):", "Implement and evaluate SMOTE and ADASYN strictly within Stratified K-Fold cross-validation splits to handle class imbalance."),
            ("Objective 3 (Model Benchmarking):", "Train, evaluate, and calibrate candidate classifiers across Macro F1, Recall, and ROC-AUC on an untouched test set."),
            ("Objective 4 (Explainable AI & Simulation):", "Integrate Game-Theoretic SHAP for local/global explainability and build a real-time counterfactual What-If simulation engine."),
            ("Objective 5 (End-to-End Delivery):", "Deploy a responsive web dashboard with SQLite audit persistence and automated institutional PDF report generation."),
            ("Project Scope & Boundaries:", "Decision-support prototype for risk classification (Low, Medium, High); does NOT auto-approve/reject loans or replace human underwriting authority.")
        ]
    },
    6: {
        "title": "Literature Review",
        "bullets": [
            ("Bussmann et al. (2021) [Base Paper]:", "'Explainable Machine Learning in Credit Risk Management', Computational Economics. Demonstrated Shapley values (SHAP) on European SME credit data to reveal non-linear risk drivers while emphasizing regulatory compliance."),
            ("Chawla et al. (2002):", "'SMOTE: Synthetic Minority Over-sampling Technique', JAIR. Established synthetic interpolation of minority samples in feature space, proving essential for imbalanced credit default distributions."),
            ("Ciampi et al. (2020):", "'SME Default Prediction with Machine Learning', EJOR. Benchmarked machine learning algorithms on SME balance sheets, concluding that financial ratio engineering significantly outperforms raw accounting values."),
            ("Lundberg & Lee (2017):", "'A Unified Approach to Interpreting Model Predictions (SHAP)', NeurIPS. Established additive feature attribution rooted in cooperative game theory, guaranteeing local accuracy, missingness, and consistency."),
            ("Summary of Synthesis:", "Existing literature confirms the power of ratio engineering, resampling, and Shapley values, but lacks unified, interactive decision-support implementations.")
        ]
    },
    7: {
        "title": "Existing System & Research Gap",
        "bullets": [
            ("Current Industrial Workflow:", "Manual credit underwriting reliant on physical visits, audited balance sheets, subjective discretion, and rigid credit bureau cutoffs (weeks of latency)."),
            ("Key Limitations of Existing Systems:", "Subjective bias, extreme vulnerability to class imbalance, static risk assessment, and zero transparency regarding why an applicant was rejected."),
            ("Identified Research Gap:", "Academic literature treats predictive classification, imbalance handling, and SHAP explainability in theoretical silos; no unified system bridges prediction with counterfactual simulation and automated client reporting in an MSME context."),
            ("How This Project Addresses the Gap:", "Implements the closed-loop PREDICT -> EXPLAIN -> SIMULATE -> IMPROVE paradigm in an interactive, audit-ready software application.")
        ]
    },
    8: {
        "title": "Proposed System",
        "bullets": [
            ("System Overview:", "An end-to-end intelligent credit risk assessment platform that processes financial statements, classifies risk tiers, explains drivers, and models interventions."),
            ("Core Differentiating Concept:", "• PREDICT: Calibrated 3-tier risk classification (LOW, MEDIUM, HIGH).\n• EXPLAIN: SHAP waterfall and directional bar plots identifying positive and negative risk contributors.\n• SIMULATE: Real-time What-If scenario sliders calculating probability and health score deltas.\n• IMPROVE: Rule-based actionable recommendations to guide enterprises toward credit eligibility."),
            ("Independent 5-Pillar Financial Health Score:", "Deterministic 0–100 index assessing Debt Management, Liquidity, Profitability, Repayment, and Stability."),
            ("Target User Groups:", "Commercial bank credit underwriters, NBFC loan officers, credit rating analysts, and MSME financial advisors."),
            ("Operational Constraints:", "Designed strictly as a decision-support system; human credit underwriters retain final sanctioning authority.")
        ]
    },
    9: {
        "title": "System Architecture / Block Diagram",
        "bullets": [
            ("Presentation Layer (Streamlit GUI):", "Responsive web UI with dark/light mode, executive KPI cards, Plotly semi-circular gauges, 5-pillar radar charts, and interactive parameter sliders."),
            ("Inference & Business Logic Engine:", "• Validation: Form constraints and boundary enforcement.\n• Ratio Transformer: Calculates DTI, Profit Margin, Loan-to-Income, and Cash Flow Coverage.\n• Pipeline Transformer: Scikit-learn ColumnTransformer (StandardScaler + SimpleImputer) fitted strictly on training data."),
            ("Model Execution & XAI Layer:", "• Classifier: Persisted optimal pipeline (`model.pkl` & `preprocessing.pkl`).\n• SHAP Engine: Linear & Tree Explainers for global importance and local instance attributions.\n• Scenario Engine: Counterfactual delta evaluator without model retraining."),
            ("Persistence & Reporting Layer:", "• SQLite Database: Normalized relational schema (`businesses`, `financial_data`, `predictions`).\n• PDF Engine: ReportLab document generator creating downloadable institutional audit reports.")
        ]
    },
    10: {
        "title": "Methodology / Workflow",
        "bullets": [
            ("Step 1 (Data Synthesis & Validation):", "Generated 1,500 realistic MSME records with log-normal revenue distributions, real-world expense variances, and domain noise."),
            ("Step 2 (Feature Engineering):", "Constructed domain ratios: Debt-to-Income (DTI), Profit Margin, Loan-to-Income, Cash Flow Coverage, and Debt Ratio with zero-division safeguards."),
            ("Step 3 (Strict Train-Test Isolation):", "Stratified 80/20 train-test split (N_train=1,200, N_test=300); preprocessing ColumnTransformer fitted strictly on training splits."),
            ("Step 4 (Imbalance Resampling & Stratified 5-Fold CV):", "Evaluated None vs. SMOTE vs. ADASYN inside each training fold to guarantee zero data leakage into validation/test data."),
            ("Step 5 (Model Benchmarking & Selection):", "Evaluated Logistic Regression, Decision Tree, and Random Forest; selected champion model based on CV Macro F1."),
            ("Step 6 (XAI & Deployment):", "Integrated SHAP explainability, deterministic scoring, What-If simulation engine, and interactive dashboard.")
        ]
    },
    11: {
        "title": "Technology Stack & Tools",
        "bullets": [
            ("Core Programming Language:", "Python 3.14+ (Typing, Multiprocessing, Modular package architecture)"),
            ("Machine Learning & Preprocessing:", "Scikit-Learn (Pipelines, Estimators, ColumnTransformer), Imbalanced-Learn (imblearn SMOTE/ADASYN), NumPy, Pandas"),
            ("Explainable AI (XAI):", "SHAP (SHapley Additive exPlanations - LinearExplainer & TreeExplainer for cooperative game-theoretic feature attribution)"),
            ("Frontend Dashboard & Visualization:", "Streamlit (Multi-page reactive web UI), Plotly Express & Graph Objects (Interactive gauges, radar charts, heatmaps)"),
            ("Data Persistence & PDF Generation:", "SQLite 3 (ACID-compliant relational store with parameterized SQL), ReportLab 5.0 (Automated institutional PDF report generation)"),
            ("Testing & Tooling:", "PyTest (Automated unit test execution), Joblib (Model serialization), Git (Version control)")
        ]
    },
    12: {
        "title": "System Design / UML",
        "bullets": [
            ("Relational Database Schema (3 Normalized Tables):", "• 'businesses': PK business_id, business_name, business_age, num_employees, created_at\n• 'financial_data': PK financial_id, FK business_id, revenue, expenses, debt, loan_amount, cash_flow, credit_history, defaults, repayment_score, credit_utilization\n• 'predictions': PK prediction_id, FK business_id, risk_category, probabilities [Low, Med, High], financial_health_score, model_version, raw_input_json, created_at"),
            ("Key Design Decisions:", "• Third Normal Form (3NF) design preventing data redundancy and update anomalies.\n• Parameterized SQL queries preventing SQL injection vulnerabilities.\n• Preserved full raw input snapshots in JSON to enable exact historical audit re-evaluations."),
            ("Architectural Decoupling:", "Complete separation between offline training pipelines (`src/train.py`) and online inference micro-services (`src/predict.py`).")
        ]
    },
    13: {
        "title": "Implementation",
        "bullets": [
            ("Feature Engineering Module (`src/feature_engineering.py`):", "Computes financial indicators with zero-division safeguards: DTI = Debt/Revenue, Profit Margin = (Rev-Exp)/Rev, Loan-to-Income = Loan/Rev, Cash Flow Coverage = (Monthly CF × 12)/Loan."),
            ("5-Pillar Financial Health Score (`src/financial_health.py`):", "Deterministic 0–100 index evaluated across 5 weighted pillars: Debt Management (25 pts), Liquidity (25 pts), Profitability (20 pts), Repayment (20 pts), and Business Stability (10 pts)."),
            ("Explainable AI Engine (`src/explain.py`):", "Calculates local directional Shapley attributions, partitioning features into risk-increasing drivers (SHAP > 0) vs. risk-decreasing drivers (SHAP < 0)."),
            ("Scenario Simulation Engine (`src/scenario.py`):", "Passes user-modified feature vectors through the saved preprocessor and model, computing instantaneous probability and health score deltas without retraining."),
            ("Streamlit Application (`app.py`):", "Interactive platform featuring single risk appraisal, batch dataset CSV/Excel uploads, 5-pillar radar charts, and instant PDF report export.")
        ]
    },
    14: {
        "title": "Testing Strategy",
        "bullets": [
            ("Automated PyTest Testing Suite:", "7 unit tests executed with a 100% pass rate (`PYTHONPATH=. pytest`)."),
            ("Feature Engineering Tests (`test_features.py`):", "Validates ratio calculation formulas and verifies mathematical stability under zero revenue/zero debt edge cases."),
            ("Preprocessing Pipeline Tests (`test_preprocessing.py`):", "Verifies duplicate record elimination, negative value clipping, credit score boundary clamping (0–100), and transformer output dimensionality."),
            ("Inference & Scenario Tests (`test_prediction.py`):", "Validates that predicted probabilities strictly sum to 100% and checks that debt reduction correctly improves financial health deltas."),
            ("Database Persistence Tests (`test_database.py`):", "Verifies SQLite table creation, foreign-key relational integrity, cascading record deletions, and aggregate dashboard metrics."),
            ("Test Isolation:", "Executed against temporary test databases (`data/test_msme.db`) with automated teardown fixtures.")
        ]
    },
    15: {
        "title": "Results & Discussion",
        "bullets": [
            ("Model Comparison Matrix (Stratified 5-Fold Cross-Validation on Training Set):", "• Logistic Regression (Champion): CV F1-Macro: 0.8671 | CV Accuracy: 0.8892 | CV Recall: 0.8597\n• Decision Tree (with ADASYN): CV F1-Macro: 0.7799 | CV Accuracy: 0.8092 | CV Recall: 0.7856\n• Random Forest (Baseline): CV F1-Macro: 0.8094 | CV Accuracy: 0.8392 | CV Recall: 0.7993"),
            ("Unbiased Test Set Evaluation (300 Untouched Samples):", "• Test Accuracy: 86.33% | Test F1-Macro: 0.8344\n• Macro Precision: 0.8468 | Macro Recall: 0.8236 | Test ROC-AUC: 0.9680"),
            ("Class-Wise Breakdown on Test Set:", "• LOW Risk: Precision = 90.61%, Recall = 94.25%, F1 = 92.39%\n• MEDIUM Risk: Precision = 75.64%, Recall = 72.84%, F1 = 74.21%\n• HIGH Risk: Precision = 87.80%, Recall = 80.00%, F1 = 83.72%"),
            ("Discussion & Insights:", "Logistic Regression demonstrated superior generalization on normalized ratio space while guaranteeing linear coefficient monotonicity required by financial audit regulations.")
        ]
    },
    16: {
        "title": "Project Plan & Contributions",
        "bullets": [
            ("Milestones Completed:", "• Phase 1: Problem formulation, synthetic data generator, and literature review [Completed]\n• Phase 2: Feature engineering, pipeline construction, and CV benchmarking [Completed]\n• Phase 3: SHAP explainability engine, Financial Health Index, and What-If simulator [Completed]\n• Phase 4: Streamlit UI/UX redesign, SQLite persistence, and ReportLab PDF engine [Completed]\n• Phase 5: Automated PyTest suite verification and academic documentation [Completed]"),
            ("Technical Challenges Overcome:", "• Prevented data leakage by embedding SMOTE/ADASYN resampling strictly inside cross-validation loops.\n• Solved dark-mode text disappearance via theme-adaptive CSS variables and transparent Plotly canvases.\n• Built zero-retraining scenario simulation for instantaneous real-time user feedback."),
            ("Demonstration Readiness:", "Fully functional web application running locally with a one-click macOS desktop launcher.")
        ]
    },
    17: {
        "title": "Conclusion",
        "bullets": [
            ("Project Summary:", "Successfully designed, developed, and evaluated an academically defensible, explainable AI-based credit risk decision-support platform tailored for MSMEs."),
            ("Key Achievements:", "• Attained 86.33% test accuracy, 0.8344 F1-Macro, and 0.9680 ROC-AUC with zero data leakage.\n• Operationalized the PREDICT -> EXPLAIN -> SIMULATE -> IMPROVE paradigm in a cohesive web dashboard.\n• Delivered local and global model interpretability using Game-Theoretic SHAP values.\n• Formulated an independent 0–100 Financial Health Index across 5 operational pillars.\n• Built real-time What-If scenario modeling and institutional PDF audit report export."),
            ("Core Value Delivered:", "Demonstrated that explainable machine learning can eliminate information asymmetry in small business lending while upholding regulatory transparency standards.")
        ]
    },
    18: {
        "title": "Limitations & Future Scope",
        "bullets": [
            ("Current Project Limitations:", "• Evaluated on synthetic financial data modeled after MSME distributions due to strict banking data confidentiality.\n• Processes static annual/monthly figures; does not currently ingest real-time continuous transaction streams."),
            ("Future Scope & Enhancements:", "• Open Banking & Account Aggregator (AA) Integration: Direct API integration with GSTN and banking aggregators for real-time transaction fetching.\n• OCR Financial Document Parser: Computer vision pipeline to parse scanned PDF balance sheets and tax returns automatically.\n• Concept Drift & Model Monitoring: Integration of Evidently AI to monitor feature drift across shifting macroeconomic cycles.\n• Multi-Language Regional Support: Localizing the UI into regional Indian languages to empower rural MSME borrowers.")
        ]
    },
    19: {
        "title": "References",
        "bullets": [
            ("[1] Bussmann et al. (2021):", "'Explainable Machine Learning in Credit Risk Management', Computational Economics, vol. 57, no. 1, pp. 203–216."),
            ("[2] Chawla et al. (2002):", "'SMOTE: Synthetic Minority Over-sampling Technique', Journal of Artificial Intelligence Research, vol. 16, pp. 321–357."),
            ("[3] Ciampi et al. (2020):", "'SME default prediction with machine learning: A survey and future research directions', European Journal of Operational Research."),
            ("[4] Lundberg & Lee (2017):", "'A unified approach to interpreting model predictions', in Advances in Neural Information Processing Systems (NeurIPS), pp. 4765–4774."),
            ("[5] Reserve Bank of India (RBI):", "'Report of the Expert Committee on Micro, Small and Medium Enterprises', RBI Guidelines on Priority Sector Lending, Mumbai, India, 2019.")
        ]
    },
    20: {
        "title": "Questions & Answers",
        "bullets": [
            ("AI-Based MSME Credit Risk Assistant", "Thank you for your valuable time and consideration!"),
            ("Floor Open for Discussion:", "We welcome your questions, feedback, and demonstration requests."),
            ("Prepared Viva Voce Defense Topics:", "• Methodology for eliminating data leakage during SMOTE/ADASYN resampling.\n• Theoretical foundations of Shapley Additive exPlanations (SHAP) vs. LIME.\n• Justification of Logistic Regression over Random Forest based on CV F1 and coefficient interpretability.\n• Deterministic formulation of the 5-Pillar Financial Health Index (0–100).\n• Counterfactual What-If simulation mechanics without model retraining.")
        ]
    },
    21: {
        "title": "Before Submission: Quick Checklist",
        "bullets": [
            ("Departmental Alignment Check:", "Bharati Vidyapeeth College of Engineering, Pune guidelines strictly adhered to."),
            ("Title & Author Details:", "Project title, student credentials, guide designation, and academic year verified."),
            ("Problem & Outcomes Mapping:", "All stated project objectives directly mapped to implemented and tested software modules."),
            ("Empirical Rigor:", "All performance numbers (86.33% Accuracy, 0.8344 F1, 0.9680 ROC-AUC) derived from actual evaluated models (`model_metadata.json`)."),
            ("Zero Data Leakage:", "Preprocessing ColumnTransformer and SMOTE/ADASYN verified strictly inside training folds."),
            ("Formatting & Citations:", "Consistent 16:9 widescreen layout, clean typography, and IEEE-compliant bibliographical citations.")
        ]
    }
}

# Update slides 2 to 21
for slide_num, data in slide_content.items():
    slide = prs.slides[slide_num - 1]
    
    # Update title
    for shp in slide.shapes:
        if shp.name == 'TextBox 2':
            shp.text_frame.clear()
            p = shp.text_frame.paragraphs[0]
            format_paragraph(p, data["title"], font_size=Pt(22), bold=True, color=RGBColor(26, 54, 93), space_after=Pt(0))
        elif shp.name == 'TextBox 7': # clear prompt footer
            shp.text_frame.clear()
            # Leave blank or set a clean presentation tag
            p = shp.text_frame.paragraphs[0]
            format_paragraph(p, "BVDU College of Engineering, Pune | Department of Computer Engineering", font_size=Pt(9), bold=False, color=RGBColor(148, 163, 184), space_after=Pt(0))
        elif shp.name == 'TextBox 6': # Main Content
            tf = shp.text_frame
            tf.clear()
            for b_idx, bullet in enumerate(data["bullets"]):
                p = tf.paragraphs[0] if b_idx == 0 else tf.add_paragraph()
                if isinstance(bullet, tuple):
                    heading, text = bullet
                    # Add bold heading
                    p.text = "•  " + heading + " "
                    p.font.name = 'Arial'
                    p.font.size = Pt(13) if len(data["bullets"]) > 6 else Pt(14)
                    p.font.bold = True
                    p.font.color.rgb = RGBColor(30, 41, 59)
                    p.space_after = Pt(4) if len(data["bullets"]) > 6 else Pt(6)
                    # Add description run
                    run = p.add_run()
                    run.text = text
                    run.font.name = 'Arial'
                    run.font.size = Pt(13) if len(data["bullets"]) > 6 else Pt(14)
                    run.font.bold = False
                    run.font.color.rgb = RGBColor(71, 85, 105)
                else:
                    p.text = "•  " + str(bullet)
                    p.font.name = 'Arial'
                    p.font.size = Pt(13) if len(data["bullets"]) > 6 else Pt(14)
                    p.font.bold = False
                    p.font.color.rgb = RGBColor(51, 65, 85)
                    p.space_after = Pt(4) if len(data["bullets"]) > 6 else Pt(6)

# Save to project folder and Desktop
prs.save(OUTPUT_PROJECT)
prs.save(OUTPUT_DESKTOP)
print(f"Presentation successfully created and saved to:\n1. {OUTPUT_PROJECT}\n2. {OUTPUT_DESKTOP}")
