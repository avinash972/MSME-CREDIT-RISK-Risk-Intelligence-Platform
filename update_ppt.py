import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
import os
import shutil

SRC_PPT = '/Users/avinashsharma/Downloads/MSME_Credit_Risk_Assistant_Final_Submission.pptx'
DEST_PROJ = '/Users/avinashsharma/msme_credit_risk_assistant/MSME_Credit_Risk_Assistant_Presentation.pptx'
DEST_DESK = '/Users/avinashsharma/Desktop/MSME_Credit_Risk_Assistant_Presentation.pptx'
DEST_DOWN = '/Users/avinashsharma/Downloads/MSME_Credit_Risk_Assistant_Final_Submission.pptx'

prs = pptx.Presentation(SRC_PPT)

COLOR_TITLE = RGBColor(0x20, 0x2F, 0x43) # Deep Navy
COLOR_BODY = RGBColor(0x2A, 0x31, 0x3A)  # Charcoal Text
COLOR_WHITE = RGBColor(0xFF, 0xFF, 0xFF)

def populate_bullet_points(text_frame, items, font_size=12.4, line_spacing=1.15, space_after=6):
    text_frame.clear()
    for i, (prefix, text) in enumerate(items):
        p = text_frame.add_paragraph() if i > 0 else text_frame.paragraphs[0]
        p.line_spacing = line_spacing
        p.space_after = Pt(space_after)
        
        # Bold bullet prefix
        r_pre = p.add_run()
        r_pre.text = f"•  {prefix}: "
        r_pre.font.name = 'Aptos'
        r_pre.font.size = Pt(font_size)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_TITLE
        
        # Regular body text
        r_body = p.add_run()
        r_body.text = text
        r_body.font.name = 'Aptos'
        r_body.font.size = Pt(font_size)
        r_body.font.bold = False
        r_body.font.color.rgb = COLOR_BODY

# ==============================================================================
# SLIDE 6: LITERATURE REVIEW
# ==============================================================================
slide6 = prs.slides[5]
tf6 = slide6.shapes[5].text_frame
items_s6 = [
    ("Base-Paper Focus (Yadav et al., June 2026)",
     "Dr. Sita Yadav, Dr. Santwana Gudadhe et al. (IJAIML, SvedbergOpen) investigated explainable alternative credit scoring for thin-file MSMEs by fusing US SBA loan data, application records, and credit bureau histories."),
    ("Modelling Approach in Base Paper",
     "Logistic Regression was benchmarked against XGBoost as the advanced model. SMOTE was applied strictly to training data to address default class imbalance, reporting an empirical AUC of 0.9646 and an F1-score of 0.9115."),
    ("Explainability & API Delivery",
     "SHAP (TreeSHAP) was utilized to interpret important default risk drivers (e.g., delinquency ratios, credit history length), and the scoring model was exposed via a REST-based API for software integration."),
    ("Foundational XAI & Scoring Literature",
     "Synthesizes Bussmann et al. (2021) for XAI supervisory compliance, Chawla et al. (2002) for SMOTE resampling, Ciampi et al. (2020) for financial ratio engineering, and Lundberg & Lee (2017) for cooperative game theory (SHAP)."),
    ("Our Extended Implementation Setting",
     "Our prototype evaluates candidate models across 1,500 MSME records, selecting regularized Logistic Regression (CV F1: 0.8671, Test Acc: 86.33%, ROC-AUC: 0.9680) due to smooth financial ratio geometry, with zero data leakage."),
    ("Core Paradigm Shift",
     "While Yadav et al. emphasize an offline, binary prediction model, our work transitions from a static score to an active, closed-loop PREDICT → EXPLAIN → SIMULATE → IMPROVE decision-support ecosystem.")
]
populate_bullet_points(tf6, items_s6, font_size=12.2, space_after=4)

# ==============================================================================
# SLIDE 7: BASE PAPER VS OUR PROJECT
# ==============================================================================
slide7 = prs.slides[6]

# Left Box: BASE PAPER (Yadav et al., 2026)
tf7_left = slide7.shapes[2].text_frame
tf7_left.clear()
p0_l = tf7_left.paragraphs[0]
r0_l = p0_l.add_run()
r0_l.text = "BASE PAPER (Yadav et al., 2026)\n"
r0_l.font.name = 'Aptos'
r0_l.font.size = Pt(16.0)
r0_l.font.bold = True
r0_l.font.color.rgb = COLOR_TITLE

items_s7_left = [
    ("Data sources", "Fuses historical US SBA loan, application, and credit-history datasets to assess thin-file MSMEs."),
    ("Task & models", "Binary default classification (0 or 1); trains an advanced XGBoost model vs. baseline Logistic Regression."),
    ("Class imbalance", "Applies SMOTE to training data; reported empirical setup achieves AUC 0.9646 and F1 0.9115."),
    ("Explainability & delivery", "Applies TreeSHAP to identify risk drivers; deploys scoring capability through a basic REST API."),
    ("Workflow model", "One-way static scoring: loan application → binary risk score + feature attribution.")
]
for prefix, text in items_s7_left:
    p = tf7_left.add_paragraph()
    p.line_spacing = 1.15
    p.space_after = Pt(4)
    r_pre = p.add_run()
    r_pre.text = f"•  {prefix}: "
    r_pre.font.name = 'Aptos'
    r_pre.font.size = Pt(12.5)
    r_pre.font.bold = True
    r_pre.font.color.rgb = COLOR_TITLE
    r_body = p.add_run()
    r_body.text = text
    r_body.font.name = 'Aptos'
    r_body.font.size = Pt(12.5)
    r_body.font.bold = False
    r_body.font.color.rgb = COLOR_BODY

# Right Box: OUR MSME CREDIT RISK ASSISTANT
tf7_right = slide7.shapes[3].text_frame
tf7_right.clear()
p0_r = tf7_right.paragraphs[0]
r0_r = p0_r.add_run()
r0_r.text = "OUR MSME CREDIT RISK ASSISTANT\n"
r0_r.font.name = 'Aptos'
r0_r.font.size = Pt(16.0)
r0_r.font.bold = True
r0_r.font.color.rgb = COLOR_TITLE

items_s7_right = [
    ("Data & model", "1,500 MSME records; selects regularized Logistic Regression (Test Acc: 86.33%, F1: 0.8344, ROC-AUC: 0.9680)."),
    ("Multi-class risk", "Granular LOW, MEDIUM, and HIGH risk tiers with calibrated probabilities (0 defaults missed)."),
    ("Financial-health tools", "Adds a decoupled deterministic 5-Pillar Financial Health Index (0–100) across Debt, Liquidity, Margins, Repayment, Stability."),
    ("Scenario simulation", "Features an interactive What-If simulation engine for dynamic parameter tuning without retraining."),
    ("Enterprise delivery", "Full 9-module Streamlit UI, ACID-compliant 3NF SQLite database, and automated ReportLab PDF audit reports.")
]
for prefix, text in items_s7_right:
    p = tf7_right.add_paragraph()
    p.line_spacing = 1.15
    p.space_after = Pt(4)
    r_pre = p.add_run()
    r_pre.text = f"•  {prefix}: "
    r_pre.font.name = 'Aptos'
    r_pre.font.size = Pt(12.5)
    r_pre.font.bold = True
    r_pre.font.color.rgb = COLOR_TITLE
    r_body = p.add_run()
    r_body.text = text
    r_body.font.name = 'Aptos'
    r_body.font.size = Pt(12.5)
    r_body.font.bold = False
    r_body.font.color.rgb = COLOR_BODY

# Bottom Banner: KEY DIFFERENCE
tf7_banner = slide7.shapes[4].text_frame
tf7_banner.clear()
p_b = tf7_banner.paragraphs[0]
r_bp = p_b.add_run()
r_bp.text = "KEY ARCHITECTURAL DIFFERENCE: "
r_bp.font.name = 'Aptos'
r_bp.font.size = Pt(11.5)
r_bp.font.bold = True
r_bp.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
r_bb = p_b.add_run()
r_bb.text = "Yadav et al. provide a static binary credit score via REST API; our system operationalizes an interactive closed-loop (PREDICT → EXPLAIN → SIMULATE → IMPROVE) empowering borrowers with actionable turnaround guidance."
r_bb.font.name = 'Aptos'
r_bb.font.size = Pt(10.5)
r_bb.font.bold = False
r_bb.font.color.rgb = COLOR_BODY

# ==============================================================================
# SLIDE 8: EXISTING SYSTEM & RESEARCH GAP
# ==============================================================================
slide8 = prs.slides[7]
tf8 = slide8.shapes[5].text_frame
items_s8 = [
    ("Existing System Approach",
     "Traditional banking relies on physical collateral and audited balance sheets, excluding thin-file MSMEs. Academic models (like Yadav et al., 2026) introduce alternative data fusion and SHAP, but operate primarily as offline, binary classifiers."),
    ("Gap 1 — Binary vs. Multi-Tier Risk Stratification",
     "Existing models provide blunt binary default predictions (0/1). Real-world commercial lending requires multi-class stratification (Low, Medium, High) to price risk premiums and determine loan covenants."),
    ("Gap 2 — Absence of Counterfactual Sensitivity Analysis",
     "The base paper offers static explanations but lacks interactive scenario simulation: rejected borrowers cannot see what financial adjustments (e.g., debt reduction, revenue growth) would make them creditworthy."),
    ("Gap 3 — Lack of an Independent Financial Health Benchmark",
     "Existing systems conflate empirical default probability with fundamental accounting health, lacking an objective, deterministic 5-pillar operational score."),
    ("Gap 4 — Enterprise Workflow & Reporting Disconnect",
     "Prior systems lack an end-to-end institutional platform combining real-time UI parameter tuning, high-throughput batch evaluation (270k+ rows), SQLite persistence, and audit-ready PDF generation."),
    ("How Our Prototype Bridges the Gap",
     "We synthesize multi-class ML, game-theoretic SHAP, a 5-pillar health score, and an interactive What-If simulator into a production-grade, zero-leakage Streamlit decision-support platform.")
]
populate_bullet_points(tf8, items_s8, font_size=12.2, space_after=4)

# ==============================================================================
# SLIDE 9: PROPOSED SYSTEM
# ==============================================================================
slide9 = prs.slides[8]
tf9 = slide9.shapes[5].text_frame
items_s9 = [
    ("End-to-End Closed-Loop Paradigm",
     "Operates on the PREDICT → EXPLAIN → SIMULATE → IMPROVE workflow, transforming credit assessment from an opaque, terminal rejection into a transparent, actionable financial roadmap."),
    ("1. PREDICT — Multi-Class Risk Inference",
     "Calculates 7 engineered ratios (DTI, Profit Margin, LTI, Cash Flow Coverage) with zero-division safeguards; outputs calibrated probabilities across LOW, MEDIUM, and HIGH risk tiers with 0 High Risk misclassifications into Low Risk."),
    ("2. EXPLAIN — Game-Theoretic SHAP XAI",
     "Decomposes predictions into signed Shapley attributions, isolating Risk Amplifiers (pushing toward High Risk) and Risk Mitigators (lowering risk) to satisfy RBI Fair Lending rules."),
    ("3. SIMULATE — What-If Scenario Engine",
     "Allows users to adjust financial sliders (e.g., reducing debt by ₹10 Lakh) and computes instantaneous probability and health score deltas without model retraining."),
    ("4. IMPROVE — 5-Pillar Health Scorecard",
     "Deterministic 0–100 index across Debt Management (25 pts), Liquidity (25 pts), Profitability (20 pts), Repayment (20 pts), and Stability (10 pts) with assigned letter grades and turnaround tips."),
    ("Record & Institutional Reporting",
     "Full SQLite 3NF relational database schema for audit tracking and dynamic, multi-page ReportLab PDF report generation for credit committees.")
]
populate_bullet_points(tf9, items_s9, font_size=12.0, space_after=3)

# ==============================================================================
# SLIDE 20: REFERENCES
# ==============================================================================
slide20 = prs.slides[19]
tf20 = slide20.shapes[5].text_frame
items_s20 = [
    ("Primary Base Paper",
     "S. Yadav, S. Gudadhe, P. Adke, V. Kalunge, and K. Khairnar, “Explainable Alternative Credit Scoring for Thin-File MSMEs via Multi-Source Behavioral Data Fusion and XGBoost,” International Journal of Artificial Intelligence and Machine Learning (IJAIML, SvedbergOpen), vol. 6, no. 6s, pp. 995–1010, June 2026. DOI: 10.51483/IJAIML.6.6s.2026.995-1010."),
    ("Explainable AI in Banking",
     "N. Bussmann, P. Giudici, D. Marinelli, and J. Papenbrock, “Explainable Machine Learning in Credit Risk Management,” Computational Economics, vol. 57, no. 1, pp. 203–216, 2021."),
    ("Class-Imbalance Resampling",
     "N. V. Chawla, K. W. Bowyer, L. O. Hall, and W. P. Kegelmeyer, “SMOTE: Synthetic Minority Over-sampling Technique,” Journal of Artificial Intelligence Research, vol. 16, pp. 321–357, 2002."),
    ("Game-Theoretic SHAP Foundation",
     "S. M. Lundberg and S.-I. Lee, “A Unified Approach to Interpreting Model Predictions,” Advances in Neural Information Processing Systems (NeurIPS), vol. 30, pp. 4765–4774, 2017."),
    ("Project Implementation & Scoping",
     "The prototype’s evaluation metrics, workflow, and feature descriptions refer to our software implementation. Candidate models were evaluated across Stratified 5-Fold Cross-Validation, establishing zero-leakage empirical benchmarks.")
]
populate_bullet_points(tf20, items_s20, font_size=12.2, space_after=4)

# Save to all destination locations
prs.save(DEST_DOWN)
prs.save(DEST_PROJ)
prs.save(DEST_DESK)

print("Successfully updated PPT slides 6, 7, 8, 9, and 20!")
print(f"1. Saved to Downloads: {DEST_DOWN}")
print(f"2. Saved to Project Workspace: {DEST_PROJ}")
print(f"3. Saved to Desktop: {DEST_DESK}")
