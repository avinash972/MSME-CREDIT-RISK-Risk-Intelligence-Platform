# Expanded Project Report Generator for AI-Based MSME Credit Risk Assistant
# Formatted strictly according to Bharati Vidyapeeth (Deemed to be University) Guidelines
# Target Page Count: 60 - 70 Pages
# Includes Page Borders, Comprehensive Chapters, 15 Figures, 14 Tables, and 4 Detailed Annexures

import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

DOCX_PROJECT = '/Users/avinashsharma/msme_credit_risk_assistant/BTech_Project_Report_MSME_Credit_Risk_Assistant.docx'
DOCX_DESKTOP = '/Users/avinashsharma/Desktop/BTech_Project_Report_MSME_Credit_Risk_Assistant.docx'
PDF_PROJECT = '/Users/avinashsharma/msme_credit_risk_assistant/BTech_Project_Report_MSME_Credit_Risk_Assistant.pdf'
PDF_DESKTOP = '/Users/avinashsharma/Desktop/BTech_Project_Report_MSME_Credit_Risk_Assistant.pdf'
LOGO_PATH = '/Users/avinashsharma/msme_credit_risk_assistant/assets/bvdu_logo.png'
DIAG_DIR = '/Users/avinashsharma/msme_credit_risk_assistant/assets/diagrams'

doc = Document()

def set_section_margins_and_border(section, add_footer=True):
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.25)
    section.right_margin = Inches(1.0)
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    
    # Add page border to every section
    sectPr = section._sectPr
    for child in list(sectPr):
        if child.tag.endswith('pgBorders'):
            sectPr.remove(child)
    border_xml = parse_xml(r'''
        <w:pgBorders {} w:offsetFrom="page">
            <w:top w:val="single" w:sz="12" w:space="24" w:color="000000"/>
            <w:left w:val="single" w:sz="12" w:space="24" w:color="000000"/>
            <w:bottom w:val="single" w:sz="12" w:space="24" w:color="000000"/>
            <w:right w:val="single" w:sz="12" w:space="24" w:color="000000"/>
        </w:pgBorders>
    '''.format(nsdecls('w')))
    sectPr.append(border_xml)
    
    if add_footer:
        footer = section.footer
        p_ft = footer.paragraphs[0]
        p_ft.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_ft.text = ""
        r_ft = p_ft.add_run("BV(DU)COE, Department of Computer Engineering 2026–2027")
        r_ft.font.name = 'Times New Roman'
        r_ft.font.size = Pt(10)
        r_ft.font.color.rgb = RGBColor(60, 60, 60)

# Configure Section 1 (Preliminary Pages)
sec1 = doc.sections[0]
set_section_margins_and_border(sec1, add_footer=False)

# Default Style Configuration
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(12)
font.color.rgb = RGBColor(0, 0, 0)
style.paragraph_format.line_spacing = 1.5
style.paragraph_format.space_after = Pt(6)

def add_title(text, size=18, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12, space_before=12):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_heading1(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(22)
    p.paragraph_format.space_after = Pt(14)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text.upper())
    run.font.name = 'Times New Roman'
    run.font.size = Pt(18)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_heading2(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text.upper())
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_heading3(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_body(text, indent=True):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(6)
    if indent:
        p.paragraph_format.first_line_indent = Inches(0.25)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p

def add_bullet(bold_prefix, text):
    p = doc.add_paragraph(style='List Bullet')
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.space_after = Pt(4)
    run_b = p.add_run(bold_prefix + " ")
    run_b.font.name = 'Times New Roman'
    run_b.font.size = Pt(12)
    run_b.font.bold = True
    run_t = p.add_run(text)
    run_t.font.name = 'Times New Roman'
    run_t.font.size = Pt(12)
    return p

def style_table(table, col_widths, headers, data):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        hdr_cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = hdr_cells[i].paragraphs[0].runs[0]
        run.font.name = 'Times New Roman'
        run.font.bold = True
        run.font.size = Pt(10)
        shading = parse_xml(r'<w:shd {} w:fill="E2E8F0"/>'.format(nsdecls('w')))
        hdr_cells[i]._tc.get_or_add_tcPr().append(shading)
        
    for r_idx, row_data in enumerate(data):
        row_cells = table.add_row().cells
        for c_idx, val in enumerate(row_data):
            row_cells[c_idx].text = str(val)
            align = WD_ALIGN_PARAGRAPH.LEFT if c_idx == 0 or len(str(val)) > 20 else WD_ALIGN_PARAGRAPH.CENTER
            row_cells[c_idx].paragraphs[0].alignment = align
            run = row_cells[c_idx].paragraphs[0].runs[0]
            run.font.name = 'Times New Roman'
            run.font.size = Pt(9.5)
            if r_idx % 2 == 1:
                shd = parse_xml(r'<w:shd {} w:fill="F8FAFC"/>'.format(nsdecls('w')))
                row_cells[c_idx]._tc.get_or_add_tcPr().append(shd)

    for row in table.rows:
        for i, w in enumerate(col_widths):
            row.cells[i].width = Inches(w)

def add_figure(img_path, caption, width=5.2):
    if os.path.exists(img_path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run()
        run.add_picture(img_path, width=Inches(width))
        
        cap_p = doc.add_paragraph()
        cap_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap_p.paragraph_format.space_after = Pt(14)
        run_c = cap_p.add_run(caption)
        run_c.font.name = 'Times New Roman'
        run_c.font.size = Pt(10.5)
        run_c.font.bold = True

print("Framework setup completed. Ready to generate report.")

# ==============================================================================
# 1. COVER PAGE (Hard Bound Black Cover with Golden Embossing Style)
# ==============================================================================
add_title("A PROJECT REPORT ON", size=14, bold=True, space_before=28, space_after=8)
add_title("AI-BASED MSME CREDIT RISK ASSISTANT", size=18, bold=True, space_before=8, space_after=16)
add_title("SUBMITTED TO\nBHARATI VIDYAPEETH (DEEMED TO BE UNIVERSITY), PUNE\nIN PARTIAL FULFILLMENT OF THE REQUIREMENTS FOR THE AWARD OF THE DEGREE OF", size=12, bold=False, space_before=12, space_after=12)
add_title("BACHELOR OF TECHNOLOGY\n(Computer Engineering)", size=14, bold=True, space_before=8, space_after=16)

add_title("BY", size=14, bold=True, space_before=8, space_after=8)

p_cand = doc.add_paragraph()
p_cand.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cand.paragraph_format.line_spacing = 1.3
r1 = p_cand.add_run("Dhairya Punihani         Roll No: 78          PRN: 2314110171\nAvinash Sharma           Roll No: 88          PRN: 2314110182\nVinay Pratap Singh       Roll No: 120        PRN: 2314110217\n")
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

add_title("DEPARTMENT OF COMPUTER ENGINEERING\nBharati Vidyapeeth (Deemed to be University)\nCollege of Engineering, Pune\n2026–2027", size=13, bold=True, space_before=8, space_after=0)

doc.add_page_break()

# ==============================================================================
# 2. CERTIFICATE (College Level)
# ==============================================================================
if os.path.exists(LOGO_PATH):
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_logo = p_logo.add_run()
    r_logo.add_picture(LOGO_PATH, width=Inches(1.2))

add_title("BHARATI VIDYAPEETH (DEEMED TO BE UNIVERSITY)\nCOLLEGE OF ENGINEERING, PUNE\nDEPARTMENT OF COMPUTER ENGINEERING", size=14, bold=True, space_before=6, space_after=12)
add_title("CERTIFICATE", size=16, bold=True, space_before=6, space_after=14)

add_body("This is to certify that the project report entitled “AI-BASED MSME CREDIT RISK ASSISTANT” submitted by Dhairya Punihani (PRN: 2314110171), Avinash Sharma (PRN: 2314110182) and Vinay Pratap Singh (PRN: 2314110217) is a bonafide work carried out by them under the supervision and guidance of Prof. Ruchira Tare.", indent=False)
add_body("This report is submitted towards the partial fulfillment of the requirements of Bharati Vidyapeeth (Deemed to be University), Pune for the award of the degree of Bachelor of Technology in Computer Engineering during the academic year 2026–2027.", indent=False)

p_sign = doc.add_paragraph()
p_sign.paragraph_format.space_before = Pt(56)
p_sign.paragraph_format.line_spacing = 1.3
r_sign = p_sign.add_run("Prof. Ruchira Tare                                                           Dr. Sandeep Vanjale\nGuide                                                                          Head of Department\nDepartment of Computer Engineering                         Department of Computer Engineering")
r_sign.font.name = 'Times New Roman'
r_sign.font.size = Pt(11)
r_sign.font.bold = True

p_loc = doc.add_paragraph()
p_loc.paragraph_format.space_before = Pt(40)
r_loc = p_loc.add_run("Place: Pune\nDate: 20/10/2026\nCollege Seal / Stamp:")
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
r_ext = p_ext.add_run("Mr. / Dr. [External Guide / Industry Mentor Name]\nDesignation: Senior Lead AI Architect / Domain Specialist\nOrganization / Research Laboratory\nExternal Guide Seal / Stamp:")
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
r_ds = p_dec_sign.add_run("Signature of Candidates:\n\n1. ____________________________ (Dhairya Punihani)\n\n2. ____________________________ (Avinash Sharma)\n\n3. ____________________________ (Vinay Pratap Singh)\n\n\nSignature of Project Guide: ____________________________\nPlace: Pune\nDate: 20/10/2026")
r_ds.font.name = 'Times New Roman'
r_ds.font.size = Pt(11)

doc.add_page_break()

# ==============================================================================
# 5. EXAMINER'S APPROVAL CERTIFICATE
# ==============================================================================
if os.path.exists(LOGO_PATH):
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_logo = p_logo.add_run()
    r_logo.add_picture(LOGO_PATH, width=Inches(1.2))

add_title("DEPARTMENT OF COMPUTER ENGINEERING\nBharati Vidyapeeth (Deemed to be University)\nCollege of Engineering, Pune", size=14, bold=True, space_before=4, space_after=14)
add_title("EXAMINER’S APPROVAL CERTIFICATE", size=16, bold=True, space_before=6, space_after=16)

add_body("The project report entitled “AI-BASED MSME CREDIT RISK ASSISTANT” submitted by Dhairya Punihani (PRN: 2314110171), Avinash Sharma (PRN: 2314110182) and Vinay Pratap Singh (PRN: 2314110217) in partial fulfillment for the award of the degree of Bachelor of Technology in Computer Engineering during the academic year 2026–2027, at Bharati Vidyapeeth (Deemed to be University) College of Engineering, Pune, is hereby approved following the oral examination and defense.", indent=False)

p_ex_sign = doc.add_paragraph()
p_ex_sign.paragraph_format.space_before = Pt(64)
p_ex_sign.paragraph_format.line_spacing = 1.4
r_ex = p_ex_sign.add_run("Board of Examiners:\n\n1. Internal Examiner: _____________________________      Signature: ____________________\n\n2. External Examiner: _____________________________      Signature: ____________________\n\nDate: ____________________\nPlace: Pune")
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
r_as = p_ack_sign.add_run("Dhairya Punihani (PRN: 2314110171)\nAvinash Sharma (PRN: 2314110182)\nVinay Pratap Singh (PRN: 2314110217)\nB.Tech. Final Year, Computer Engineering\nBV(DU)COE, Pune")
r_as.font.name = 'Times New Roman'
r_as.font.size = Pt(11)

doc.add_page_break()

# ==============================================================================
# 7. ABSTRACT
# ==============================================================================
add_title("ABSTRACT", size=16, bold=True, space_before=18, space_after=14)

add_body("Micro, Small, and Medium Enterprises (MSMEs) represent the cornerstone of socioeconomic industrial development in emerging economies, contributing roughly 30% of India's Gross Domestic Product (GDP), commanding 45% of total manufacturing exports, and employing upwards of 110 million individuals across urban, peri-urban, and rural sectors. Despite their vital macroeconomic role, more than 70% of credit-seeking MSMEs encounter severe credit access bottlenecks and credit rationing. Traditional banking credit appraisal protocols rely predominantly on audited financial statements, multi-year asset histories, and rigid credit bureau cutoffs—collateral requirements that informal, nascent, or service-oriented enterprises often cannot satisfy. Conversely, contemporary automated credit scoring algorithms operate largely as black-box models, obscuring the reasoning behind loan rejections and failing to comply with evolving financial explainability mandates (e.g., Reserve Bank of India Fair Lending Guidelines, Basel II/III Internal Ratings-Based frameworks).")

add_body("To address this dual challenge, this dissertation presents the design, development, and empirical evaluation of the 'AI-Based MSME Credit Risk Assistant'—an explainable, data-driven decision-support prototype. The proposed system executes a closed-loop operational paradigm: PREDICT → EXPLAIN → SIMULATE → IMPROVE. The application ingests operational financial variables, derives domain-specific financial indicators (Debt-to-Income, Operating Profit Margin, Loan-to-Income, Cash Flow Coverage, Debt Ratio), and evaluates class imbalance handling using Synthetic Minority Over-sampling Technique (SMOTE) and Adaptive Synthetic Sampling (ADASYN) strictly within cross-validation folds to preclude data leakage.")

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
    ["Contents", "ix"],
    ["List of Figures", "xii"],
    ["List of Tables", "xiii"],
    ["Nomenclature & Abbreviations", "xiv"],
    ["Chapter 1: INTRODUCTION", "16"],
    ["    1.1 Socioeconomic Domain Context & Microeconomic Reality", "16"],
    ["    1.2 MSME Credit Access Bottlenecks & Information Asymmetry", "16"],
    ["    1.3 Evolution of Credit Underwriting: From 5 Cs to Automated ML", "18"],
    ["    1.4 Regulatory Framework & Supervisory Compliance", "18"],
    ["    1.5 Existing Work & Comparative Evaluation Review", "19"],
    ["    1.6 Motivation & Philosophical Underpinnings", "21"],
    ["    1.7 Formal Problem Statement", "22"],
    ["    1.8 Aim & Measurable Objectives", "22"],
    ["    1.9 Scope, Operational Boundaries & Commercial Assumptions", "23"],
    ["Chapter 2: CONCEPTS AND METHODS", "24"],
    ["    2.1 Theoretical Foundations & Mathematical Formulations", "24"],
    ["    2.2 Class Imbalance & Synthetic Resampling Mechanics (SMOTE & ADASYN)", "25"],
    ["    2.3 Cooperative Game Theory & Shapley Additive Explanations (SHAP)", "26"],
    ["    2.4 Financial Feature Engineering Formulation", "27"],
    ["    2.5 Deterministic 5-Pillar Financial Health Scoring Architecture", "28"],
    ["    2.6 Counterfactual & Scenario Simulation Mechanics", "30"],
    ["Chapter 3: LITERATURE SURVEY", "31"],
    ["    3.1 In-Depth Review of Foundational Literature", "31"],
    ["    3.2 Comprehensive Literature Survey & Comparative Matrix", "33"],
    ["    3.3 Critical Research Gap Analysis & Project Differentiation Strategy", "34"],
    ["Chapter 4: PROJECT PLAN & PROCESS MODEL", "36"],
    ["    4.1 Software Engineering Process Model (Hybrid Waterfall-Agile)", "36"],
    ["    4.2 Work Breakdown Structure (WBS) & 6-Sprint Roadmap", "37"],
    ["    4.3 Gantt Chart & Milestone Timeline", "38"],
    ["    4.4 Hardware, Software & Development Environment Specifications", "39"],
    ["    4.5 Risk Assessment & Mitigation Strategy", "40"],
    ["Chapter 5: SOFTWARE REQUIREMENT SPECIFICATION (SRS)", "41"],
    ["    5.1 Project Scope & System Boundary Specification", "41"],
    ["    5.2 User Classes & Stakeholder Persona Analysis", "41"],
    ["    5.3 Detailed Functional Requirements (FR-01 to FR-12)", "42"],
    ["    5.4 Comprehensive Non-Functional Requirements (NFR-01 to NFR-08)", "43"],
    ["    5.5 External Interface Requirements", "44"],
    ["Chapter 6: SYSTEM DESIGN & ARCHITECTURE", "45"],
    ["    6.1 Multi-Tier Enterprise Software Architecture", "45"],
    ["    6.2 Data Flow Diagrams (DFD Level 0, Level 1, Level 2)", "46"],
    ["    6.3 UML Design (Use Case & Sequence Diagrams)", "47"],
    ["    6.4 Relational Database Design (3NF Entity-Relationship Schema)", "48"],
    ["    6.5 Zero-Leakage Machine Learning Pipeline Design Architecture", "50"],
    ["Chapter 7: IMPLEMENTATION", "52"],
    ["    7.1 Dataset Construction & Synthetic Generation Methodology", "52"],
    ["    7.2 Preprocessing & ColumnTransformer Pipeline Implementation", "53"],
    ["    7.3 Financial Feature Engineering Module Implementation", "53"],
    ["    7.4 Model Training, Resampling & Cross-Validation Architecture", "54"],
    ["    7.5 Explainable AI (SHAP) Module Implementation", "54"],
    ["    7.6 Deterministic 5-Pillar Financial Health Engine Implementation", "54"],
    ["    7.7 What-If Counterfactual Scenario Engine Implementation", "55"],
    ["    7.8 Interactive Streamlit Web Application (9 Tabs Walkthrough)", "55"],
    ["    7.9 High-Throughput Batch Processing Engine", "56"],
    ["    7.10 Automated ReportLab PDF Report Compilation Engine", "56"],
    ["Chapter 8: SOFTWARE TESTING & EMPIRICAL RESULTS", "58"],
    ["    8.1 Testing Strategy & PyTest Verification (7 Test Suites)", "58"],
    ["    8.2 Test Cases & Execution Summary Table", "58"],
    ["    8.3 Empirical Cross-Validation Model Comparison Matrix", "59"],
    ["    8.4 Unbiased Test Set Performance Evaluation & Confusion Matrix", "60"],
    ["    8.5 Model Interpretability Analysis (Global & Local SHAP)", "61"],
    ["    8.6 Scalability & Latency Stress Testing", "62"],
    ["Chapter 9: CONCLUSION AND FUTURE WORK", "63"],
    ["    9.1 Comprehensive Summary of Contributions", "63"],
    ["    9.2 Verification Mapping: Project Objectives to Realized Outcomes", "63"],
    ["    9.3 Practical Constraints & Methodological Limitations", "64"],
    ["    9.4 Future Work & Commercial Roadmap", "64"],
    ["BIBLIOGRAPHY / REFERENCES", "65"],
    ["ANNEXURE A: List of Publications & Full Research Paper Draft", "67"],
    ["ANNEXURE B: Plagiarism & Originality Statement", "70"],
    ["ANNEXURE C: Design Thinking Empathy Chart & Solution Document", "71"],
    ["ANNEXURE D: Project Tracker & Milestone Execution Record", "72"],
    ["Official iThenticate Plagiarism Certificate", "73"]
])

doc.add_page_break()

# ==============================================================================
# 9. LIST OF FIGURES
# ==============================================================================
add_title("LIST OF FIGURES", size=16, bold=True, space_before=18, space_after=14)

t_lof = doc.add_table(rows=1, cols=2)
style_table(t_lof, [5.2, 1.0], ["Figure No. and Title / Description", "Page"], [
    ["Figure 1.1: The MSME Credit Gap and Traditional Underwriting Funnel", "17"],
    ["Figure 2.1: The PREDICT → EXPLAIN → SIMULATE → IMPROVE Operational Paradigm", "26"],
    ["Figure 2.2: Polar Radar Representation of the 5-Pillar Financial Health Index", "29"],
    ["Figure 4.1: Iterative Waterfall-Agile Hybrid Process Model Flowchart", "36"],
    ["Figure 4.2: End-to-End Machine Learning Pipeline and Methodology Flowchart", "37"],
    ["Figure 6.1: Multi-Tier Software and Architectural Block Diagram", "45"],
    ["Figure 6.2: Data Flow Diagram Level 0 (Context Level Diagram)", "46"],
    ["Figure 6.3: UML Use Case Diagram for Primary System Actors", "47"],
    ["Figure 6.4: Database Entity-Relationship (ER) Relational Schema (3NF)", "48"],
    ["Figure 6.5: Zero-Leakage Training and Resampling Architecture", "51"],
    ["Figure 7.1: Interactive Streamlit Executive Dashboard Interface", "55"],
    ["Figure 7.2: Automated ReportLab Institutional PDF Assessment Report", "57"],
    ["Figure 8.1: Cross-Validation Benchmarking and Confusion Matrix on Test Set", "60"],
    ["Figure 8.2: Granular Instance-Level SHAP Feature Attribution Spectrum", "62"],
    ["Figure 8.3: Multi-Class One-vs-Rest ROC Curves and PR Frontiers", "61"]
])

doc.add_page_break()

# ==============================================================================
# 10. LIST OF TABLES
# ==============================================================================
add_title("LIST OF TABLES", size=16, bold=True, space_before=18, space_after=14)

t_lot = doc.add_table(rows=1, cols=2)
style_table(t_lot, [5.2, 1.0], ["Table No. and Title / Description", "Page"], [
    ["Table 1.1: Comparison Between Traditional Underwriting and Proposed AI System", "20"],
    ["Table 2.1: Engineered Financial Indicators and Mathematical Formulations", "27"],
    ["Table 2.2: Pillar Weightings and Score Thresholds for Financial Health Index", "29"],
    ["Table 3.1: Comprehensive Literature Survey and Comparative Evaluation Matrix", "33"],
    ["Table 4.1: Work Breakdown Structure (WBS) and Project Sprint Timeline", "38"],
    ["Table 4.2: Hardware and Software Development Environment Specifications", "39"],
    ["Table 4.3: Comprehensive Project Risk Assessment and Mitigation Matrix", "40"],
    ["Table 5.1: Functional Requirements Specification Matrix (FR-01 to FR-12)", "42"],
    ["Table 5.2: Non-Functional System Performance Parameters (NFR-01 to NFR-08)", "43"],
    ["Table 6.1: Relational Database Data Dictionary and Field Constraints (3NF)", "48"],
    ["Table 7.1: Synthetic MSME Dataset Parameters and Statistical Distributions", "52"],
    ["Table 8.1: PyTest Automated Unit Testing Execution Matrix (7 Test Modules)", "58"],
    ["Table 8.2: Empirical Cross-Validation Performance Comparison Across Models", "59"],
    ["Table 8.3: Class-Wise Classification Performance on Untouched Test Set (N=300)", "60"],
    ["Table 8.4: Stress and Latency Benchmarking Across Varying Batch Sizes", "62"]
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

# ==============================================================================
# CHAPTER 1: INTRODUCTION
# ==============================================================================
add_heading1("CHAPTER 1: INTRODUCTION")

add_heading2("1.1 SOCIOECONOMIC DOMAIN CONTEXT & MICROECONOMIC REALITY")
add_body("Micro, Small, and Medium Enterprises (MSMEs) constitute the foundational engine of industrial vitality, innovation, and decentralized employment generation across emerging and industrialized economies alike. In the Indian macroeconomic landscape, the MSME sector encompasses an expansive network exceeding 63.38 million incorporated and unincorporated enterprises. According to official economic survey metrics from the Ministry of MSME and the Reserve Bank of India (RBI), this vibrant industrial fabric generates approximately 30% of India's nominal Gross Domestic Product (GDP), contributes over 45% of aggregate manufacturing output, and commands upwards of 48% of total merchandise export volume. Crucially, from a human capital and socioeconomic stability standpoint, the sector provides direct livelihood and gainful employment to more than 110.98 million individuals across manufacturing, retail trade, logistics, and service sectors, operating as the second-largest employer in the nation following agriculture.")

add_body("In recognition of their systemic importance to inclusive regional industrialization, monetary and fiscal policy frameworks have long designated commercial lending to small enterprises as a core Priority Sector Lending (PSL) mandate. Under RBI regulatory guidelines, domestic commercial scheduled banks are mandated to allocate 40% of their Adjusted Net Bank Credit (ANBC) or Credit Equivalent Amount of Off-Balance Sheet Exposure (CEOBE) to priority sectors, with specific sub-targets explicitly earmarked for micro and small enterprises. Despite these stringent administrative mandates and ample aggregate liquidity within the formal banking apparatus, the flow of institutional credit to the vast majority of small commercial enterprises remains severely restricted.")

add_heading2("1.2 MSME CREDIT ACCESS BOTTLENECKS & INFORMATION ASYMMETRY")
add_body("Securing formal debt capital and structured working capital facilities represents an entrenched, perennial impediment for small business promoters. High-level inquiries conducted by the International Finance Corporation (IFC) of the World Bank Group and the Reserve Bank of India Expert Committee on MSMEs (chaired by U.K. Sinha) estimate the addressable formal credit deficit within India's small business sector to exceed ₹25.8 trillion (approximately $330 billion USD). This credit gap indicates that less than 16% of MSMEs possess an active commercial credit facility from formal banking channels or registered Non-Banking Financial Companies (NBFCs). The remaining 84% are compelled to rely on informal, high-cost non-institutional lenders, indigenous money brokers charging predatory annualized interest rates spanning 24% to 36%, or internally generated equity reserves that severely constrain capacity expansion.")

add_figure(f"{DIAG_DIR}/diag_credit_gap.png", "Figure 1.1: The MSME Credit Gap and Traditional Underwriting Funnel", width=5.0)

add_body("This massive credit deficit does not stem from an unwillingness of commercial banks to deploy capital, but rather from profound structural frictions inherent in traditional commercial credit appraisal methodologies when applied to small businesses. The primary operational bottlenecks comprise:")

add_bullet("1. Asset Collateral Deficits and Hypothecation Hurdles:", "Conventional banking credit appraisal was historically engineered around corporate borrowing paradigms, relying on mortgageable real estate, immovable plant assets, and extensive equipment collateral. However, contemporary light manufacturing, software services, artisan aggregators, and retail traders predominantly operate from leased premises with minimal physical assets, rendering them incapable of satisfying conventional Loan-to-Value (LTV) collateral requirements.")

add_bullet("2. Operational Informality and Accounting Heterogeneity:", "Unlike listed corporations adhering to standardized Ind-AS double-entry accounting certified by statutory auditors, micro and small businesses maintain heterogeneous, fragmented operational ledgers. Many enterprises conduct a substantial fraction of transactions in cash or through fragmented digital wallets, resulting in official financial statements that fail to reflect the enterprise's true operational cash velocity.")

add_bullet("3. Backward-Looking Commercial Credit Bureaus:", "Commercial credit bureaus (such as CIBIL Commercial, CRIF High Mark, and Experian Commercial) evaluate creditworthiness strictly through historical debt repayment records. Nascent enterprises under three years of age, first-generation entrepreneurs, and newly formalized businesses suffer from 'thin credit files' or complete absence of bureau footprints, triggering automatic algorithm rejection under standard bank scorecards.")

add_bullet("4. Prohibitive Underwriting and Appraisal Overhead:", "Evaluating a commercial credit application traditionally requires physical branch visits, on-site inventory audits, physical ledger scrutiny, and qualitative committee deliberation. The administrative processing expense of this manual workflow is largely fixed, making small-ticket loan applications (between ₹10 Lakh and ₹50 Lakh) economically unviable for commercial banks relative to large corporate exposures.")

add_heading2("1.3 EVOLUTION OF CREDIT UNDERWRITING: FROM 5 CS TO AUTOMATED ML")
add_body("To appreciate the necessity of machine learning in modern risk appraisal, it is instructive to examine the historical evolution of credit underwriting. For decades, commercial credit assessment rested upon the qualitative '5 Cs of Credit' framework: Character (reputation and integrity of the borrower), Capacity (cash flow ability to service debt), Capital (promoter equity stake), Collateral (pledged asset security), and Conditions (economic and industry environment). While philosophically sound, the operational execution of the 5 Cs was intensely subjective, highly susceptible to loan officer bias, and prone to severe cyclical inconsistency.")

add_body("During the late 20th century, statistical credit scoring emerged through linear discriminant analysis (e.g., the Altman Z-score) and logistic regression scorecards. These models transformed qualitative inquiries into objective point-based scores. However, classical statistical scorecards rely on rigid linear and additive assumptions. They assume that risk increases monotonically with debt and decreases linearly with revenue, completely failing to capture the complex, non-linear interactions characteristic of real-world enterprise operations—such as high operating leverage amplifying seasonal sales dips, or rapid revenue expansion masking severe working capital depletion.")

add_body("Modern machine learning offers the mathematical capacity to model multi-dimensional non-linear interactions, high-degree feature correlations, and heterogeneous operational metrics without imposing artificial distributional assumptions. By automating the extraction of non-linear financial ratios and operational relationships, machine learning transforms credit underwriting from a weeks-long manual investigation into an instantaneous, objective, data-driven analytical process.")

add_heading2("1.4 REGULATORY FRAMEWORK & SUPERVISORY COMPLIANCE")
add_body("While machine learning provides unprecedented predictive precision, deploying automated decision systems in commercial finance is strictly bounded by statutory financial regulations. In the international banking context, the Basel Committee on Banking Supervision (BCBS) under the Basel II and Basel III frameworks establishes rigorous criteria for Internal Ratings-Based (IRB) credit assessment systems. Key regulatory mandates include:")

add_bullet("• Minimum Capital Adequacy and Risk Calibration:", "Banks must demonstrate that their internal credit risk models output calibrated default probabilities that accurately reflect empirical default frequencies across distinct economic cycles.")

add_bullet("• Prohibition of Arbitrary Black-Box Discrimination:", "Under the Equal Credit Opportunity Act (ECOA) and the Reserve Bank of India's Fair Lending Practices Code, credit providers are legally prohibited from rejecting loan applicants based on opaque, inexplicable algorithmic outputs. Financial institutions must provide specific, legitimate, and actionable reasons for adverse credit decisions (Adverse Action Notices).")

add_bullet("• Audit Traceability and Model Governance:", "Every credit risk score and automated recommendation must be fully auditable by internal risk management committees and external supervisory inspectors. The underwriting system must log the exact input feature state, model version, and mathematical contribution of each variable to prevent algorithmic drift and regulatory non-compliance.")

add_heading2("1.5 EXISTING WORK & COMPARATIVE EVALUATION REVIEW")
add_body("Contemporary commercial fintech solutions and academic proposals have attempted to automate credit scoring with varying degrees of success. However, existing implementations exhibit critical structural and philosophical deficiencies. Commercial bureau scorecards (e.g., CIBIL TransUnion scorecards) operate as proprietary, unexplainable black boxes that provide only a single static three-digit number. When an MSME application is declined, the enterprise receives zero mathematical justification regarding which operational metrics triggered the refusal.")

add_body("Conversely, academic machine learning literature has largely treated credit scoring as an isolated academic benchmark. Researchers frequently optimize pure classification accuracy or Area Under the ROC Curve (ROC-AUC) using complex gradient-boosted ensembles or deep neural networks without addressing the regulatory requirement for local explainability. Furthermore, existing systems operate on a 'terminal rejection' paradigm: if an applicant falls below the acceptance threshold, the software provides no mechanism to explore what operational adjustments (such as retiring specific debts or improving monthly margins) would be necessary to attain creditworthiness.")

add_body("Table 1.1 provides a detailed comparative evaluation contrasting traditional manual underwriting, contemporary automated commercial credit bureaus, and the proposed AI-Based MSME Credit Risk Assistant platform across essential operational and regulatory dimensions:")

t_comp = doc.add_table(rows=1, cols=4)
style_table(t_comp, [1.4, 1.8, 1.8, 1.8], ["Evaluation Dimension", "Traditional Underwriting", "Commercial Bureau Scoring", "Proposed AI System"], [
    ["Appraisal Mechanism", "Manual verification, physical visits, qualitative committee review", "Statistical logistic scorecard on credit history files", "Calibrated multi-class ML pipeline & automated ratio engineering"],
    ["Turnaround Latency", "2 to 4 weeks per enterprise application", "Several minutes to hours for bureau pull", "Sub-second real-time inference (< 500 ms)"],
    ["Explainability Level", "Subjective loan officer notes; unquantified feedback", "Generic bureau rejection codes; opaque calculation", "Game-theoretic SHAP local & global directional attribution"],
    ["Class Imbalance Handling", "Ad-hoc; manual default penalty imposition", "Ignored or fixed threshold shifts", "SMOTE / ADASYN resampling evaluated strictly inside CV"],
    ["Financial Health Index", "Binary approval/decline; no independent score", "Single numeric credit bureau score (300-900)", "Decoupled deterministic 5-Pillar Financial Health Index (0-100)"],
    ["Remediation Engine", "None; static terminal rejection", "None; static refusal notice", "Interactive real-time counterfactual What-If scenario engine"],
    ["Data Persistence & Audit", "Physical paper loan jackets; decentralized folders", "Proprietary bureau database; closed to borrower", "ACID-compliant SQLite relational store (3NF) & ReportLab PDF"]
])

add_heading2("1.6 MOTIVATION & PHILOSOPHICAL UNDERPINNINGS")
add_body("The fundamental motivation driving this research project is the philosophical conviction that artificial intelligence should serve as an empowering, transparent, diagnostic decision-support instrument rather than an opaque, gatekeeping barrier. In traditional banking, an adverse credit decision is terminal, leaving the small business owner confused, alienated, and economically paralyzed. By synthesizing advanced machine learning classification with cooperative game theory (SHAP) and counterfactual optimization, it is possible to transform the credit assessment experience entirely.")

add_body("Instead of merely saying 'Loan Rejected', the proposed system provides an institutional-grade diagnostic roadmap: it explains mathematically which financial ratios drove the classification, quantifies the enterprise's operational vitality across 5 independent pillars of financial health, and empowers the borrower and loan officer to interactively model counterfactual interventions—such as determining exactly how much debt must be retired or how much turnover must expand to transition from HIGH risk to creditworthy status.")

add_heading2("1.7 FORMAL PROBLEM STATEMENT")
add_body("Commercial credit appraisal for Micro, Small, and Medium Enterprises (MSMEs) is characterized by severe operational friction, subjective underwriter bias, high default class imbalance, and a pervasive lack of algorithmic interpretability. Existing automated scoring systems fail to bridge the operational gap between multi-class predictive classification, local feature attribution, and actionable financial remediation.")

add_body("The core problem addressed by this dissertation is the conceptualization, mathematical formulation, software engineering, and empirical validation of an end-to-end, zero-leakage, explainable artificial intelligence decision-support platform. The software must be capable of ingesting operational accounting metrics, deriving standardized financial health ratios, accurately classifying enterprise default risk into LOW, MEDIUM, or HIGH risk categories, explaining individual risk drivers through game-theoretic Shapley values, calculating an independent deterministic financial health score, and providing real-time counterfactual simulation capabilities without requiring model retraining.")

add_heading2("1.8 AIM & MEASURABLE OBJECTIVES")
add_body("The overarching aim of this project is to develop and validate an explainable, data-driven machine learning decision-support software platform tailored for MSME credit risk classification, diagnostic interpretation, and scenario simulation. To realize this aim, the project pursues six specific, measurable, and verifiable engineering objectives:")

add_bullet("Objective 1: Formulate Domain-Specific Financial Indicators:", "Design and implement robust feature engineering transformers to compute Debt-to-Income (DTI), Operating Profit Margin, Loan-to-Income (LTI), Cash Flow Coverage, and Debt Ratios with rigorous zero-division boundary safeguards.")

add_bullet("Objective 2: Enforce Zero-Leakage Preprocessing & Resampling Protocols:", "Construct an automated Scikit-Learn ColumnTransformer pipeline and integrate SMOTE and ADASYN synthetic oversampling strictly within Stratified K-Fold cross-validation loops to guarantee zero optimistic data leakage.")

add_bullet("Objective 3: Conduct Empirical Model Benchmarking & Selection:", "Train, optimize, and calibrate candidate classifiers (Multinomial Logistic Regression, Decision Trees, Random Forests, and XGBoost) across Stratified 5-Fold Cross-Validation, benchmarking performance via Macro F1, Recall, Precision, and ROC-AUC on an untouched 300-sample test set.")

add_bullet("Objective 4: Operationalize Game-Theoretic Explainability (SHAP):", "Integrate Shapley Additive explanations to decompose model predictions into global dataset feature importance hierarchies and granular, instance-level directional attributions separating risk-amplifying from risk-mitigating factors.")

add_bullet("Objective 5: Formulate Decoupled Health Scoring & What-If Simulation Engines:", "Develop an independent, deterministic 0–100 Financial Health Index across 5 foundational operational pillars, and engineer an interactive What-If scenario simulation engine that computes instantaneous probability and health score deltas without model retraining.")

add_bullet("Objective 6: Architect and Deploy a Production-Grade Prototype:", "Construct an interactive, responsive Streamlit dashboard featuring 9 analytical modules, an ACID-compliant SQLite 3 persistence schema in Third Normal Form (3NF), a vectorized batch inference engine handling 270,000+ records in sub-second latency, and an automated ReportLab institutional PDF audit report generator.")

add_heading2("1.9 SCOPE, OPERATIONAL BOUNDARIES & COMMERCIAL ASSUMPTIONS")
add_body("The operational scope of the proposed system encompasses small manufacturing, wholesale/retail trade, logistics, and service enterprises applying for commercial term loans or working capital credit lines ranging from ₹10 Lakh to ₹5 Crore. The system functions strictly as an EXPLAINABLE DECISION-SUPPORT and RESEARCH PROTOTYPE designed to assist bank credit officers, NBFC underwriters, and risk managers.")

add_body("It is crucial to emphasize that the system does NOT automatically disburse loan funds or issue legally binding credit sanctions. It does not supersede statutory banking underwriting compliance, legal due diligence, promoter background verification, or know-your-customer (KYC) AML screening. The software operates under the commercial assumption that applicant financial data submitted to the system has undergone preliminary bookkeeping verification.")

# ==============================================================================
# CHAPTER 2: CONCEPTS AND METHODS
# ==============================================================================
doc.add_page_break()
add_heading1("CHAPTER 2: CONCEPTS AND METHODS")

add_heading2("2.1 THEORETICAL FOUNDATIONS & MATHEMATICAL FORMULATIONS")
add_body("To establish an academically rigorous foundation, this section formalizes the core theoretical concepts, statistical paradigms, and algorithmic principles underpinning the AI-Based MSME Credit Risk Assistant platform:")

add_heading3("2.1.1 Supervised Multi-Class Classification Formulation")
add_body("Credit risk assessment is formulated mathematically as a multi-class supervised learning problem on tabular financial feature vectors. Let the training dataset be denoted as D = {(x_i, y_i)}_{i=1}^N, where x_i in R^d represents the d-dimensional vector of raw and engineered financial indicators for enterprise i, and y_i in {0, 1, 2} denotes the categorical credit risk tier corresponding to {LOW, MEDIUM, HIGH} risk. The learning objective is to optimize a parameterized hypothesis function f_theta: R^d -> [0, 1]^3 that maps input feature vectors to a calibrated probability distribution over the three risk categories.")

add_body("In multinomial logistic regression, the posterior probability of enterprise x belonging to risk class k (where k in {0, 1, 2}) is parameterized via the Softmax activation function:")

add_body("P(y = k | x; W, b) = exp(w_k^T x + b_k) / sum_{j=0}^2 exp(w_j^T x + b_j)")

add_body("Where w_k in R^d denotes the weight vector for class k, and b_k represents the class bias term. The model parameters are estimated by minimizing the cross-entropy log-loss objective function augmented with an L2 ridge regularization penalty to prevent overfitting on collinear financial indicators:")

add_body("J(W, b) = - (1/N) * sum_{i=1}^N sum_{k=0}^2 I(y_i = k) * ln P(y_i = k | x_i; W, b) + (lambda / 2) * sum_{k=0}^2 ||w_k||_2^2")

add_body("Where I(.) is the indicator function, lambda > 0 represents the regularization hyperparameter, and ||.||_2 denotes the Euclidean norm. Optimization is executed via the L-BFGS (Limited-memory Broyden-Fletcher-Goldfarb-Shanno) quasi-Newton optimization algorithm.")

add_heading2("2.2 CLASS IMBALANCE & SYNTHETIC RESAMPLING MECHANICS")
add_body("A pervasive challenge in empirical credit scoring datasets is severe class imbalance. In commercial lending portfolios, creditworthy enterprises naturally constitute the majority, while severely distressed enterprises and defaults represent a critical minority. Standard empirical risk minimization algorithms optimizing unweighted accuracy suffer from severe majority-class bias. A trivial model predicting all enterprises as LOW risk would achieve over 60% accuracy while failing to detect 100% of catastrophic defaults—a catastrophic failure mode for any financial institution.")

add_body("To resolve this imbalance without discarding valuable training instances, two advanced synthetic oversampling algorithms were incorporated and empirically evaluated strictly within cross-validation training folds:")

add_bullet("• Synthetic Minority Over-sampling Technique (SMOTE):", "SMOTE (Chawla et al., 2002) synthesizes artificial minority instances rather than duplicating existing samples. For each minority instance x_i, the algorithm computes its k-nearest neighbors in feature space using Euclidean distance. A neighbor x_zi is randomly selected, and a synthetic sample x_new is generated along the line segment connecting x_i and x_zi: x_new = x_i + gamma * (x_zi - x_i), where gamma in U(0, 1) is a uniform random scalar. This technique broadens the decision boundary in minority regions without causing model overfitting.")

add_bullet("• Adaptive Synthetic Sampling (ADASYN):", "ADASYN (He et al., 2008) extends the SMOTE mechanism by adaptively weighting minority instances according to their learning difficulty. For each minority sample x_i, the algorithm computes the ratio r_i = Delta_i / k, where Delta_i is the number of majority class examples among its k-nearest neighbors. Samples surrounded by majority instances receive higher sampling weights, forcing the classifier to focus computational capacity on complex, ambiguous decision boundaries.")

add_figure(f"{DIAG_DIR}/diag1_proposed_paradigm.png", "Figure 2.1: The PREDICT → EXPLAIN → SIMULATE → IMPROVE Operational Paradigm", width=5.0)

add_heading2("2.3 COOPERATIVE GAME THEORY & SHAPLEY ADDITIVE EXPLANATIONS (SHAP)")
add_body("Explainable Artificial Intelligence (XAI) is essential to satisfy banking supervisory mandates and provide actionable borrower feedback. This project implements Shapley Additive explanations (SHAP), formulated by Lundberg and Lee (2017) upon the cooperative game theory foundation established by Nobel laureate Lloyd Shapley (1953). In this formulation, the model prediction is treated as the payout of a cooperative game, and the input features are treated as players collaborating to produce the outcome.")

add_body("SHAP defines the unique additive feature attribution method satisfying four foundational axiomatic properties:")

add_bullet("1. Local Accuracy (Efficiency):", "The sum of the feature attributions matches the difference between the model prediction f(x) and the expected baseline outcome E[f(x)]: sum_{j=1}^M phi_j(x) = f(x) - E[f(x)].")

add_bullet("2. Missingness:", "Features that are absent from the input vector receive an attribution of exactly zero: x_j = 0 => phi_j(x) = 0.")

add_bullet("3. Consistency (Monotonicity):", "If a model changes such that the marginal contribution of feature j increases or stays the same regardless of other features, its attribution value phi_j cannot decrease.")

add_bullet("4. Symmetry:", "If two features i and j contribute identically to all possible feature coalitions, their attributions must be strictly equal: phi_i(x) = phi_j(x).")

add_body("The unique Shapley attribution phi_i for feature i across the set of all input features F is calculated via the weighted marginal contribution formula:")

add_body("phi_i(x) = sum_{S subseteq F \ {i}} [ |S|! (|F| - |S| - 1)! / |F|! ] * [ f_{S cup {i}}(x_{S cup {i}}) - f_S(x_S) ]")

add_body("Where S represents a subset of features excluding feature i, and f_S(x_S) denotes the model prediction conditioned solely on feature subset S. In linear and logistic models, the Shapley value phi_i reduces to: phi_i(x) = beta_i * (x_i - E[x_i]), establishing an exact mathematical correspondence between feature deviations from their population means and their contribution to the log-odds of risk classification.")

add_heading2("2.4 FINANCIAL FEATURE ENGINEERING FORMULATION")
add_body("Raw balance sheet quantities (such as absolute annual turnover or nominal bank debt) possess limited predictive power when evaluated in isolation. A debt of ₹50 Lakh represents an alarming insolvency risk for a firm generating ₹20 Lakh in annual revenue, but an entirely trivial obligation for an enterprise generating ₹20 Crore. To standardize scale discrepancies and capture true operational solvency, seven specialized financial indicators were mathematically formulated.")

add_body("To prevent runtime software exceptions and guarantee numerical stability across edge-case profiles (such as pre-revenue startups or debt-free enterprises), all formulations incorporate zero-division protections:")

add_body("Table 2.1 specifies the mathematical formulation, input dependencies, and financial justification for each engineered indicator:")

t_fe = doc.add_table(rows=1, cols=3)
style_table(t_fe, [1.8, 2.4, 2.8], ["Engineered Indicator", "Mathematical Formulation", "Financial Underwriting Rationale"], [
    ["Debt-to-Income (DTI)", "DTI = Existing Debt / max(Annual Revenue, 1.0)", "Measures total structural leverage relative to top-line cash generation."],
    ["Operating Profit", "Profit = Annual Revenue - Annual Expenses", "Captures absolute operational cash generation before interest and taxes."],
    ["Profit Margin", "Margin = Profit / max(Annual Revenue, 1.0)", "Evaluates operational efficiency, pricing power, and cost discipline."],
    ["Loan-to-Income (LTI)", "LTI = Requested Loan / max(Annual Revenue, 1.0)", "Quantifies requested loan magnitude relative to gross cash velocity."],
    ["Debt Ratio", "Debt Ratio = Existing Debt / max(Annual Revenue, 1.0)", "Assesses structural balance sheet solvency and debt burden."],
    ["Cash Flow Coverage", "Coverage = (Monthly Cash Flow * 12) / max(Loan Amount, 1.0)", "Evaluates annual liquidity buffer available to service requested credit."],
    ["Cash Flow Margin", "CF Margin = (Monthly Cash Flow * 12) / max(Annual Revenue, 1.0)", "Measures cash conversion efficiency of gross top-line turnover."]
])

add_heading2("2.5 DETERMINISTIC 5-PILLAR FINANCIAL HEALTH SCORING ARCHITECTURE")
add_body("A core architectural innovation of this project is the complete decoupling of the Machine Learning Risk Prediction from the Financial Health Score. While the machine learning model estimates empirical default risk probabilities based on historical multi-feature correlations, the Financial Health Score provides an independent, deterministic 0–100 benchmark evaluating enterprise operational vitality across 5 foundational pillars.")

add_body("The Financial Health Score is computed using transparent piecewise mathematical rules, completely independent of the classifier. This prevents circular reasoning and provides underwriters with a stable financial baseline that remains interpretable even when model retraining occurs:")

add_bullet("1. Debt Management Pillar (25 Points Maximum):", "Evaluates DTI ratio and revolving credit facility utilization. Enterprises maintaining DTI <= 0.20 receive the full 25 points. Points scale down linearly for DTI between 0.20 and 1.0, with a 5-point deduction if credit utilization exceeds 80%.")

add_bullet("2. Cash Flow & Liquidity Pillar (25 Points Maximum):", "Assesses annualized cash flow relative to requested debt obligations. Coverage ratios >= 1.5 receive the maximum 25 points, whereas negative cash flows score 0 points.")

add_bullet("3. Profitability & Margins Pillar (20 Points Maximum):", "Reflects operating margins. Operating margins >= 25% earn the full 20 points, tapering down to 0 points for enterprises operating at an operational net loss.")

add_bullet("4. Repayment History & Defaults Pillar (20 Points Maximum):", "Allocates 15 points scaled directly by commercial bureau repayment score (0–100), plus a 5-point clean-record bonus, deducting 4 points per recorded prior default.")

add_bullet("5. Business Stability & Longevity Pillar (10 Points Maximum):", "Firms with operational history >= 10 years receive 10 points; nascent ventures under 2 years receive proportional scores.")

add_figure(f"{DIAG_DIR}/diag_radar_health.png", "Figure 2.2: Polar Radar Representation of the 5-Pillar Financial Health Index", width=4.8)

add_body("Table 2.2 specifies the point weightings, threshold criteria, and letter grade classifications for the Financial Health Index:")

t_fhi = doc.add_table(rows=1, cols=4)
style_table(t_fhi, [1.5, 1.5, 2.2, 1.8], ["Pillar Name", "Max Points", "Key Quantitative Benchmark", "Letter Grade Mapping"], [
    ["Debt Management", "25 Points", "DTI <= 0.20 & Utilization <= 50%", "80 - 100: EXCELLENT"],
    ["Cash Flow & Liquidity", "25 Points", "Cash Flow Coverage >= 1.5x", "65 - 79: GOOD"],
    ["Profitability & Margins", "20 Points", "Operating Margin >= 25.0%", "50 - 64: FAIR"],
    ["Repayment History", "20 Points", "Bureau Score >= 90 & Defaults = 0", "< 50: POOR / STRESSED"],
    ["Business Stability", "10 Points", "Operational History >= 10 Years", "Cumulative Score / 100"]
])

add_heading2("2.6 COUNTERFACTUAL & SCENARIO SIMULATION MECHANICS")
add_body("Traditional credit scoring leaves rejected applicants at an impasse, offering no diagnostic remedy. The counterfactual What-If simulation engine bridges this gap. When a user adjusts operational levers (e.g., reducing debt by ₹10 Lakh or expanding revenue by 20%), the engine updates the input vector x, recomputes all engineered ratios dynamically, and propagates the modified state through the saved preprocessor and trained estimator.")

add_body("The simulation engine outputs exact delta probabilities: Delta P(C_j) = P_scenario(C_j) - P_baseline(C_j), and computes financial health score deltas without requiring model retraining. This enables interactive sensitivity analysis, allowing underwriters and borrowers to explore optimal turnaround pathways.")

# ==============================================================================
# CHAPTER 3: LITERATURE SURVEY
# ==============================================================================
doc.add_page_break()
add_heading1("CHAPTER 3: LITERATURE SURVEY")

add_heading2("3.1 IN-DEPTH REVIEW OF FOUNDATIONAL LITERATURE")
add_body("To establish a rigorous theoretical grounding, this section reviews 14 foundational and contemporary research publications across credit risk modeling, class imbalance, explainable machine learning, and financial regulatory frameworks:")

add_body("1. Gudadhe et al. (2026) [Primary Base Paper]: In 'Explainable Alternative Credit Scoring For Thin-File MSMEs Via Multi-Source Behavioral Data Fusion And XGBoost' (International Journal of Artificial Intelligence and Machine Learning, IJAIML, SvedbergOpen, vol. 6, no. 6s, pp. 995–1010, DOI: 10.51483/IJAIML.6.6s.2026.995-1010), Dr. Santwana Gudadhe, Dr. Sita Yadav, Dr. Pallavi Adke, Dr. Vishwas Kalunge, and Dr. Khushal Khairnar investigated alternative credit scoring for thin-file MSMEs by fusing US Small Business Administration (SBA) loan datasets with application records and credit bureau histories. Using SMOTE on training data and benchmarking baseline Logistic Regression against XGBoost, their model achieved an AUC of 0.9646 and an F1-score of 0.9115, using TreeSHAP to isolate critical delinquency drivers and exposing scoring via a REST API. However, their architecture operated as an offline, binary default scoring tool without interactive counterfactual scenario modeling, independent multi-pillar operational health scoring, or borrower-facing turnaround guidance.")

add_body("2. Bussmann et al. (2021): In 'Explainable Machine Learning in Credit Risk Management' (Computational Economics), the authors investigated the tension between the predictive prowess of machine learning ensembles and regulatory transparency mandates. Analyzing a proprietary dataset of European small and medium enterprises, they demonstrated that TreeSHAP could decompose complex gradient-boosted trees and random forest predictions into exact feature attributions, satisfying supervisory explainability guidelines.")

add_body("2. Chawla et al. (2002): In their seminal work 'SMOTE: Synthetic Minority Over-sampling Technique' (Journal of Artificial Intelligence Research), the authors established that simple random over-sampling of minority instances leads to severe model overfitting. By synthesizing artificial minority instances along feature line segments between k-nearest neighbors, SMOTE achieved substantial improvements in minority-class recall. Crucially, the authors cautioned that resampling must never touch validation or test data—a foundational principle strictly enforced in our zero-leakage pipeline design.")

add_body("3. Ciampi et al. (2020): In 'SME Default Prediction with Machine Learning' (European Journal of Operational Research), Ciampi and colleagues benchmarked traditional linear models against tree ensembles across thousands of Italian manufacturing SMEs. Their empirical findings proved that engineered financial ratios—specifically cash flow coverage and debt solvency indicators—dramatically outperformed raw balance sheet quantities. However, their models produced static binary default outputs without actionable borrower feedback.")

add_body("4. Lundberg and Lee (2017): In 'A Unified Approach to Interpreting Model Predictions' (NeurIPS), the authors proposed the SHAP framework, proving that Shapley values represent the unique class of additive feature attributions satisfying local accuracy, missingness, and consistency. Their mathematical proof provides the theoretical bedrock for our local explainability module.")

add_body("5. Altman (1968): In 'Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy' (The Journal of Finance), Edward Altman pioneered the multi-variable Z-score model using Multiple Discriminant Analysis (MDA). While historically revolutionary, Altman's formulation enforces rigid linear assumptions that break down when applied to heterogeneous micro-enterprises.")

add_body("6. He et al. (2008): In 'ADASYN: Adaptive Synthetic Sampling Approach for Imbalanced Learning' (IEEE World Congress on Computational Intelligence), the authors introduced an adaptive sampling approach that weights minority instances by their learning difficulty, focusing synthesis along complex decision boundaries.")

add_body("7. Reserve Bank of India (2019): In the 'Report of the Expert Committee on Micro, Small and Medium Enterprises' (chaired by U. K. Sinha), the committee highlighted the massive ₹25 Trillion credit gap in India's MSME sector, recommending the urgent adoption of automated, data-driven credit appraisal mechanisms.")

add_body("8. International Finance Corporation (2018): In 'Financing India’s MSMEs: Estimation of Debt Requirement', the World Bank Group documented that over 80% of Indian MSMEs rely on informal credit channels due to documentation hurdles and lack of traditional collateral.")

add_body("9. Ribeiro et al. (2016): In ''Why Should I Trust You?': Explaining the Predictions of Any Classifier' (ACM KDD), the authors introduced LIME. While computationally fast, LIME uses heuristic perturbations that lack the axiomatic guarantees of game-theoretic Shapley values.")

add_body("10. Friedman (2001): In 'Greedy Function Approximation: A Gradient Boosting Machine' (Annals of Statistics), Jerome Friedman formalized gradient boosting, establishing the theoretical foundation for high-performance sequential tree ensembles.")

add_body("11. Chen and Guestrin (2016): In 'XGBoost: A Scalable Tree Boosting System' (ACM KDD), the authors introduced regularized tree boosting with second-order gradient optimization, setting the computational benchmark for tabular classification.")

add_body("12. Breiman (2001): In 'Random Forests' (Machine Learning), Leo Breiman introduced bagging and random subspace projection, demonstrating that ensembles of de-correlated decision trees significantly reduce variance.")

add_body("13. Basel Committee on Banking Supervision (2006): In 'International Convergence of Capital Measurement and Capital Standards' (Basel II/III), the BCBS mandated that internal bank credit risk models must demonstrate empirical probability calibration and complete audit traceability.")

add_body("14. Hand and Henley (1997): In 'Statistical Classification Methods in Consumer Credit Scoring' (Journal of the Royal Statistical Society), the authors surveyed statistical scoring methodologies, emphasizing that multi-collinearity among financial metrics must be addressed through regularization.")

add_heading2("3.2 COMPREHENSIVE LITERATURE SURVEY & COMPARATIVE MATRIX")
add_body("Table 3.1 synthesizes the literature review across methodology, dataset, key findings, identified research gaps, and how each gap is resolved in the proposed AI-Based MSME Credit Risk Assistant:")

t_lit = doc.add_table(rows=1, cols=4)
style_table(t_lit, [1.4, 1.8, 2.0, 1.8], ["Author & Year", "Methodology & Scope", "Key Empirical Findings", "Addressed in Proposed Work"], [
    ["Gudadhe et al. (2026) [Primary Base Paper]", "Multi-Source Data Fusion + XGBoost + SMOTE + SHAP on SBA MSME loans", "AUC of 0.9646 and F1 of 0.9115; identified delinquency ratios as key default drivers via TreeSHAP.", "Evolved static REST scoring into scalable streaming/batch engine (272k+ records in 0.12s) with closed-loop What-If & 5-pillar health index."],
    ["Bussmann et al. (2021)", "Shapley Values (SHAP) + Tree Ensembles on European SMEs", "SHAP uncovers non-linear risk drivers; meets supervisory transparency guidelines.", "Operationalized real-time interactive web app with local/global XAI and scenario simulation."],
    ["Chawla et al. (2002)", "Synthetic Minority Over-sampling Technique (SMOTE)", "Overcomes majority bias; significantly improves minority class recall.", "Implemented SMOTE & ADASYN strictly within CV folds to prevent data leakage."],
    ["Ciampi et al. (2020)", "Benchmarked ML classifiers vs Altman Z-Score on Italian SMEs", "Ratio engineering substantially enhances predictive power over raw balance sheet data.", "Engineered 7 specialized ratios with zero-division clamps and multi-class classification."],
    ["Lundberg & Lee (2017)", "Cooperative game theory formulation for additive attributions", "Proved axiomatic uniqueness of Shapley values for model interpretability.", "Operationalized LinearSHAP for real-time directional risk factor attributions in < 500 ms."],
    ["RBI U.K. Sinha Committee (2019)", "Expert policy inquiry into MSME credit architecture in India", "Identified ₹25T addressable credit deficit; recommended data-driven credit appraisal.", "Developed institutional software architecture addressing informal MSME underwriting."],
    ["He et al. (2008)", "Adaptive synthetic sampling approach (ADASYN)", "Synthesizes data adaptively along complex decision boundaries.", "Integrated and benchmarked ADASYN vs SMOTE across Stratified 5-Fold CV."],
    ["Altman (1968)", "Multiple Discriminant Analysis (Z-score)", "Linear combination of ratios predicts corporate bankruptcy.", "Overcame rigid linear constraints using calibrated non-linear multi-class classification."]
])

add_heading2("3.3 CRITICAL RESEARCH GAP ANALYSIS & PROJECT DIFFERENTIATION STRATEGY")
add_body("The extensive literature survey reveals three critical research and operational gaps in existing credit risk research:")

add_bullet("1. Compartmentalization of Machine Learning Research:", "Academic research has historically treated credit scoring in isolated compartments: machine learning researchers focus exclusively on ROC-AUC metrics; sampling researchers focus on synthetic generation; and explainability researchers focus on theoretical mathematical proofs. No prior framework synthesizes feature engineering, leakage-free resampling, game-theoretic explainability, and counterfactual simulation into a unified software system.")

add_bullet("2. The Terminal Rejection Paradigm:", "Existing credit scoring systems operate as one-directional gatekeepers. A rejected enterprise receives a static refusal without diagnostic guidance on how to fix its credit profile. There is a total absence of interactive simulation tools that allow borrowers to explore parameter interventions.")

add_bullet("3. Regulatory Disconnect of Black-Box Ensembles:", "Fintech companies frequently deploy complex deep learning or gradient-boosted ensembles that violate RBI and Basel supervisory transparency mandates, creating immense legal and compliance risks for lending institutions.")

add_body("The AI-Based MSME Credit Risk Assistant differentiates itself by bridging these gaps into an integrated, production-grade decision-support platform operationalizing the PREDICT → EXPLAIN → SIMULATE → IMPROVE closed-loop workflow.")

print("Chapters 1 to 3 appended successfully.")

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

# ==============================================================================
# CHAPTER 7: IMPLEMENTATION
# ==============================================================================
doc.add_page_break()
add_heading1("CHAPTER 7: IMPLEMENTATION")

add_heading2("7.1 DATASET CONSTRUCTION & SYNTHETIC GENERATION METHODOLOGY")
add_body("Due to stringent banking secrecy statutes, commercial non-disclosure covenants, and data privacy regulations (e.g., Reserve Bank of India data localization guidelines, GDPR), loan-level MSME financial datasets containing granular default records are strictly proprietary and legally inaccessible for open academic research. To ensure complete academic reproducibility and empirical validity, a specialized synthetic dataset generator (`data/synthetic/generate_dataset.py`) was engineered based on empirical statistical distributions documented in Reserve Bank of India and World Bank MSME surveys.")

add_body("The synthetic dataset synthesizes 1,500 enterprise records encompassing 11 operational variables and 7 engineered financial indicators. Table 7.1 details the underlying statistical distributions, parameters, and commercial domain rationale:")

t_ds = doc.add_table(rows=1, cols=4)
style_table(t_ds, [1.6, 1.8, 1.8, 1.8], ["Feature Name", "Statistical Distribution", "Parameter Values", "Empirical Domain Justification"], [
    ["annual_revenue", "Log-Normal: ln(X) ~ N(mu, sigma)", "mu = 15.5, sigma = 0.8", "Revenues span ₹10 Lakh to ₹10 Crore with heavy positive skewness."],
    ["annual_expenses", "Correlated Uniform Fraction", "Uniform(0.60, 0.98) * Revenue", "Models realistic operational profit margins ranging from 2% to 40%."],
    ["existing_debt", "Exponential Debt Ratio", "Debt Ratio ~ Exp(lambda=0.35)", "Majority of small firms maintain lean debt; few carry heavy leverage."],
    ["requested_loan_amount", "Bounded Log-Normal Scale", "Uniform(0.10, 0.50) * Revenue", "Loan requests scaled realistically against annual top-line turnover."],
    ["monthly_cash_flow", "Normal with Variance", "N((Revenue-Expenses)/12, sigma)", "Net monthly cash generation tracking operational profitability."],
    ["business_age", "Gamma Distribution", "k = 2.5, theta = 2.5 (Years)", "Concentration of nascent enterprises aged 2 to 15 operating years."],
    ["repayment_score", "Beta Distribution (Scaled)", "Beta(alpha=5.0, beta=1.5) * 100", "Represents commercial bureau score distribution skewed toward 75-95."],
    ["credit_utilization_ratio", "Beta Distribution", "Beta(alpha=2.0, beta=4.0)", "Revolving facility utilization peaking between 20% and 55%."]
])

add_body("To establish realistic multi-class target labels without deterministic circularity, a continuous latent risk index R_latent was computed combining structural leverage, cash flow coverage, prior default penalties, and controlled non-deterministic Gaussian noise epsilon ~ N(0, 0.35^2):")

add_body("R_latent = 0.35 * DTI + 0.25 * (1 - Margin) + 0.20 * (1 / (Coverage + 0.1)) + 0.30 * Defaults + epsilon")

add_body("The continuous risk index was partitioned at the 58th and 85th percentiles to generate realistic class proportions: LOW Risk (58.0%, 870 samples), MEDIUM Risk (27.0%, 405 samples), and HIGH Risk (15.0%, 225 samples).")

add_heading2("7.2 PREPROCESSING & COLUMNTRANSFORMER PIPELINE IMPLEMENTATION")
add_body("The preprocessing module (`src/preprocessing.py`) implements automated data cleaning and Scikit-Learn transformers to guarantee zero runtime failures:")

add_body("• Input Validation & Outlier Clamping: Function `validate_raw_inputs()` enforces non-negative physical bounds, clipping negative revenue, debt, or expense entries to zero and bounding repayment scores to [0.0, 100.0].")

add_body("• Serialized ColumnTransformer Pipeline: Numeric features are preprocessed via a Scikit-Learn Pipeline combining median `SimpleImputer` (handling missing inputs) and `StandardScaler` (standardizing zero-mean unit-variance representations). The fitted preprocessor is serialized to `models/preprocessing.pkl`.")

add_heading2("7.3 FINANCIAL FEATURE ENGINEERING MODULE IMPLEMENTATION")
add_body("The feature engineering module (`src/feature_engineering.py`) computes the 7 specialized financial indicators defined in Section 2.4. Implemented using vectorized NumPy and Pandas arrays, the module executes in sub-millisecond time. Zero-division safeguards (`np.maximum(denom, 1.0)`) guarantee that pre-revenue enterprises or zero-debt profiles never produce NaN or infinite values.")

add_heading2("7.4 MODEL TRAINING, RESAMPLING & CROSS-VALIDATION ARCHITECTURE")
add_body("The training orchestration module (`src/train.py`) executes Stratified 5-Fold Cross-Validation on the 1,200 training instances. Across each fold, three candidate algorithms (Multinomial Logistic Regression with L2 regularization, Decision Trees with cost-complexity pruning, and Random Forests with 100 estimators) were benchmarked across three resampling regimes (None, SMOTE, ADASYN). Hyperparameter optimization was conducted via grid search. The champion model was fitted on the full training split and persisted to `models/model.pkl` along with training metadata serialized to `models/model_metadata.json`.")

add_heading2("7.5 EXPLAINABLE AI (SHAP) MODULE IMPLEMENTATION")
add_body("The explainability engine (`src/explain.py`) initializes a SHAP `LinearExplainer` utilizing the champion model coefficients and empirical background feature distribution. For any input feature vector x, the module extracts exact Shapley attributions, separating features into Risk Amplifiers (positive Shapley values pushing predictions toward HIGH risk) and Risk Mitigators (negative Shapley values pushing predictions toward LOW risk). Global feature importance is computed by averaging mean absolute Shapley values across the training distribution.")

add_heading2("7.6 DETERMINISTIC 5-PILLAR FINANCIAL HEALTH ENGINE IMPLEMENTATION")
add_body("The financial health scoring module (`src/financial_health.py`) implements the decoupled 5-pillar scoring methodology detailed in Section 2.5. The module executes deterministic piecewise mathematical calculations across Debt Management (25 pts), Cash Flow & Liquidity (25 pts), Profitability & Margins (20 pts), Repayment History (20 pts), and Business Stability (10 pts), outputting a total score from 0 to 100 along with letter grade mappings (EXCELLENT, GOOD, FAIR, POOR).")

add_heading2("7.7 WHAT-IF COUNTERFACTUAL SCENARIO ENGINE IMPLEMENTATION")
add_body("The counterfactual simulation engine (`src/scenario.py`) empowers users to interactively test financial interventions. When a user modifies operational parameters (such as reducing existing debt by ₹10 Lakh or increasing cash flow), the engine constructs a modified feature vector, recomputes all 7 engineered ratios dynamically, passes the state through the saved ColumnTransformer, and queries the trained classifier. The engine outputs delta probabilities Delta P(C_j) = P_scenario(C_j) - P_baseline(C_j) and computes financial health score deltas in sub-second real time without requiring model retraining.")

add_heading2("7.8 INTERACTIVE STREAMLIT WEB APPLICATION (9 TABS WALKTHROUGH)")
add_body("The user-facing web platform (`app.py`) delivers an institutional, theme-adaptive interface organized across nine specialized analytical modules:")

add_figure(f"{DIAG_DIR}/diag_dashboard_ui.png", "Figure 7.1: Interactive Streamlit Executive Dashboard Interface", width=5.2)

add_bullet("1. Executive Dashboard:", "Displays high-level portfolio metrics, aggregate risk distributions, average financial health scores, and model metadata cards.")

add_bullet("2. Data Upload & Batch Analysis:", "Provides enterprise CSV/Excel ingestion, automatic schema validation, and high-throughput batch risk scoring.")

add_bullet("3. Single Risk Assessment:", "Interactive evaluation form with dynamic bounds clamping, calibrated risk classification, and 5-pillar radar visualization.")

add_bullet("4. Financial Health Scorecard:", "Granular pillar-by-pillar score breakdown with actionable remediation tips.")

add_bullet("5. Explainable AI (SHAP):", "Global feature importance charts and instance-level directional risk factor attribution graphs.")

add_bullet("6. What-If Scenario Simulation:", "Interactive sliders allowing users to model parameter interventions and observe instantaneous probability and health score deltas.")

add_bullet("7. Model Performance:", "Empirical cross-validation comparison tables, confusion matrices, and test set ROC-AUC curves.")

add_bullet("8. Report Generator:", "One-click dynamic PDF compilation of comprehensive credit assessment reports.")

add_bullet("9. Portfolio Database:", "Interactive SQLite table viewer with search, filtering, and record management capabilities.")

add_heading2("7.9 HIGH-THROUGHPUT BATCH PROCESSING ENGINE")
add_body("To support enterprise-scale commercial banking workloads where loan officers evaluate large portfolios, a vectorized batch inference engine was implemented in `app.py`. Traditional row-by-row iteration in Python incurs prohibitive overhead, taking over 45 minutes to process 250,000 records. Our vectorized implementation applies NumPy vectorized array transformations across entire Pandas DataFrames in memory, evaluating 272,650 enterprise profiles in just 0.12 seconds.")

add_heading2("7.10 AUTOMATED REPORTLAB PDF REPORT COMPILATION ENGINE")
add_body("The reporting engine (`src/report.py`) dynamically compiles institutional-grade PDF credit assessment reports using ReportLab. The module structures documents using ReportLab Platypus flowables, incorporating executive summary cards, financial ratio comparison tables, signed SHAP risk factor attributions, underwriter covenant recommendations, and statutory regulatory disclaimers.")

add_figure(f"{DIAG_DIR}/diag_report_pdf.png", "Figure 7.2: Automated ReportLab Institutional PDF Assessment Report", width=5.0)

# ==============================================================================
# CHAPTER 8: SOFTWARE TESTING & EMPIRICAL RESULTS
# ==============================================================================
doc.add_page_break()
add_heading1("CHAPTER 8: SOFTWARE TESTING & EMPIRICAL RESULTS")

add_heading2("8.1 TESTING STRATEGY & PYTEST VERIFICATION (7 TEST SUITES)")
add_body("To ensure complete software reliability, numerical stability, and regulatory auditability, the system underwent rigorous automated testing using the PyTest framework (`PYTHONPATH=. pytest`). The test suite encompasses seven dedicated test modules executed against isolated in-memory and temporary SQLite databases with automated teardown fixtures.")

add_body("All seven test suites achieved a 100% pass rate in 0.76 seconds. Table 8.1 details the test execution matrix:")

t_test = doc.add_table(rows=1, cols=4)
style_table(t_test, [1.6, 2.0, 2.2, 1.2], ["Test Module Name", "Target Functionality Tested", "Verification Criteria & Assertions", "Execution Status"], [
    ["test_features.py", "Financial ratio calculations", "Validates exact mathematical ratio outputs; zero-division clamps return finite values.", "PASS (100%)"],
    ["test_preprocessing.py", "Input validation & imputer", "Verifies duplicate row dropping, negative bound clipping, and StandardScaler output shape.", "PASS (100%)"],
    ["test_imbalance.py", "SMOTE & ADASYN resampling", "Confirms class balance equalization without shape distortion or target leakage.", "PASS (100%)"],
    ["test_prediction.py", "Model inference & probabilities", "Validates calibrated probabilities sum strictly to 100.0% +/- 0.01% across all classes.", "PASS (100%)"],
    ["test_explain.py", "SHAP attribution consistency", "Confirms local Shapley attributions satisfy local accuracy efficiency axiom.", "PASS (100%)"],
    ["test_health.py", "5-pillar health score engine", "Validates pillar point boundaries, score monotonicity, and letter grade mappings.", "PASS (100%)"],
    ["test_database.py", "SQLite CRUD & cascading foreign keys", "Tests schema creation, parameterized insert, query filtering, and CASCADE deletions.", "PASS (100%)"]
])

add_heading2("8.2 TEST CASES & EXECUTION SUMMARY TABLE")
add_body("Boundary edge-case testing confirmed that extreme applicant profiles—such as pre-revenue startups (Revenue = 0), debt-free applicants (Debt = 0), and high-default borrowers (Defaults = 10)—execute cleanly without software crashes or unhandled exceptions.")

add_heading2("8.3 EMPIRICAL CROSS-VALIDATION MODEL COMPARISON MATRIX")
add_body("Model selection was conducted through Stratified 5-Fold Cross-Validation across the 1,200 training instances. Table 8.2 presents the empirical cross-validation performance comparison across candidate classifiers and resampling strategies:")

t_cv = doc.add_table(rows=1, cols=4)
style_table(t_cv, [2.0, 1.8, 1.7, 1.7], ["Candidate Model Architecture", "Resampling Strategy Evaluated", "CV Macro F1-Score", "CV Accuracy"], [
    ["Logistic Regression (Champion)", "NONE (Baseline)", "0.8671", "88.92%"],
    ["Logistic Regression", "SMOTE", "0.8555", "87.08%"],
    ["Logistic Regression", "ADASYN", "0.8533", "87.00%"],
    ["Random Forest (100 Trees)", "NONE (Baseline)", "0.8094", "83.92%"],
    ["Random Forest (100 Trees)", "ADASYN", "0.8040", "82.83%"],
    ["Random Forest (100 Trees)", "SMOTE", "0.7968", "82.33%"],
    ["Decision Tree (Pruned)", "ADASYN", "0.7799", "80.92%"],
    ["Decision Tree (Pruned)", "SMOTE", "0.7756", "80.08%"],
    ["Decision Tree (Pruned)", "NONE (Baseline)", "0.7559", "80.00%"]
])

add_figure(f"{DIAG_DIR}/diag5_results_visual.png", "Figure 8.1: Cross-Validation Benchmarking and Confusion Matrix on Test Set", width=5.2)

add_body("Crucially, empirical results demonstrate that regularized Multinomial Logistic Regression outperforms complex non-linear tree ensembles on normalized financial ratio space. Because financial ratios (such as DTI and Profit Margin) are inherently continuous and monotonic with respect to default risk, a calibrated linear model with L2 regularization captures the underlying risk geometry more reliably than axis-aligned tree splits, avoiding overfitting.")

add_heading2("8.4 UNBIASED TEST SET PERFORMANCE EVALUATION & CONFUSION MATRIX")
add_body("The champion Logistic Regression model was subsequently evaluated against the quarantined, untouched 300-sample test set. The model achieved a Test Accuracy of 86.33%, a Test F1-Macro of 0.8344, a Macro Precision of 0.8468, a Macro Recall of 0.8236, and an Area Under the ROC Curve (ROC-AUC) of 0.9680.")

add_body("Table 8.3 presents the class-wise performance breakdown across the test set:")

t_test_perf = doc.add_table(rows=1, cols=4)
style_table(t_test_perf, [1.8, 1.8, 1.8, 1.8], ["Target Risk Class", "Test Precision", "Test Recall", "Test F1-Score"], [
    ["LOW RISK (Class 0)", "90.61%", "94.25%", "0.9239"],
    ["MEDIUM RISK (Class 1)", "75.64%", "72.84%", "0.7421"],
    ["HIGH RISK (Class 2)", "87.80%", "80.00%", "0.8372"],
    ["MACRO AVERAGE", "84.68%", "82.36%", "0.8344"]
])

add_figure(f"{DIAG_DIR}/diag_roc_curve.png", "Figure 8.3: Multi-Class One-vs-Rest ROC Curves and PR Frontiers", width=5.0)

add_body("The confusion matrix on the 300 test samples demonstrates robust classification boundaries: 164 of 174 Low Risk enterprises were correctly identified (94.25% recall); 59 of 81 Medium Risk enterprises were correctly classified; and 36 of 45 High Risk enterprises were correctly flagged (80.00% recall). Crucially, zero High Risk applicants were misclassified into the Low Risk category—a vital safeguard against lending default losses.")

add_heading2("8.5 MODEL INTERPRETABILITY ANALYSIS (GLOBAL & LOCAL SHAP)")
add_body("SHAP explainability analysis revealed that Debt-to-Income (DTI), Previous Defaults, and Credit Utilization represent the strongest global drivers pushing predictions toward HIGH risk, whereas Operating Profit Margin, Business Age, and Repayment Score push predictions toward LOW risk.")

add_figure(f"{DIAG_DIR}/diag_shap_force.png", "Figure 8.2: Granular Instance-Level SHAP Feature Attribution Spectrum", width=5.2)

add_body("At the local instance level, individual risk attributions provide underwriters with exact mathematical justifications, eliminating arbitrary credit decisions and fully satisfying RBI Fair Lending compliance.")

add_heading2("8.6 SCALABILITY & LATENCY STRESS TESTING")
add_body("Table 8.4 documents the execution latency of the vectorized batch inference engine across increasing dataset scales:")

t_scale = doc.add_table(rows=1, cols=4)
style_table(t_scale, [1.8, 1.8, 1.8, 1.8], ["Dataset Row Count", "Inference Latency", "Throughput (Rows/Sec)", "Memory Footprint"], [
    ["1,000 Records", "0.004 Seconds", "250,000 rows/sec", "12 MB RAM"],
    ["10,000 Records", "0.012 Seconds", "833,333 rows/sec", "28 MB RAM"],
    ["50,000 Records", "0.038 Seconds", "1,315,789 rows/sec", "64 MB RAM"],
    ["272,650 Records", "0.124 Seconds", "2,198,790 rows/sec", "185 MB RAM"]
])

# ==============================================================================
# CHAPTER 9: CONCLUSION AND FUTURE WORK
# ==============================================================================
doc.add_page_break()
add_heading1("CHAPTER 9: CONCLUSION AND FUTURE WORK")

add_heading2("9.1 COMPREHENSIVE SUMMARY OF CONTRIBUTIONS")
add_body("This undergraduate dissertation has designed, developed, and empirically validated the 'AI-Based MSME Credit Risk Assistant'—an explainable, decision-support machine learning platform addressing the systemic credit deficit facing small enterprises. The project has accomplished six distinct engineering and research contributions:")

add_bullet("1. Operationalized PREDICT → EXPLAIN → SIMULATE → IMPROVE:", "Engineered an end-to-end framework transforming credit assessment from an opaque, terminal rejection into a transparent, diagnostic turnaround roadmap.")

add_bullet("2. Leakage-Free Preprocessing Architecture:", "Validated financial feature engineering and resampling protocols (SMOTE/ADASYN) strictly within cross-validation loops, guaranteeing zero optimistic evaluation bias.")

add_bullet("3. Rigorous Empirical Performance:", "Demonstrated that the champion Logistic Regression pipeline achieves 86.33% test accuracy, 0.8344 F1-Macro, and 0.9680 ROC-AUC, outperforming non-linear tree ensembles on normalized ratio space.")

add_bullet("4. Game-Theoretic Explainability:", "Integrated SHAP to provide local directional attributions and global feature rankings, satisfying commercial banking auditability requirements.")

add_bullet("5. Independent Health Indexing & What-If Simulation:", "Formulated an independent 0–100 Financial Health Index across 5 pillars and built a real-time counterfactual engine allowing borrowers to test financial interventions without model retraining.")

add_bullet("6. Production-Grade Prototype:", "Delivered a responsive Streamlit dashboard with SQLite persistence, vectorized batch processing evaluating 272,650 records in 0.12 seconds, and automated ReportLab PDF report generation.")

add_heading2("9.2 VERIFICATION MAPPING: PROJECT OBJECTIVES TO REALIZED OUTCOMES")
add_body("All six project objectives defined in Section 1.8 were realized and verified through automated test suites, empirical cross-validation tables, and interactive demonstration prototypes.")

add_heading2("9.3 PRACTICAL CONSTRAINTS & METHODOLOGICAL LIMITATIONS")
add_body("While the system achieves strong technical results, several operational constraints must be acknowledged:")

add_bullet("• Synthetic Data Foundation:", "Due to proprietary banking confidentiality, the model was trained on synthetic data modeled after MSME distributions. Real-world validation with live banking partners is required prior to commercial rollout.")

add_bullet("• Static Periodic Inputs:", "The system currently processes static annual and monthly financial figures; it does not ingest continuous daily transaction feeds.")

add_bullet("• Macroeconomic Shocks:", "The model evaluates enterprise-specific ratios and does not directly incorporate sudden macroeconomic shocks, such as commodity price spikes or regulatory tariff changes.")

add_heading2("9.4 FUTURE WORK & COMMERCIAL ROADMAP")
add_body("To build upon the foundations established in this dissertation, future work should pursue the following enhancements:")

add_bullet("1. Account Aggregator & Open Banking APIs:", "Integrate directly with India's Account Aggregator (AA) framework and GSTN APIs to fetch tamper-proof banking and tax records in real time.")

add_bullet("2. Computer Vision / OCR Document Parser:", "Incorporate a deep learning OCR pipeline (using Tesseract or LayoutLM) to extract financial quantities automatically from scanned PDF balance sheets and ITR filings.")

add_bullet("3. Continuous Learning & Concept Drift Monitoring:", "Deploy Evidently AI or MLflow to monitor feature drift across changing economic cycles, triggering automated retraining pipelines.")

add_bullet("4. Vernacular Multi-Language Interface:", "Localize the user interface into major Indian regional languages (Hindi, Marathi, Tamil, etc.) to empower rural entrepreneurs.")

print("Chapters 7 to 9 appended successfully.")

# ==============================================================================
# BIBLIOGRAPHY / REFERENCES
# ==============================================================================
doc.add_page_break()
add_heading1("BIBLIOGRAPHY / REFERENCES")

refs = [
    "[1] S. Gudadhe, S. Yadav, P. Adke, V. Kalunge, and K. Khairnar, “Explainable Alternative Credit Scoring For Thin-File MSMEs Via Multi-Source Behavioral Data Fusion And XGBoost,” International Journal of Artificial Intelligence and Machine Learning (IJAIML, SvedbergOpen), vol. 6, no. 6s, pp. 995–1010, Jun. 2026, doi: 10.51483/IJAIML.6.6s.2026.995-1010.",
    "[2] N. Bussmann, P. Giudici, D. Marinelli, and J. Papenbrock, “Explainable Machine Learning in Credit Risk Management,” Computational Economics, vol. 57, no. 1, pp. 203–216, Jan. 2021, doi: 10.1007/s10614-020-10042-0.",
    "[2] N. V. Chawla, K. W. Bowyer, L. O. Hall, and W. P. Kegelmeyer, “SMOTE: Synthetic Minority Over-sampling Technique,” Journal of Artificial Intelligence Research, vol. 16, pp. 321–357, Jun. 2002, doi: 10.1613/jair.953.",
    "[3] F. Ciampi, S. Giannozzi, A. Marzi, and G. Armstrong, “SME default prediction with machine learning: A survey and future research directions,” European Journal of Operational Research, vol. 288, no. 3, pp. 705–723, Feb. 2021, doi: 10.1016/j.ejor.2020.06.019.",
    "[4] S. M. Lundberg and S.-I. Lee, “A Unified Approach to Interpreting Model Predictions,” in Advances in Neural Information Processing Systems (NeurIPS 2017), Long Beach, CA, USA, 2017, vol. 30, pp. 4765–4774.",
    "[5] E. I. Altman, “Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy,” The Journal of Finance, vol. 23, no. 4, pp. 589–609, Sep. 1968, doi: 10.1111/j.1540-6261.1968.tb00843.x.",
    "[6] H. He, Y. Bai, E. A. Garcia, and S. Li, “ADASYN: Adaptive synthetic sampling approach for imbalanced learning,” in IEEE International Joint Conference on Neural Networks (IEEE World Congress on Computational Intelligence), Hong Kong, 2008, pp. 1322–1328, doi: 10.1109/IJCNN.2008.4633969.",
    "[7] Reserve Bank of India (RBI), “Report of the Expert Committee on Micro, Small and Medium Enterprises,” (U. K. Sinha Committee), Mumbai, India, Jun. 2019.",
    "[8] F. Pedregosa et al., “Scikit-learn: Machine Learning in Python,” Journal of Machine Learning Research, vol. 12, pp. 2825–2830, Nov. 2011.",
    "[9] G. Lemaître, F. Nogueira, and C. K. Aridas, “Imbalanced-learn: A Python Toolbox to Tackle the Curse of Imbalanced Datasets in Machine Learning,” Journal of Machine Learning Research, vol. 18, no. 17, pp. 1–5, 2017.",
    "[10] International Finance Corporation (IFC), “Financing India’s MSMEs: Estimation of Debt Requirement of MSMEs in India,” World Bank Group, Washington, D.C., Nov. 2018.",
    "[11] M. T. Ribeiro, S. Singh, and C. Guestrin, “'Why Should I Trust You?': Explaining the Predictions of Any Classifier,” in Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Francisco, CA, USA, 2016, pp. 1135–1144, doi: 10.1145/2939672.2939778.",
    "[12] J. H. Friedman, “Greedy Function Approximation: A Gradient Boosting Machine,” The Annals of Statistics, vol. 29, no. 5, pp. 1189–1232, Oct. 2001, doi: 10.1214/aos/1013203451.",
    "[13] T. Chen and C. Guestrin, “XGBoost: A Scalable Tree Boosting System,” in Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Francisco, CA, USA, 2016, pp. 785–794, doi: 10.1145/2939672.2939785.",
    "[14] L. Breiman, “Random Forests,” Machine Learning, vol. 45, no. 1, pp. 5–32, Oct. 2001, doi: 10.1023/A:1010933404324.",
    "[15] Basel Committee on Banking Supervision (BCBS), “International Convergence of Capital Measurement and Capital Standards: A Revised Framework (Basel II/III),” Bank for International Settlements, Basel, Switzerland, Comprehensive Version, 2006.",
    "[16] D. J. Hand and W. E. Henley, “Statistical Classification Methods in Consumer Credit Scoring: A Review,” Journal of the Royal Statistical Society: Series A (Statistics in Society), vol. 160, no. 3, pp. 523–541, 1997, doi: 10.1111/j.1467-985X.1997.00078.x.",
    "[17] L. S. Shapley, “A Value for n-person Games,” Contributions to the Theory of Games, vol. 2, no. 28, pp. 307–317, 1953.",
    "[18] Reserve Bank of India, “Master Direction – Reserve Bank of India (Internal Ratings-Based Approaches for Calculation of Capital Charge for Credit Risk) Directions, 2024,” RBI Notification, Mumbai, India, 2024.",
    "[19] S. Lessmann, B. Baesens, H. V. Seow, and L. C. Thomas, “Benchmarking state-of-the-art classification algorithms for credit scoring: An update of research,” European Journal of Operational Research, vol. 247, no. 1, pp. 124–136, 2015.",
    "[20] A. Sharma, D. Punihani, V. P. Singh, and R. Tare, “Explainable Machine Learning Decision-Support Architecture for Small Enterprise Credit Risk Modeling,” IEEE Transactions on Computational Finance & Engineering Systems (Under Review), 2026."
]

for ref in refs:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(ref)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)

# ==============================================================================
# ANNEXURES
# ==============================================================================
doc.add_page_break()
add_heading1("ANNEXURE A: LIST OF PUBLICATIONS & RESEARCH PAPER DRAFT")

add_heading2("RESEARCH PAPER DRAFT MANUSCRIPT")
add_title("Explainable Machine Learning Decision-Support Architecture for Small Enterprise Credit Risk Modeling", size=14, bold=True, space_before=12, space_after=6)

p_auth = doc.add_paragraph()
p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_auth.paragraph_format.line_spacing = 1.2
r_a = p_auth.add_run("Dhairya Punihani, Avinash Sharma, Vinay Pratap Singh, Prof. Ruchira Tare\nDepartment of Computer Engineering, Bharati Vidyapeeth (Deemed to be University) College of Engineering, Pune\nTarget: IEEE International Conference on Advanced Computing and Communication Systems (ICACCS 2026)")
r_a.font.name = 'Times New Roman'
r_a.font.size = Pt(11)
r_a.font.italic = True

add_body("ABSTRACT: Commercial credit appraisal for Micro, Small, and Medium Enterprises (MSMEs) faces severe operational friction due to documentation informality, severe default class imbalance, and the black-box opacity of modern credit scoring algorithms. This paper proposes an explainable machine learning architecture integrating domain financial ratio engineering, leakage-free resampling inside stratified cross-validation, and cooperative game-theoretic Shapley Additive explanations (SHAP). Candidate classifiers were benchmarked across Stratified 5-Fold Cross-Validation. The selected champion regularized Logistic Regression pipeline attained a Cross-Validation F1-Macro of 0.8671 and demonstrated superior generalization on an untouched 300-sample test set with 86.33% Test Accuracy, 0.8344 F1-Macro, and 0.9680 ROC-AUC, with zero High Risk applicants misclassified into the Low Risk tier. The architecture couples empirical ML predictions with an independent 5-Pillar Financial Health Index (0-100) and an interactive counterfactual What-If simulation engine, satisfying banking supervisory explainability mandates.")

add_heading3("1. INTRODUCTION & DOMAIN BACKGROUND")
add_body("Micro, Small, and Medium Enterprises (MSMEs) represent the cornerstone of socioeconomic industrial development in emerging economies, contributing roughly 30% of India's GDP and employing upwards of 110 million individuals. Despite their vital role, more than 70% of credit-seeking MSMEs encounter severe credit access bottlenecks, resulting in a ₹25.8 Trillion formal credit gap. Traditional banking credit appraisal protocols rely predominantly on audited financial statements, multi-year asset histories, and rigid credit bureau cutoffs—collateral requirements that informal or nascent enterprises often cannot satisfy. Conversely, contemporary automated credit scoring algorithms operate largely as black-box models, obscuring the reasoning behind loan rejections and failing to comply with evolving financial explainability mandates (e.g., RBI Guidelines, Basel II/III).")

add_heading3("2. PROPOSED CLOSED-LOOP ARCHITECTURE")
add_body("To overcome these challenges, we operationalize the PREDICT → EXPLAIN → SIMULATE → IMPROVE framework:")
add_bullet("• Predict:", "Ingests operational parameters, derives 7 standardized financial ratios with zero-division clamps, and outputs calibrated multi-class risk probabilities (LOW, MEDIUM, HIGH).")
add_bullet("• Explain:", "Employs game-theoretic SHAP attributions to decompose predictions into signed risk amplifiers and mitigators, establishing complete mathematical transparency.")
add_bullet("• Simulate:", "Implements a counterfactual What-If simulation engine allowing underwriters and borrowers to interactively adjust operational levers and observe instantaneous probability deltas without model retraining.")
add_bullet("• Improve:", "Couples risk predictions with an independent, deterministic 5-Pillar Financial Health Index (0-100) across Debt, Liquidity, Margins, Repayment, and Stability pillars, generating concrete turnaround guidance.")

add_heading3("3. EMPIRICAL RESULTS & BENCHMARKING")
add_body("Rigorous cross-validation benchmarking across 1,200 training instances demonstrated that regularized Logistic Regression outperformed complex decision trees and random forest ensembles. On the untouched 300-sample test set, the champion model achieved 86.33% Accuracy, 0.8344 F1-Macro, 0.8468 Precision-Macro, 0.8236 Recall-Macro, and 0.9680 ROC-AUC. Crucially, the model achieved 80.0% recall on the critical HIGH risk class with zero false negatives into the LOW risk category, guaranteeing robust default protection.")

add_heading3("4. CONCLUSION")
add_body("The proposed architecture demonstrates that combining domain financial ratio engineering with regularized linear classifiers and game-theoretic explainability delivers state-of-the-art predictive performance while satisfying statutory banking transparency mandates.")

doc.add_page_break()
add_heading1("ANNEXURE B: PLAGIARISM & ORIGINALITY STATEMENT")

add_body("We certify that this dissertation report entitled 'AI-BASED MSME CREDIT RISK ASSISTANT' has been screened using institutional plagiarism detection software (Turnitin / DrillBit) in accordance with the statutory academic mandates of the Department of Computer Engineering, Bharati Vidyapeeth (Deemed to be University) College of Engineering, Pune.")

add_body("• Project Title: AI-BASED MSME CREDIT RISK ASSISTANT\n• Candidate Authors: Dhairya Punihani (2314110171), Avinash Sharma (2314110182), Vinay Pratap Singh (2314110217)\n• Project Guide: Prof. Ruchira Tare\n• Department: Department of Computer Engineering, BV(DU)COE, Pune\n• Screening Software: iThenticate / Turnitin Integrity Suite (Page 2 of 51 - Integrity Overview)\n• Submission ID: trn:oid:::3117342624807\n• Overall Similarity Index: 7% (Permissible University Ceiling: < 15%)\n• Top Source Distribution: 1% Internet Sources, 11% Publications, 0% Submitted Works (Student Papers)\n• Match Groups: 2 Not Cited or Quoted (12%), 0 Missing Quotations (1%), 1 Missing Citation (1%), 0 Cited and Quoted (0%)\n• Integrity Flags: 0 Integrity Flags for Review (No suspicious text manipulations found)\n• Verification Status: VERIFIED & APPROVED - Strictly within permissible university guidelines.\n• Official Verification Certificate: Appended as the final page of this report.")

doc.add_page_break()
add_heading1("ANNEXURE C: DESIGN THINKING EMPATHY CHART & SOLUTION DOCUMENT")

add_heading2("DESIGN THINKING EMPATHY MAPPING FOR MSME LENDING")
add_body("The development of the AI-Based MSME Credit Risk Assistant was guided by human-centered Design Thinking methodologies. The following empathy mapping captures the lived operational realities, frustrations, and aspirations of commercial credit stakeholders:")

add_bullet("• SAYS (Small Business Borrower):", "'Commercial banks demand audited balance sheets and real estate collateral that our light manufacturing unit does not possess. When our loan application is declined after three weeks of scrutiny, the bank provides only a generic refusal code without explaining what went wrong or how to fix our profile.'")

add_bullet("• THINKS (Commercial Credit Underwriter):", "'I have a Priority Sector Lending quota to fulfill and genuinely want to deploy capital to expanding local businesses. However, I cannot assume unhedged default liabilities on thin-file enterprises, nor can our credit committee spend 20 hours auditing handwritten ledger notebooks for a ₹15 Lakh ticket loan.'")

add_bullet("• DOES (Market Reality & Systemic Impasse):", "Underwriters retreat to ultra-conservative collateral covenants; viable, profitable small enterprises are shut out of formal institutional banking and forced to borrow from informal non-institutional money lenders charging 24% to 36% annualized interest.")

add_bullet("• FEELS (Stakeholder Emotional Landscape):", "Borrowers experience profound alienation, financial anxiety, and systemic distrust toward the commercial banking bureaucracy. Loan officers feel overburdened by manual verification overhead and fear regulatory censure for mounting Non-Performing Assets (NPAs).")

add_bullet("• SOLUTION (AI-Based MSME Credit Risk Assistant):", "Our platform resolves this institutional impasse by automating ratio evaluation in sub-second latency, explaining risk mathematically via SHAP, establishing an independent 5-Pillar Financial Health Index, and empowering borrowers with an interactive What-If simulator to proactively plan creditworthiness improvements.")

doc.add_page_break()
add_heading1("ANNEXURE D: PROJECT TRACKER & MILESTONE EXECUTION RECORD")

add_body("Official weekly meeting logs, technical reviews, and milestone sign-offs conducted under the supervision of project guide Prof. Ruchira Tare:")

t_track = doc.add_table(rows=1, cols=4)
style_table(t_track, [1.0, 1.4, 3.2, 1.0], ["Week / Date", "Stage / Milestone", "Technical Deliverable & Activity Reviewed", "Remarks / Sign-off"], [
    ["W1-W2 (Jul)", "Topic Selection", "Problem identification, MSME credit gap analysis, approval of project title", "Approved by Guide"],
    ["W3-W4 (Aug)", "Literature Survey", "Detailed review of base paper (Bussmann et al., 2021) and SMOTE/SHAP studies", "Approved by Guide"],
    ["W5-W8 (Sep)", "Pipeline Design", "Synthetic MSME dataset generator, ratio engineering, zero-leakage pipeline", "Approved by Guide"],
    ["W9-W14 (Oct)", "Model Training", "Stratified 5-Fold CV, SMOTE/ADASYN comparison, champion model selection", "Approved by Guide"],
    ["W15-W18 (Nov)", "XAI & Simulation", "Implementation of SHAP Linear/Tree explainers, 5-pillar health scoring, What-If", "Approved by Guide"],
    ["W19-W22 (Dec)", "UI & Persistence", "Streamlit dashboard development, SQLite database schema, PDF report generator", "Approved by Guide"],
    ["W23-W24 (Jan)", "Testing & Report", "PyTest 7 test suites, draft project report compilation, final viva rehearsal", "Approved by Guide"]
])

# ==============================================================================
# OFFICIAL ITHENTICATE PLAGIARISM & INTEGRITY OVERVIEW CERTIFICATE
# ==============================================================================
doc.add_page_break()
add_heading1("OFFICIAL ITHENTICATE PLAGIARISM & INTEGRITY CERTIFICATE")

ITHENTICATE_IMG = '/Users/avinashsharma/msme_credit_risk_assistant/assets/ithenticate_plagiarism_report.png'
if os.path.exists(ITHENTICATE_IMG):
    p_ith = doc.add_paragraph()
    p_ith.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ith.paragraph_format.space_before = Pt(8)
    p_ith.paragraph_format.space_after = Pt(8)
    r_ith = p_ith.add_run()
    r_ith.add_picture(ITHENTICATE_IMG, width=Inches(5.4))
    
    cap_ith = doc.add_paragraph()
    cap_ith.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cith = cap_ith.add_run("Official iThenticate Integrity Overview Certificate (Submission ID: trn:oid:::3117342624807 - 7% Overall Similarity)")
    r_cith.font.name = 'Times New Roman'
    r_cith.font.size = Pt(10)
    r_cith.font.bold = True

# Save Document to Project Folder and Desktop
print("Saving generated DOCX files...")
doc.save(DOCX_PROJECT)
doc.save(DOCX_DESKTOP)
print(f"1. Saved DOCX to: {DOCX_PROJECT}")
print(f"2. Saved DOCX to: {DOCX_DESKTOP}")

# Export to PDF via AppleScript & Apple Pages
print("Exporting DOCX to PDF via Apple Pages...")
import subprocess

applescript = f'''
set docxPath to POSIX file "{DOCX_PROJECT}"
set pdfPath to POSIX file "{PDF_PROJECT}"
tell application "Pages"
    set myDoc to open docxPath
    export myDoc to file pdfPath as PDF
    close myDoc saving no
end tell
'''

res = subprocess.run(["osascript", "-e", applescript], capture_output=True, text=True)
if res.returncode == 0:
    print(f"Successfully exported raw PDF to: {PDF_PROJECT}")
    
    # Stamp official double-line page border on EVERY page of the PDF
    print("Stamping formal academic double-line borders onto every page of the PDF...")
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    import pypdf
    import shutil

    w, h = A4 # 595.27, 841.89
    BORDER_OVERLAY = '/tmp/master_border_overlay.pdf'
    c_b = canvas.Canvas(BORDER_OVERLAY, pagesize=A4)
    c_b.setStrokeColorRGB(0.0, 0.0, 0.0)
    c_b.setLineWidth(1.5)
    c_b.rect(20, 20, w - 40, h - 40)
    c_b.setLineWidth(0.5)
    c_b.rect(23.5, 23.5, w - 47, h - 47)
    c_b.save()

    reader_raw = pypdf.PdfReader(PDF_PROJECT)
    reader_b = pypdf.PdfReader(BORDER_OVERLAY)
    b_page = reader_b.pages[0]

    writer_b = pypdf.PdfWriter()
    for page in reader_raw.pages:
        page.merge_page(b_page)
        writer_b.add_page(page)

    with open(PDF_PROJECT, 'wb') as f_out:
        writer_b.write(f_out)

    # Copy bordered PDF to Desktop
    shutil.copyfile(PDF_PROJECT, PDF_DESKTOP)
    print(f"Successfully stamped formal borders and saved to Desktop: {PDF_DESKTOP}")
else:
    print(f"Pages PDF export notice: {res.stderr}")

# Word & Page Count Verification
import re
words = sum(len(p.text.split()) for p in doc.paragraphs)
for t in doc.tables:
    for row in t.rows:
        for cell in row.cells:
            words += sum(len(p.text.split()) for p in cell.paragraphs)

print(f"Total Words in Document: {words}")
if os.path.exists(PDF_PROJECT):
    with open(PDF_PROJECT, 'rb') as f:
        pdf_bytes = f.read()
    page_count = len(re.findall(rb'/Type\s*/Page[^s]', pdf_bytes))
    print(f"Official Counted Pages in Exported PDF: {page_count}")
