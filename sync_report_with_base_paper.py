with open('/Users/avinashsharma/msme_credit_risk_assistant/generate_expanded_final_report.py', 'r') as f:
    text = f.read()

# 1. Update Chapter 3 item 1
old_item1 = '''add_body("1. Bussmann et al. (2021) [Primary Base Paper]: In 'Explainable Machine Learning in Credit Risk Management' (Computational Economics), the authors investigated the tension between the predictive prowess of machine learning ensembles and regulatory transparency mandates. Analyzing a proprietary dataset of European small and medium enterprises, they demonstrated that Shapley Additive explanations (TreeSHAP) could decompose complex gradient-boosted trees and random forest predictions into exact feature attributions, satisfying supervisory explainability guidelines. However, their research remained strictly an offline analytical study, omitting interactive software implementations, real-time counterfactual simulations, or automated borrower remediation guidance.")'''

new_item1 = '''add_body("1. Yadav et al. (2026) [Primary Base Paper]: In 'Explainable Alternative Credit Scoring For Thin-File MSMEs Via Multi-Source Behavioral Data Fusion And XGBoost' (International Journal of Artificial Intelligence and Machine Learning, IJAIML, SvedbergOpen, vol. 6, no. 6s, pp. 995–1010, DOI: 10.51483/IJAIML.6.6s.2026.995-1010), Dr. Sita Yadav, Dr. Santwana Gudadhe, Dr. Pallavi Adke, Dr. Vishwas Kalunge, and Dr. Khushal Khairnar investigated alternative credit scoring for thin-file MSMEs by fusing US Small Business Administration (SBA) loan datasets with application records and credit bureau histories. Using SMOTE on training data and benchmarking baseline Logistic Regression against XGBoost, their model achieved an AUC of 0.9646 and an F1-score of 0.9115, using TreeSHAP to isolate critical delinquency drivers and exposing scoring via a REST API. However, their architecture operated as an offline, binary default scoring tool without interactive counterfactual scenario modeling, independent multi-pillar operational health scoring, or borrower-facing turnaround guidance.")

add_body("2. Bussmann et al. (2021): In 'Explainable Machine Learning in Credit Risk Management' (Computational Economics), the authors investigated the tension between the predictive prowess of machine learning ensembles and regulatory transparency mandates. Analyzing a proprietary dataset of European small and medium enterprises, they demonstrated that TreeSHAP could decompose complex gradient-boosted trees and random forest predictions into exact feature attributions, satisfying supervisory explainability guidelines.")'''

text = text.replace(old_item1, new_item1)

# 2. Update Table 3.1 row 1
old_row1 = '''    ["Bussmann et al. (2021)", "Shapley Values (SHAP) + XGBoost on European SMEs", "SHAP uncovers non-linear risk drivers; meets supervisory transparency guidelines.", "Transformed offline study into real-time interactive web app with What-If counterfactuals."],'''

new_row1 = '''    ["Yadav et al. (2026) [Primary Base Paper]", "Multi-Source Data Fusion + XGBoost + SMOTE + SHAP on SBA MSME loans", "AUC of 0.9646 and F1 of 0.9115; identified delinquency ratios as key default drivers via TreeSHAP.", "Evolved binary static REST scoring into closed-loop PREDICT-EXPLAIN-SIMULATE-IMPROVE with 5-pillar health score & What-If engine."],
    ["Bussmann et al. (2021)", "Shapley Values (SHAP) + Tree Ensembles on European SMEs", "SHAP uncovers non-linear risk drivers; meets supervisory transparency guidelines.", "Operationalized real-time interactive web app with local/global XAI and scenario simulation."],'''

text = text.replace(old_row1, new_row1)

# 3. Update Bibliography reference [1]
old_ref1 = '''    "[1] N. Bussmann, P. Giudici, D. Marinelli, and J. Papenbrock, “Explainable Machine Learning in Credit Risk Management,” Computational Economics, vol. 57, no. 1, pp. 203–216, Jan. 2021, doi: 10.1007/s10614-020-10042-0.",'''

new_ref1 = '''    "[1] S. Yadav, S. Gudadhe, P. Adke, V. Kalunge, and K. Khairnar, “Explainable Alternative Credit Scoring For Thin-File MSMEs Via Multi-Source Behavioral Data Fusion And XGBoost,” International Journal of Artificial Intelligence and Machine Learning (IJAIML, SvedbergOpen), vol. 6, no. 6s, pp. 995–1010, Jun. 2026, doi: 10.51483/IJAIML.6.6s.2026.995-1010.",
    "[2] N. Bussmann, P. Giudici, D. Marinelli, and J. Papenbrock, “Explainable Machine Learning in Credit Risk Management,” Computational Economics, vol. 57, no. 1, pp. 203–216, Jan. 2021, doi: 10.1007/s10614-020-10042-0.",'''

text = text.replace(old_ref1, new_ref1)

with open('/Users/avinashsharma/msme_credit_risk_assistant/generate_expanded_final_report.py', 'w') as f:
    f.write(text)

print("Synchronized dissertation report with primary base paper Yadav et al. (2026)!")
