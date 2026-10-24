import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

TEMPLATE_PATH = '/Users/avinashsharma/.gemini/antigravity/brain/b298ac1f-7377-49f3-aa32-b17f7ce447fb/.user_uploaded/media_1792495787257_abbc31cd.pptx'
OUTPUT_PROJECT = '/Users/avinashsharma/msme_credit_risk_assistant/MSME_Credit_Risk_Assistant_Presentation.pptx'
OUTPUT_DESKTOP = '/Users/avinashsharma/Desktop/MSME_Credit_Risk_Assistant_Presentation.pptx'
IMG_DIR = '/Users/avinashsharma/msme_credit_risk_assistant/assets/diagrams'

prs = pptx.Presentation(TEMPLATE_PATH)

def format_paragraph(p, text, font_size=Pt(14), bold=False, color=RGBColor(30, 41, 59), space_after=Pt(6), level=0):
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
# SLIDES DATA & DIAGRAM MAPPING
# ==========================================
slide_content = {
    2: {
        "title": "Presentation Roadmap",
        "diagram": None,
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
        "diagram": None,
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
        "diagram": None,
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
        "diagram": None,
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
        "diagram": None,
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
        "diagram": None,
        "bullets": [
            ("Current Industrial Workflow:", "Manual credit underwriting reliant on physical visits, audited balance sheets, subjective discretion, and rigid credit bureau cutoffs (weeks of latency)."),
            ("Key Limitations of Existing Systems:", "Subjective bias, extreme vulnerability to class imbalance, static risk assessment, and zero transparency regarding why an applicant was rejected."),
            ("Identified Research Gap:", "Academic literature treats predictive classification, imbalance handling, and SHAP explainability in theoretical silos; no unified system bridges prediction with counterfactual simulation and automated client reporting in an MSME context."),
            ("How This Project Addresses the Gap:", "Implements the closed-loop PREDICT -> EXPLAIN -> SIMULATE -> IMPROVE paradigm in an interactive, audit-ready software application.")
        ]
    },
    8: {
        "title": "Proposed System",
        "diagram": f"{IMG_DIR}/diag1_proposed_paradigm.png",
        "bullets": [
            ("Architectural Paradigm:", "Executes a closed-loop framework: PREDICT -> EXPLAIN -> SIMULATE -> IMPROVE."),
            ("PREDICT Module:", "Classifies MSMEs into LOW, MEDIUM, or HIGH risk tiers with calibrated probabilities."),
            ("EXPLAIN (SHAP XAI):", "Local and global Shapley attribution decomposing predictions into risk-increasing vs risk-decreasing drivers."),
            ("SIMULATE (What-If Engine):", "Real-time slider simulation showing how revenue or debt modifications alter credit classification."),
            ("IMPROVE (Financial Health):", "Deterministic 5-pillar 0-100 score with actionable turnaround advisory guidance.")
        ]
    },
    9: {
        "title": "System Architecture / Block Diagram",
        "diagram": f"{IMG_DIR}/diag2_architecture.png",
        "bullets": [
            ("Presentation Layer:", "Streamlit UI with dark/light mode, Plotly semi-circular gauges, 5-pillar radar charts, and sliders."),
            ("Inference & Ratio Pipeline:", "Zero-leakage ColumnTransformer (StandardScaler + SimpleImputer) and financial ratio calculations."),
            ("ML & Explainability Layer:", "Champion Logistic Regression classifier (`model.pkl`), SHAP Linear/Tree Explainers, and scenario calculator."),
            ("Storage & Audit Layer:", "SQLite 3 database with 3NF relational schema and ReportLab automated institutional PDF generator.")
        ]
    },
    10: {
        "title": "Methodology / Workflow",
        "diagram": f"{IMG_DIR}/diag3_methodology.png",
        "bullets": [
            ("Data Synthesis & Ingestion:", "1,500 MSME records modeled on log-normal revenue, expenses, debt, and operational noise."),
            ("Financial Ratio Engineering:", "Extracted DTI, Profit Margin, Loan-to-Income, Cash Flow Coverage with zero-division safeguards."),
            ("Stratified 80/20 Train-Test Split:", "Strict isolation (N_train=1,200, N_test=300); preprocessing fitted strictly on training data."),
            ("Resampling inside 5-Fold CV:", "Evaluated None vs SMOTE vs ADASYN inside each fold with zero validation leakage."),
            ("Champion Model Selection:", "Selected Logistic Regression based on CV F1-Macro (0.8671) and linear monotonicity.")
        ]
    },
    11: {
        "title": "Technology Stack & Tools",
        "diagram": None,
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
        "diagram": f"{IMG_DIR}/diag4_er_schema.png",
        "bullets": [
            ("Relational 3NF Schema:", "• 'businesses': Master entity holding business_id PK, name, age, employees.\n• 'financial_data': 1:M child table holding 11 financial metrics & credit history.\n• 'predictions': 1:M audit table storing category, 3-class probabilities, health score & raw JSON."),
            ("Referential Integrity:", "Foreign keys enforce strict parent-child cascading relationships with zero orphaned records."),
            ("Security & Audit Guarantee:", "Parameterized SQL queries block SQL injection; raw JSON snapshots enable exact retrospective replay.")
        ]
    },
    13: {
        "title": "Implementation",
        "diagram": None,
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
        "diagram": None,
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
        "diagram": f"{IMG_DIR}/diag5_results_visual.png",
        "bullets": [
            ("Model Benchmarking (5-Fold CV):", "• Logistic Regression (Champion): CV F1 0.8671, Acc 88.92%\n• Decision Tree (ADASYN): CV F1 0.7799, Acc 80.92%\n• Random Forest: CV F1 0.8094, Acc 83.92%"),
            ("Unbiased Test Set Evaluation (N=300):", "• Test Accuracy: 86.33% | Test F1-Macro: 0.8344\n• Macro Precision: 0.8468 | Macro Recall: 0.8236 | ROC-AUC: 0.9680"),
            ("Class-Wise Performance:", "• LOW Risk: Precision = 90.6%, Recall = 94.3%, F1 = 0.924\n• MEDIUM Risk: Precision = 75.6%, Recall = 72.8%, F1 = 0.742\n• HIGH Risk: Precision = 87.8%, Recall = 80.0%, F1 = 0.837"),
            ("Theoretical Finding:", "Normalized ratio features linearize well under Logistic Regression, providing superior generalization and monotonic SHAP interpretability.")
        ]
    },
    16: {
        "title": "Project Plan & Contributions",
        "diagram": None,
        "bullets": [
            ("Milestones Completed:", "• Phase 1: Problem formulation, synthetic data generator, and literature review [Completed]\n• Phase 2: Feature engineering, pipeline construction, and CV benchmarking [Completed]\n• Phase 3: SHAP explainability engine, Financial Health Index, and What-If simulator [Completed]\n• Phase 4: Streamlit UI/UX redesign, SQLite persistence, and ReportLab PDF engine [Completed]\n• Phase 5: Automated PyTest suite verification and academic documentation [Completed]"),
            ("Technical Challenges Overcome:", "• Prevented data leakage by embedding SMOTE/ADASYN resampling strictly inside cross-validation loops.\n• Solved dark-mode text disappearance via theme-adaptive CSS variables and transparent Plotly canvases.\n• Built zero-retraining scenario simulation for instantaneous real-time user feedback."),
            ("Demonstration Readiness:", "Fully functional web application running locally with a one-click macOS desktop launcher.")
        ]
    },
    17: {
        "title": "Conclusion",
        "diagram": None,
        "bullets": [
            ("Project Summary:", "Successfully designed, developed, and evaluated an academically defensible, explainable AI-based credit risk decision-support platform tailored for MSMEs."),
            ("Key Achievements:", "• Attained 86.33% test accuracy, 0.8344 F1-Macro, and 0.9680 ROC-AUC with zero data leakage.\n• Operationalized the PREDICT -> EXPLAIN -> SIMULATE -> IMPROVE paradigm in a cohesive web dashboard.\n• Delivered local and global model interpretability using Game-Theoretic SHAP values.\n• Formulated an independent 0–100 Financial Health Index across 5 operational pillars.\n• Built real-time What-If scenario modeling and institutional PDF audit report export."),
            ("Core Value Delivered:", "Demonstrated that explainable machine learning can eliminate information asymmetry in small business lending while upholding regulatory transparency standards.")
        ]
    },
    18: {
        "title": "Limitations & Future Scope",
        "diagram": None,
        "bullets": [
            ("Current Project Limitations:", "• Evaluated on synthetic financial data modeled after MSME distributions due to strict banking data confidentiality.\n• Processes static annual/monthly figures; does not currently ingest real-time continuous transaction streams."),
            ("Future Scope & Enhancements:", "• Open Banking & Account Aggregator (AA) Integration: Direct API integration with GSTN and banking aggregators for real-time transaction fetching.\n• OCR Financial Document Parser: Computer vision pipeline to parse scanned PDF balance sheets and tax returns automatically.\n• Concept Drift & Model Monitoring: Integration of Evidently AI to monitor feature drift across shifting macroeconomic cycles.\n• Multi-Language Regional Support: Localizing the UI into regional Indian languages to empower rural MSME borrowers.")
        ]
    },
    19: {
        "title": "References",
        "diagram": None,
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
        "diagram": None,
        "bullets": [
            ("AI-Based MSME Credit Risk Assistant", "Thank you for your valuable time and consideration!"),
            ("Floor Open for Discussion:", "We welcome your questions, feedback, and demonstration requests."),
            ("Prepared Viva Voce Defense Topics:", "• Methodology for eliminating data leakage during SMOTE/ADASYN resampling.\n• Theoretical foundations of Shapley Additive exPlanations (SHAP) vs. LIME.\n• Justification of Logistic Regression over Random Forest based on CV F1 and coefficient interpretability.\n• Deterministic formulation of the 5-Pillar Financial Health Index (0–100).\n• Counterfactual What-If simulation mechanics without model retraining.")
        ]
    },
    21: {
        "title": "Before Submission: Quick Checklist",
        "diagram": None,
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

# ==========================================
# POPULATE SLIDES & EMBED DIAGRAMS
# ==========================================
for slide_num, data in slide_content.items():
    slide = prs.slides[slide_num - 1]
    has_diagram = data["diagram"] is not None and os.path.exists(data["diagram"])
    
    # Update title and footer
    for shp in slide.shapes:
        if shp.name == 'TextBox 2':
            shp.text_frame.clear()
            p = shp.text_frame.paragraphs[0]
            format_paragraph(p, data["title"], font_size=Pt(22), bold=True, color=RGBColor(26, 54, 93), space_after=Pt(0))
        elif shp.name == 'TextBox 7': # clear prompt footer
            shp.text_frame.clear()
            p = shp.text_frame.paragraphs[0]
            format_paragraph(p, "BVDU College of Engineering, Pune | Department of Computer Engineering", font_size=Pt(9), bold=False, color=RGBColor(148, 163, 184), space_after=Pt(0))
        elif shp.name == 'TextBox 6': # Main Content
            # Adjust width if diagram exists
            if has_diagram:
                shp.left = 822960
                shp.width = 5200000 # ~5.7 inches
                shp.top = 1325880
                shp.height = 4754880
            else:
                shp.left = 822960
                shp.width = 10515600 # full width
                shp.top = 1325880
                shp.height = 4754880
                
            tf = shp.text_frame
            tf.clear()
            for b_idx, bullet in enumerate(data["bullets"]):
                p = tf.paragraphs[0] if b_idx == 0 else tf.add_paragraph()
                font_sz = Pt(12) if has_diagram else (Pt(13) if len(data["bullets"]) > 6 else Pt(14))
                sp_after = Pt(3) if has_diagram else (Pt(4) if len(data["bullets"]) > 6 else Pt(6))
                
                if isinstance(bullet, tuple):
                    heading, text = bullet
                    p.text = "•  " + heading + " "
                    p.font.name = 'Arial'
                    p.font.size = font_sz
                    p.font.bold = True
                    p.font.color.rgb = RGBColor(30, 41, 59)
                    p.space_after = sp_after
                    run = p.add_run()
                    run.text = text
                    run.font.name = 'Arial'
                    run.font.size = font_sz
                    run.font.bold = False
                    run.font.color.rgb = RGBColor(71, 85, 105)
                else:
                    p.text = "•  " + str(bullet)
                    p.font.name = 'Arial'
                    p.font.size = font_sz
                    p.font.bold = False
                    p.font.color.rgb = RGBColor(51, 65, 85)
                    p.space_after = sp_after

    # Insert Diagram Picture if applicable
    if has_diagram:
        pic_left = 6200000 # ~6.8 inches
        pic_top = 1350000  # ~1.48 inches
        pic_width = 5300000 # ~5.8 inches
        pic_height = 4700000 # ~5.1 inches
        slide.shapes.add_picture(data["diagram"], pic_left, pic_top, width=pic_width, height=pic_height)
        print(f"Added diagram picture on Slide {slide_num}: {data['diagram']}")

# Save to project folder and Desktop
prs.save(OUTPUT_PROJECT)
prs.save(OUTPUT_DESKTOP)
print(f"Presentation with diagrams successfully saved to:\n1. {OUTPUT_PROJECT}\n2. {OUTPUT_DESKTOP}")
