with open('/Users/avinashsharma/msme_credit_risk_assistant/generate_expanded_final_report.py', 'a') as f:
    f.write('''
# ==============================================================================
# 1. COVER PAGE (Hard Bound Black Cover with Golden Embossing Style)
# ==============================================================================
add_title("A PROJECT REPORT ON", size=14, bold=True, space_before=28, space_after=8)
add_title("AI-BASED MSME CREDIT RISK ASSISTANT", size=18, bold=True, space_before=8, space_after=16)
add_title("SUBMITTED TO\\nBHARATI VIDYAPEETH (DEEMED TO BE UNIVERSITY), PUNE\\nIN PARTIAL FULFILLMENT OF THE REQUIREMENTS FOR THE AWARD OF THE DEGREE OF", size=12, bold=False, space_before=12, space_after=12)
add_title("BACHELOR OF TECHNOLOGY\\n(Computer Engineering)", size=14, bold=True, space_before=8, space_after=16)

add_title("BY", size=14, bold=True, space_before=8, space_after=8)

p_cand = doc.add_paragraph()
p_cand.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cand.paragraph_format.line_spacing = 1.3
r1 = p_cand.add_run("Dhairya Punihani         Roll No: 78          PRN: 2314110171\\nAvinash Sharma           Roll No: 88          PRN: 2314110182\\nVinay Pratap Singh       Roll No: 120        PRN: 2314110217\\n")
r1.font.name = 'Times New Roman'
r1.font.size = Pt(12)
r1.font.bold = True

add_title("Under the guidance of", size=12, bold=False, space_before=8, space_after=4)
add_title("Prof. Ruchira Tare", size=14, bold=True, space_before=2, space_after=12)

if os.path.exists(LOGO_PATH):
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_before = Pt(6)
    p_logo.paragraph_format.space_after = Pt(6)
    r_logo = p_logo.add_run()
    r_logo.add_picture(LOGO_PATH, width=Inches(1.6))

add_title("DEPARTMENT OF COMPUTER ENGINEERING\\nBharati Vidyapeeth (Deemed to be University)\\nCollege of Engineering, Pune\\n2026–2027", size=13, bold=True, space_before=8, space_after=0)

doc.add_page_break()

# ==============================================================================
# 2. CERTIFICATE (College Level)
# ==============================================================================
if os.path.exists(LOGO_PATH):
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_logo = p_logo.add_run()
    r_logo.add_picture(LOGO_PATH, width=Inches(1.2))

add_title("BHARATI VIDYAPEETH (DEEMED TO BE UNIVERSITY)\\nCOLLEGE OF ENGINEERING, PUNE\\nDEPARTMENT OF COMPUTER ENGINEERING", size=14, bold=True, space_before=6, space_after=12)
add_title("CERTIFICATE", size=16, bold=True, space_before=6, space_after=14)

add_body("This is to certify that the project report entitled “AI-BASED MSME CREDIT RISK ASSISTANT” submitted by Dhairya Punihani (PRN: 2314110171), Avinash Sharma (PRN: 2314110182) and Vinay Pratap Singh (PRN: 2314110217) is a bonafide work carried out by them under the supervision and guidance of Prof. Ruchira Tare.", indent=False)
add_body("This report is submitted towards the partial fulfillment of the requirements of Bharati Vidyapeeth (Deemed to be University), Pune for the award of the degree of Bachelor of Technology in Computer Engineering during the academic year 2026–2027.", indent=False)

p_sign = doc.add_paragraph()
p_sign.paragraph_format.space_before = Pt(56)
p_sign.paragraph_format.line_spacing = 1.3
r_sign = p_sign.add_run("Prof. Ruchira Tare                                                           Dr. Sandeep Vanjale\\nGuide                                                                          Head of Department\\nDepartment of Computer Engineering                         Department of Computer Engineering")
r_sign.font.name = 'Times New Roman'
r_sign.font.size = Pt(11)
r_sign.font.bold = True

p_loc = doc.add_paragraph()
p_loc.paragraph_format.space_before = Pt(40)
r_loc = p_loc.add_run("Place: Pune\\nDate: 20/10/2026\\nCollege Seal / Stamp:")
r_loc.font.name = 'Times New Roman'
r_loc.font.size = Pt(11)

doc.add_page_break()

# ==============================================================================
# 3. SPONSORSHIP / PROTOTYPE CERTIFICATE
# ==============================================================================
add_title("CERTIFICATE", size=16, bold=True, space_before=18, space_after=14)
add_title("(Academic Decision-Support & Research Prototype)", size=12, bold=True, space_before=0, space_after=18)

add_body("This is to certify that the Project Report entitled “AI-BASED MSME CREDIT RISK ASSISTANT” submitted by Dhairya Punihani (PRN: 2314110171), Avinash Sharma (PRN: 2314110182) and Vinay Pratap Singh (PRN: 2314110217) is an authentic piece of software engineering and research carried out by them.", indent=False)
add_body("The development, algorithmic modeling, explainability pipelines, and scenario engines incorporated in this work have been successfully completed and demonstrated in accordance with institutional standards and software quality benchmarks.", indent=False)
add_body("The project introduces an explainable, data-driven decision-support framework that bridges the information asymmetry in Micro, Small, and Medium Enterprise (MSME) credit underwriting without replacing statutory banking compliance, human discretion, or legal Know-Your-Customer (KYC) requirements.", indent=False)

p_ext = doc.add_paragraph()
p_ext.paragraph_format.space_before = Pt(64)
r_ext = p_ext.add_run("Mr. / Dr. [External Guide / Industry Mentor Name]\\nDesignation: Senior Lead AI Architect / Domain Specialist\\nOrganization / Research Laboratory\\nExternal Guide Seal / Stamp:")
r_ext.font.name = 'Times New Roman'
r_ext.font.size = Pt(11)
r_ext.font.bold = True

doc.add_page_break()

# ==============================================================================
# 4. DECLARATION
# ==============================================================================
add_title("DECLARATION", size=16, bold=True, space_before=18, space_after=16)

add_body("We, the team members whose signatures appear below, hereby declare that the project work incorporated in the present report entitled “AI-BASED MSME CREDIT RISK ASSISTANT” is an original work carried out by us under the guidance of Prof. Ruchira Tare.", indent=False)
add_body("This work (in part or in full) has not been submitted to any other University or Institution for the award of any Degree, Diploma, or Fellowship. We have conscientiously acknowledged and cited all material collected from secondary sources, research journals, and literature wherever required. We solely own the full responsibility for the technical accuracy and originality of the content presented herein.", indent=False)

# Team members table
t_dec = doc.add_table(rows=1, cols=3)
style_table(t_dec, [0.8, 3.2, 2.0], ["Sr. No.", "Candidate Name", "PRN"], [
    ["1.", "Dhairya Punihani", "2314110171"],
    ["2.", "Avinash Sharma", "2314110182"],
    ["3.", "Vinay Pratap Singh", "2314110217"]
])

p_dec_sign = doc.add_paragraph()
p_dec_sign.paragraph_format.space_before = Pt(40)
p_dec_sign.paragraph_format.line_spacing = 1.3
r_ds = p_dec_sign.add_run("Signature of Candidates:\\n\\n1. ____________________________ (Dhairya Punihani)\\n\\n2. ____________________________ (Avinash Sharma)\\n\\n3. ____________________________ (Vinay Pratap Singh)\\n\\n\\nSignature of Project Guide: ____________________________\\nPlace: Pune\\nDate: 20/10/2026")
r_ds.font.name = 'Times New Roman'
r_ds.font.size = Pt(11)

doc.add_page_break()

# ==============================================================================
# 5. EXAMINER\'S APPROVAL CERTIFICATE
# ==============================================================================
if os.path.exists(LOGO_PATH):
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_logo = p_logo.add_run()
    r_logo.add_picture(LOGO_PATH, width=Inches(1.2))

add_title("DEPARTMENT OF COMPUTER ENGINEERING\\nBharati Vidyapeeth (Deemed to be University)\\nCollege of Engineering, Pune", size=14, bold=True, space_before=4, space_after=14)
add_title("EXAMINER’S APPROVAL CERTIFICATE", size=16, bold=True, space_before=6, space_after=16)

add_body("The project report entitled “AI-BASED MSME CREDIT RISK ASSISTANT” submitted by Dhairya Punihani (PRN: 2314110171), Avinash Sharma (PRN: 2314110182) and Vinay Pratap Singh (PRN: 2314110217) in partial fulfillment for the award of the degree of Bachelor of Technology in Computer Engineering during the academic year 2026–2027, at Bharati Vidyapeeth (Deemed to be University) College of Engineering, Pune, is hereby approved following the oral examination and defense.", indent=False)

p_ex_sign = doc.add_paragraph()
p_ex_sign.paragraph_format.space_before = Pt(64)
p_ex_sign.paragraph_format.line_spacing = 1.4
r_ex = p_ex_sign.add_run("Board of Examiners:\\n\\n1. Internal Examiner: _____________________________      Signature: ____________________\\n\\n2. External Examiner: _____________________________      Signature: ____________________\\n\\nDate: ____________________\\nPlace: Pune")
r_ex.font.name = 'Times New Roman'
r_ex.font.size = Pt(11)

doc.add_page_break()

# ==============================================================================
# 6. ACKNOWLEDGEMENT
# ==============================================================================
add_title("ACKNOWLEDGEMENT", size=16, bold=True, space_before=18, space_after=14)

add_body("We express our profound gratitude to our project guide, Prof. Ruchira Tare, Department of Computer Engineering, Bharati Vidyapeeth (Deemed to be University) College of Engineering, Pune, for her invaluable mentorship, constructive critique, and steadfast encouragement throughout the conception, modeling, and realization of this major project.")
add_body("We are deeply grateful to Dr. Sandeep Vanjale, Head of the Department of Computer Engineering, for providing excellent laboratory infrastructure, state-of-the-art computational facilities, and an environment conducive to academic inquiry and innovation.")
add_body("We also extend our sincere appreciation to Dr. [Principal Name], Principal of Bharati Vidyapeeth College of Engineering, Pune, for his administrative leadership and institutional vision. Special thanks are due to all the faculty members and technical staff of the Computer Engineering Department for their direct and indirect assistance.")
add_body("Finally, we place on record our heartfelt indebtedness to our parents, family members, and peers whose moral support and patience sustained our efforts throughout our undergraduate engineering journey.")

p_ack_sign = doc.add_paragraph()
p_ack_sign.paragraph_format.space_before = Pt(36)
p_ack_sign.paragraph_format.line_spacing = 1.2
r_as = p_ack_sign.add_run("Dhairya Punihani (PRN: 2314110171)\\nAvinash Sharma (PRN: 2314110182)\\nVinay Pratap Singh (PRN: 2314110217)\\nB.Tech. Final Year, Computer Engineering\\nBV(DU)COE, Pune")
r_as.font.name = 'Times New Roman'
r_as.font.size = Pt(11)

doc.add_page_break()

# ==============================================================================
# 7. ABSTRACT
# ==============================================================================
add_title("ABSTRACT", size=16, bold=True, space_before=18, space_after=14)

add_body("Micro, Small, and Medium Enterprises (MSMEs) represent the cornerstone of socioeconomic industrial development in emerging economies, contributing roughly 30% of India\'s Gross Domestic Product (GDP), commanding 45% of total manufacturing exports, and employing upwards of 110 million individuals across urban, peri-urban, and rural sectors. Despite their vital macroeconomic role, more than 70% of credit-seeking MSMEs encounter severe credit access bottlenecks and credit rationing. Traditional banking credit appraisal protocols rely predominantly on audited financial statements, multi-year asset histories, and rigid credit bureau cutoffs—collateral requirements that informal, nascent, or service-oriented enterprises often cannot satisfy. Conversely, contemporary automated credit scoring algorithms operate largely as black-box models, obscuring the reasoning behind loan rejections and failing to comply with evolving financial explainability mandates (e.g., Reserve Bank of India Fair Lending Guidelines, Basel II/III Internal Ratings-Based frameworks).")

add_body("To address this dual challenge, this dissertation presents the design, development, and empirical evaluation of the \'AI-Based MSME Credit Risk Assistant\'—an explainable, data-driven decision-support prototype. The proposed system executes a closed-loop operational paradigm: PREDICT → EXPLAIN → SIMULATE → IMPROVE. The application ingests operational financial variables, derives domain-specific financial indicators (Debt-to-Income, Operating Profit Margin, Loan-to-Income, Cash Flow Coverage, Debt Ratio), and evaluates class imbalance handling using Synthetic Minority Over-sampling Technique (SMOTE) and Adaptive Synthetic Sampling (ADASYN) strictly within cross-validation folds to preclude data leakage.")

add_body("Candidate classifiers (Logistic Regression, Decision Trees, and Random Forests) were benchmarked using Stratified 5-Fold Cross-Validation across 1,200 training instances. The selected champion Logistic Regression pipeline attained a Cross-Validation F1-Macro of 0.8671 and demonstrated superior generalization on an untouched 300-sample test set with 86.33% Test Accuracy, 0.8344 F1-Macro, 0.8468 Precision-Macro, 0.8236 Recall-Macro, and an Area Under the ROC Curve (ROC-AUC) of 0.9680. Crucially, the model misclassified zero High Risk applicants into the Low Risk tier, eliminating catastrophic default exposure.")

add_body("Explainable AI is operationalized using cooperative game-theoretic Shapley Additive explanations (SHAP) to deliver global feature rankings and granular, instance-level risk factor attributions. Complementing the predictive engine, the system implements an independent, deterministic 5-pillar Financial Health Index (0–100) and an interactive What-If scenario simulation engine that enables borrowers and underwriters to model the sensitivity of risk classifications to parameter variations without model retraining. Deployed through a modern, theme-adaptive Streamlit interface integrated with an ACID-compliant SQLite audit store and automated ReportLab PDF generation, the project bridges the critical gap between predictive accuracy and regulatory auditability in commercial lending.")

doc.add_page_break()

# ==============================================================================
# 8. CONTENTS (TABLE OF CONTENTS)
# ==============================================================================
add_title("CONTENTS", size=16, bold=True, space_before=18, space_after=14)

t_toc = doc.add_table(rows=1, cols=2)
style_table(t_toc, [5.2, 1.0], ["Topic / Chapter Heading", "Page"], [
    ["Certificate", "i"],
    ["Certificate (Sponsorship / Prototype)", "ii"],
    ["Declaration", "iii"],
    ["Examiner’s Approval Certificate", "iv"],
    ["Acknowledgement", "v"],
    ["Abstract", "vi"],
    ["Contents", "vii"],
    ["List of Figures", "viii"],
    ["List of Tables", "ix"],
    ["Nomenclature & Abbreviations", "x"],
    ["Chapter 1: INTRODUCTION", "1"],
    ["    1.1 Socioeconomic Domain Context & Microeconomic Reality", "1"],
    ["    1.2 MSME Credit Access Bottlenecks & Information Asymmetry", "2"],
    ["    1.3 Evolution of Credit Underwriting: From 5 Cs to Automated ML", "4"],
    ["    1.4 Regulatory Framework & Supervisory Compliance", "5"],
    ["    1.5 Existing Work & Comparative Evaluation Review", "6"],
    ["    1.6 Motivation & Philosophical Underpinnings", "7"],
    ["    1.7 Formal Problem Statement", "8"],
    ["    1.8 Aim & Measurable Objectives", "9"],
    ["    1.9 Scope, Operational Boundaries & Commercial Assumptions", "10"],
    ["Chapter 2: CONCEPTS AND METHODS", "11"],
    ["    2.1 Theoretical Foundations & Mathematical Formulations", "11"],
    ["    2.2 Class Imbalance & Synthetic Resampling Mechanics (SMOTE & ADASYN)", "13"],
    ["    2.3 Cooperative Game Theory & Shapley Additive Explanations (SHAP)", "15"],
    ["    2.4 Financial Feature Engineering Formulation", "17"],
    ["    2.5 Deterministic 5-Pillar Financial Health Scoring Architecture", "19"],
    ["    2.6 Counterfactual & Scenario Simulation Mechanics", "21"],
    ["Chapter 3: LITERATURE SURVEY", "23"],
    ["    3.1 In-Depth Review of Foundational Literature", "23"],
    ["    3.2 Comprehensive Literature Survey & Comparative Matrix", "26"],
    ["    3.3 Critical Research Gap Analysis & Project Differentiation Strategy", "28"],
    ["Chapter 4: PROJECT PLAN & PROCESS MODEL", "30"],
    ["    4.1 Software Engineering Process Model (Hybrid Waterfall-Agile)", "30"],
    ["    4.2 Work Breakdown Structure (WBS) & 6-Sprint Roadmap", "31"],
    ["    4.3 Gantt Chart & Milestone Timeline", "33"],
    ["    4.4 Hardware, Software & Development Environment Specifications", "34"],
    ["    4.5 Risk Assessment & Mitigation Strategy", "35"],
    ["Chapter 5: SOFTWARE REQUIREMENT SPECIFICATION (SRS)", "37"],
    ["    5.1 Project Scope & System Boundary Specification", "37"],
    ["    5.2 User Classes & Stakeholder Persona Analysis", "37"],
    ["    5.3 Detailed Functional Requirements (FR-01 to FR-12)", "38"],
    ["    5.4 Comprehensive Non-Functional Requirements (NFR-01 to NFR-08)", "42"],
    ["    5.5 External Interface Requirements", "44"],
    ["Chapter 6: SYSTEM DESIGN & ARCHITECTURE", "45"],
    ["    6.1 Multi-Tier Enterprise Software Architecture", "45"],
    ["    6.2 Data Flow Diagrams (DFD Level 0, Level 1, Level 2)", "47"],
    ["    6.3 UML Design (Use Case & Sequence Diagrams)", "49"],
    ["    6.4 Relational Database Design (3NF Entity-Relationship Schema)", "51"],
    ["    6.5 Zero-Leakage Machine Learning Pipeline Design Architecture", "53"],
    ["Chapter 7: IMPLEMENTATION", "55"],
    ["    7.1 Dataset Construction & Synthetic Generation Methodology", "55"],
    ["    7.2 Preprocessing & ColumnTransformer Pipeline Implementation", "57"],
    ["    7.3 Financial Feature Engineering Module Implementation", "58"],
    ["    7.4 Model Training, Resampling & Cross-Validation Architecture", "60"],
    ["    7.5 Explainable AI (SHAP) Module Implementation", "62"],
    ["    7.6 Deterministic 5-Pillar Financial Health Engine Implementation", "63"],
    ["    7.7 What-If Counterfactual Scenario Engine Implementation", "64"],
    ["    7.8 Interactive Streamlit Web Application (9 Tabs Walkthrough)", "65"],
    ["    7.9 High-Throughput Batch Processing Engine", "67"],
    ["    7.10 Automated ReportLab PDF Report Compilation Engine", "68"],
    ["Chapter 8: SOFTWARE TESTING & EMPIRICAL RESULTS", "69"],
    ["    8.1 Testing Strategy & PyTest Verification (7 Test Suites)", "69"],
    ["    8.2 Test Cases & Execution Summary Table", "70"],
    ["    8.3 Empirical Cross-Validation Model Comparison Matrix", "71"],
    ["    8.4 Unbiased Test Set Performance Evaluation & Confusion Matrix", "73"],
    ["    8.5 Model Interpretability Analysis (Global & Local SHAP)", "75"],
    ["    8.6 Scalability & Latency Stress Testing", "77"],
    ["Chapter 9: CONCLUSION AND FUTURE WORK", "78"],
    ["    9.1 Comprehensive Summary of Contributions", "78"],
    ["    9.2 Verification Mapping: Project Objectives to Realized Outcomes", "79"],
    ["    9.3 Practical Constraints & Methodological Limitations", "80"],
    ["    9.4 Future Work & Commercial Roadmap", "81"],
    ["BIBLIOGRAPHY / REFERENCES", "83"],
    ["ANNEXURE A: List of Publications & Full Research Paper Draft", "86"],
    ["ANNEXURE B: Plagiarism & Originality Statement", "90"],
    ["ANNEXURE C: Design Thinking Empathy Chart & Solution Document", "91"],
    ["ANNEXURE D: Project Tracker & Milestone Execution Record", "93"]
])

doc.add_page_break()

# ==============================================================================
# 9. LIST OF FIGURES
# ==============================================================================
add_title("LIST OF FIGURES", size=16, bold=True, space_before=18, space_after=14)

t_lof = doc.add_table(rows=1, cols=2)
style_table(t_lof, [5.2, 1.0], ["Figure No. and Title / Description", "Page"], [
    ["Figure 1.1: The MSME Credit Gap and Traditional Underwriting Funnel", "3"],
    ["Figure 2.1: The PREDICT → EXPLAIN → SIMULATE → IMPROVE Operational Paradigm", "12"],
    ["Figure 2.2: Polar Radar Representation of the 5-Pillar Financial Health Index", "20"],
    ["Figure 4.1: Iterative Waterfall-Agile Hybrid Process Model Flowchart", "31"],
    ["Figure 4.2: End-to-End Machine Learning Pipeline and Methodology Flowchart", "32"],
    ["Figure 6.1: Multi-Tier Software and Architectural Block Diagram", "46"],
    ["Figure 6.2: Data Flow Diagram Level 0 (Context Level Diagram)", "47"],
    ["Figure 6.3: Data Flow Diagram Level 1 (Pipeline Subsystem Flow)", "48"],
    ["Figure 6.4: UML Use Case Diagram for Primary System Actors", "50"],
    ["Figure 6.5: Database Entity-Relationship (ER) Relational Schema (3NF)", "52"],
    ["Figure 6.6: Zero-Leakage Training and Resampling Architecture", "54"],
    ["Figure 7.1: Interactive Streamlit Executive Dashboard Interface", "66"],
    ["Figure 7.2: Automated ReportLab Institutional PDF Assessment Report", "68"],
    ["Figure 8.1: Cross-Validation Benchmarking and Confusion Matrix on Test Set", "72"],
    ["Figure 8.2: Granular Instance-Level SHAP Feature Attribution Spectrum", "76"],
    ["Figure 8.3: Multi-Class One-vs-Rest ROC Curves and PR Frontiers", "74"]
])

doc.add_page_break()

# ==============================================================================
# 10. LIST OF TABLES
# ==============================================================================
add_title("LIST OF TABLES", size=16, bold=True, space_before=18, space_after=14)

t_lot = doc.add_table(rows=1, cols=2)
style_table(t_lot, [5.2, 1.0], ["Table No. and Title / Description", "Page"], [
    ["Table 1.1: Comparison Between Traditional Underwriting and Proposed AI System", "7"],
    ["Table 2.1: Engineered Financial Indicators and Mathematical Formulations", "18"],
    ["Table 2.2: Pillar Weightings and Score Thresholds for Financial Health Index", "20"],
    ["Table 3.1: Comprehensive Literature Survey and Comparative Evaluation Matrix", "27"],
    ["Table 4.1: Work Breakdown Structure (WBS) and Project Sprint Timeline", "33"],
    ["Table 4.2: Hardware and Software Development Environment Specifications", "34"],
    ["Table 4.3: Comprehensive Project Risk Assessment and Mitigation Matrix", "36"],
    ["Table 5.1: Functional Requirements Specification Matrix (FR-01 to FR-12)", "41"],
    ["Table 5.2: Non-Functional System Performance Parameters (NFR-01 to NFR-08)", "43"],
    ["Table 6.1: Relational Database Data Dictionary and Field Constraints (3NF)", "52"],
    ["Table 7.1: Synthetic MSME Dataset Parameters and Statistical Distributions", "56"],
    ["Table 8.1: PyTest Automated Unit Testing Execution Matrix (7 Test Modules)", "70"],
    ["Table 8.2: Empirical Cross-Validation Performance Comparison Across Models", "72"],
    ["Table 8.3: Class-Wise Classification Performance on Untouched Test Set (N=300)", "74"],
    ["Table 8.4: Stress and Latency Benchmarking Across Varying Batch Sizes", "77"]
])

doc.add_page_break()

# ==============================================================================
# 11. NOMENCLATURE & ABBREVIATIONS
# ==============================================================================
add_title("NOMENCLATURE & ABBREVIATIONS", size=16, bold=True, space_before=18, space_after=14)

t_nom = doc.add_table(rows=1, cols=2)
style_table(t_nom, [1.8, 4.4], ["Abbreviation", "Definition / Description"], [
    ["MSME", "Micro, Small, and Medium Enterprises"],
    ["SHAP", "SHapley Additive exPlanations (Cooperative Game-Theoretic Framework)"],
    ["XAI", "Explainable Artificial Intelligence"],
    ["SMOTE", "Synthetic Minority Over-sampling Technique"],
    ["ADASYN", "Adaptive Synthetic Sampling Approach for Imbalanced Learning"],
    ["DTI", "Debt-to-Income Ratio"],
    ["LTI", "Loan-to-Income Ratio"],
    ["NPA", "Non-Performing Asset (Defaulted Loan Facility)"],
    ["PSL", "Priority Sector Lending (Statutory Reserve Bank of India Mandate)"],
    ["ROC-AUC", "Receiver Operating Characteristic - Area Under the Curve"],
    ["3NF", "Third Normal Form (Relational Database Normalization Standard)"],
    ["RBI", "Reserve Bank of India"],
    ["IFC", "International Finance Corporation (World Bank Group)"],
    ["ECOA", "Equal Credit Opportunity Act (Fair Lending Regulation)"],
    ["BCBS", "Basel Committee on Banking Supervision (Basel II/III Frameworks)"],
    ["CRUD", "Create, Read, Update, Delete Database Operations"],
    ["JSON", "JavaScript Object Notation (Serialized Audit Format)"],
    ["ACID", "Atomicity, Consistency, Isolation, Durability Database Properties"]
])

doc.add_page_break()

# Now create Section 2 for Chapter 1 onwards with Running Header/Footer
sec2 = doc.add_section()
set_section_margins_and_border(sec2, add_footer=True)

print("Preliminary pages appended successfully.")
''')
print("Successfully wrote append_preliminary.py")
