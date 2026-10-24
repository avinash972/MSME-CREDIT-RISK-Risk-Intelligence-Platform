import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

os.makedirs('/Users/avinashsharma/msme_credit_risk_assistant/assets/diagrams', exist_ok=True)
IMG_DIR = '/Users/avinashsharma/msme_credit_risk_assistant/assets/diagrams'

plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# ==============================================================================
# DIAGRAM 1: Proposed Paradigm (Predict -> Explain -> Simulate -> Improve)
# ==============================================================================
fig, ax = plt.subplots(figsize=(8, 6.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Background container
bg = patches.FancyBboxPatch((0.2, 0.2), 9.6, 9.6, boxstyle="round,pad=0.2,rounding_size=0.3",
                           facecolor="#f8fafc", edgecolor="#cbd5e1", linewidth=1.5)
ax.add_patch(bg)

# Title
ax.text(5, 9.3, "CORE SYSTEM PARADIGM", fontsize=15, fontweight='bold', color="#0f172a", ha='center')
ax.text(5, 8.85, "Continuous Credit Assessment & Improvement Loop", fontsize=10, color="#64748b", ha='center')

steps = [
    ("1. PREDICT", "#1e3a8a", "#dbeafe", "Multi-Class Credit Risk", "LOW | MEDIUM | HIGH Tiers\nCalibrated Class Probabilities", 7.0),
    ("2. EXPLAIN", "#065f46", "#d1fae5", "Game-Theoretic SHAP XAI", "Directional Feature Attribution\nRisk Amplifiers vs Mitigators", 5.0),
    ("3. SIMULATE", "#b45309", "#fef3c7", "What-If Scenario Engine", "Interactive Parameter Tuning\nInstant Probability & Health Deltas", 3.0),
    ("4. IMPROVE", "#0e7490", "#cffafe", "5-Pillar Health Score (0-100)", "Debt, Liquidity, Profit, Repay, Stability\nActionable Turnaround Guidance", 1.0)
]

for title, stroke, fill, sub, desc, y in steps:
    box = patches.FancyBboxPatch((0.8, y), 8.4, 1.45, boxstyle="round,pad=0.15,rounding_size=0.2",
                                facecolor=fill, edgecolor=stroke, linewidth=2)
    ax.add_patch(box)
    ax.text(1.2, y + 0.95, title, fontsize=12, fontweight='bold', color=stroke, va='center')
    ax.text(4.2, y + 0.95, f"[{sub}]", fontsize=10, fontweight='bold', color="#334155", va='center')
    ax.text(1.2, y + 0.45, desc, fontsize=9.5, color="#1e293b", va='center')

# Arrows connecting steps
arrow_props = dict(facecolor='#64748b', edgecolor='none', width=2.5, headwidth=7)
ax.annotate('', xy=(5, 6.75), xytext=(5, 7.0), arrowprops=arrow_props)
ax.annotate('', xy=(5, 4.75), xytext=(5, 5.0), arrowprops=arrow_props)
ax.annotate('', xy=(5, 2.75), xytext=(5, 3.0), arrowprops=arrow_props)

plt.tight_layout()
plt.savefig(f"{IMG_DIR}/diag1_proposed_paradigm.png", bbox_inches='tight', dpi=300)
plt.close()
print("Generated Diagram 1: Proposed Paradigm")

# ==============================================================================
# DIAGRAM 2: System Architecture Block Diagram
# ==============================================================================
fig, ax = plt.subplots(figsize=(8.5, 6.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.6, "SYSTEM ARCHITECTURE", fontsize=14, fontweight='bold', color="#0f172a", ha='center')

layers = [
    ("PRESENTATION LAYER", "#3b82f6", "#eff6ff", 7.6, [
        ("Streamlit Web UI", 0.6, 2.6),
        ("Theme Adaptive Dark/Light", 3.4, 3.2),
        ("Plotly Gauges & Radar", 6.8, 2.6)
    ]),
    ("INFERENCE & PIPELINE ENGINE", "#10b981", "#f0fdf4", 5.2, [
        ("Feature Engineering (DTI, CF)", 0.6, 3.0),
        ("StandardScaler & Imputer", 3.8, 2.8),
        ("Calibrated Probability Engine", 6.8, 2.6)
    ]),
    ("MACHINE LEARNING & EXPLAINABILITY LAYER", "#f59e0b", "#fffbeb", 2.8, [
        ("Optimal Logistic Classifier", 0.6, 2.8),
        ("SHAP Explainer (Global/Local)", 3.6, 3.2),
        ("What-If Simulation Engine", 7.0, 2.4)
    ]),
    ("STORAGE & AUDIT LAYER", "#6366f1", "#eef2ff", 0.5, [
        ("SQLite 3 Database (3NF)", 1.2, 3.4),
        ("ReportLab Institutional PDF Engine", 5.4, 3.4)
    ])
]

for l_title, l_col, l_bg, y, boxes in layers:
    # Outer layer box
    l_box = patches.FancyBboxPatch((0.3, y), 9.4, 1.85, boxstyle="round,pad=0.1,rounding_size=0.15",
                                  facecolor=l_bg, edgecolor=l_col, linewidth=1.5)
    ax.add_patch(l_box)
    ax.text(0.5, y + 1.55, l_title, fontsize=10, fontweight='bold', color=l_col)
    
    # Inner component boxes
    for b_title, b_x, b_w in boxes:
        c_box = patches.FancyBboxPatch((b_x, y + 0.25), b_w, 1.0, boxstyle="round,pad=0.08,rounding_size=0.1",
                                      facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1.2)
        ax.add_patch(c_box)
        ax.text(b_x + b_w/2, y + 0.75, b_title, fontsize=8.5, fontweight='bold', color="#1e293b",
                ha='center', va='center', multialignment='center')

# Arrows between layers
arrow_props = dict(facecolor='#475569', edgecolor='none', width=2, headwidth=6)
ax.annotate('', xy=(5, 7.35), xytext=(5, 7.6), arrowprops=arrow_props)
ax.annotate('', xy=(5, 4.95), xytext=(5, 5.2), arrowprops=arrow_props)
ax.annotate('', xy=(5, 2.55), xytext=(5, 2.8), arrowprops=arrow_props)

plt.tight_layout()
plt.savefig(f"{IMG_DIR}/diag2_architecture.png", bbox_inches='tight', dpi=300)
plt.close()
print("Generated Diagram 2: System Architecture")

# ==============================================================================
# DIAGRAM 3: Methodology & ML Pipeline Workflow
# ==============================================================================
fig, ax = plt.subplots(figsize=(8.5, 6.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9.6, "ML PIPELINE & WORKFLOW", fontsize=14, fontweight='bold', color="#0f172a", ha='center')

steps_data = [
    ("Step 1: Data Synthesis & Ingestion", "1,500 MSME records (Log-normal revenue, expenses, debt, noise)", 8.2, "#1e3a8a", "#dbeafe"),
    ("Step 2: Financial Ratio Engineering", "DTI, Operating Profit Margin, Loan-to-Income, Cash Flow Coverage", 6.8, "#0369a1", "#e0f2fe"),
    ("Step 3: Stratified 80/20 Train-Test Split", "Train: 1,200 samples | Untouched Test: 300 samples (Zero Leakage)", 5.4, "#0f766e", "#ccfbf1"),
    ("Step 4: Imbalance Resampling inside 5-Fold CV", "Evaluate None vs SMOTE vs ADASYN strictly inside CV training folds", 4.0, "#b45309", "#fef3c7"),
    ("Step 5: Model Selection & Final Fitting", "Selected Champion: Logistic Regression (CV F1: 0.8671, Acc: 88.92%)", 2.6, "#15803d", "#dcfce7"),
    ("Step 6: Evaluation & Explainability", "Test Acc: 86.33%, ROC-AUC: 0.9680 + SHAP Local/Global + PDF Export", 1.2, "#4338ca", "#e0e7ff")
]

for title, desc, y, stroke, fill in steps_data:
    box = patches.FancyBboxPatch((0.6, y), 8.8, 1.05, boxstyle="round,pad=0.1,rounding_size=0.15",
                                facecolor=fill, edgecolor=stroke, linewidth=1.6)
    ax.add_patch(box)
    ax.text(0.9, y + 0.68, title, fontsize=10.5, fontweight='bold', color=stroke)
    ax.text(0.9, y + 0.28, desc, fontsize=8.5, color="#1e293b")

arrow_props = dict(facecolor='#475569', edgecolor='none', width=2, headwidth=5)
for y in [7.95, 6.55, 5.15, 3.75, 2.35]:
    ax.annotate('', xy=(5, y - 0.25), xytext=(5, y), arrowprops=arrow_props)

plt.tight_layout()
plt.savefig(f"{IMG_DIR}/diag3_methodology.png", bbox_inches='tight', dpi=300)
plt.close()
print("Generated Diagram 3: Methodology Workflow")

# ==============================================================================
# DIAGRAM 4: Database Entity-Relationship (ER) Design
# ==============================================================================
fig, ax = plt.subplots(figsize=(8.5, 6.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9.6, "DATABASE ENTITY-RELATIONSHIP (ER) SCHEMA", fontsize=13, fontweight='bold', color="#0f172a", ha='center')

# Entity 1: BUSINESSES
e1_box = patches.FancyBboxPatch((0.4, 5.2), 4.2, 3.8, boxstyle="round,pad=0.1,rounding_size=0.15",
                                facecolor="#eff6ff", edgecolor="#1d4ed8", linewidth=1.8)
ax.add_patch(e1_box)
ax.text(2.5, 8.6, "BUSINESSES", fontsize=11, fontweight='bold', color="#1d4ed8", ha='center')
ax.plot([0.5, 4.5], [8.3, 8.3], color="#93c5fd", linewidth=1.2)
b_fields = [
    "PK  business_id  (INTEGER)",
    "    business_name  (TEXT)",
    "    business_age  (REAL)",
    "    num_employees  (INTEGER)",
    "    created_at  (TIMESTAMP)"
]
for idx, f in enumerate(b_fields):
    fontw = 'bold' if 'PK' in f else 'normal'
    ax.text(0.7, 7.8 - idx*0.5, f, fontsize=8.5, fontweight=fontw, color="#1e293b")

# Entity 2: FINANCIAL_DATA
e2_box = patches.FancyBboxPatch((5.4, 3.8), 4.2, 5.2, boxstyle="round,pad=0.1,rounding_size=0.15",
                                facecolor="#f0fdf4", edgecolor="#15803d", linewidth=1.8)
ax.add_patch(e2_box)
ax.text(7.5, 8.6, "FINANCIAL_DATA", fontsize=11, fontweight='bold', color="#15803d", ha='center')
ax.plot([5.5, 9.5], [8.3, 8.3], color="#86efac", linewidth=1.2)
f_fields = [
    "PK  financial_id  (INTEGER)",
    "FK  business_id  (INTEGER)",
    "    annual_revenue  (REAL)",
    "    annual_expenses  (REAL)",
    "    existing_debt  (REAL)",
    "    requested_loan  (REAL)",
    "    monthly_cash_flow (REAL)",
    "    credit_history_m (INT)",
    "    previous_defaults (INT)",
    "    repayment_score  (REAL)",
    "    credit_utilization (REAL)"
]
for idx, f in enumerate(f_fields):
    fontw = 'bold' if ('PK' in f or 'FK' in f) else 'normal'
    ax.text(5.7, 7.8 - idx*0.38, f, fontsize=8, fontweight=fontw, color="#1e293b")

# Entity 3: PREDICTIONS
e3_box = patches.FancyBboxPatch((0.4, 0.4), 4.2, 4.4, boxstyle="round,pad=0.1,rounding_size=0.15",
                                facecolor="#faf5ff", edgecolor="#7e22ce", linewidth=1.8)
ax.add_patch(e3_box)
ax.text(2.5, 4.4, "PREDICTIONS", fontsize=11, fontweight='bold', color="#7e22ce", ha='center')
ax.plot([0.5, 4.5], [4.1, 4.1], color="#d8b4fe", linewidth=1.2)
p_fields = [
    "PK  prediction_id  (INTEGER)",
    "FK  business_id  (INTEGER)",
    "    risk_category  (TEXT)",
    "    probability_low  (REAL)",
    "    probability_medium (REAL)",
    "    probability_high  (REAL)",
    "    financial_health_score (REAL)",
    "    model_version  (TEXT)",
    "    raw_input_json  (TEXT)",
    "    created_at  (TIMESTAMP)"
]
for idx, f in enumerate(p_fields):
    fontw = 'bold' if ('PK' in f or 'FK' in f) else 'normal'
    ax.text(0.7, 3.7 - idx*0.35, f, fontsize=8, fontweight=fontw, color="#1e293b")

# Connectors: 1 to Many
# E1 to E2
ax.annotate("", xy=(5.4, 6.5), xytext=(4.6, 6.5),
            arrowprops=dict(arrowstyle="->", color="#1d4ed8", lw=2))
ax.text(4.7, 6.7, "1 : M", fontsize=9, fontweight='bold', color="#1d4ed8")

# E1 to E3
ax.annotate("", xy=(2.5, 4.8), xytext=(2.5, 5.2),
            arrowprops=dict(arrowstyle="->", color="#7e22ce", lw=2))
ax.text(2.7, 4.95, "1 : M", fontsize=9, fontweight='bold', color="#7e22ce")

plt.tight_layout()
plt.savefig(f"{IMG_DIR}/diag4_er_schema.png", bbox_inches='tight', dpi=300)
plt.close()
print("Generated Diagram 4: ER Schema")

# ==============================================================================
# DIAGRAM 5: Empirical Model Comparison & Confusion Matrix Visual
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 4.8), dpi=300)

# Subplot 1: Model Comparison Bar Chart
models = ['Logistic Reg\n(Selected)', 'Random Forest\n(Baseline)', 'Decision Tree\n(ADASYN)']
cv_f1 = [0.8671, 0.8094, 0.7799]
cv_acc = [0.8892, 0.8392, 0.8092]

x = np.arange(len(models))
width = 0.35

rects1 = ax1.bar(x - width/2, cv_f1, width, label='CV F1-Macro', color='#1d4ed8')
rects2 = ax1.bar(x + width/2, cv_acc, width, label='CV Accuracy', color='#60a5fa')

ax1.set_ylabel('Score (0 - 1.0)', fontsize=10, fontweight='bold')
ax1.set_title('Cross-Validation Performance', fontsize=11, fontweight='bold', color='#0f172a')
ax1.set_xticks(x)
ax1.set_xticklabels(models, fontsize=8.5)
ax1.set_ylim(0.65, 0.95)
ax1.legend(loc='lower right', fontsize=8.5)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

for rect in rects1:
    height = rect.get_height()
    ax1.annotate(f'{height:.3f}', xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=7.5, fontweight='bold')

for rect in rects2:
    height = rect.get_height()
    ax1.annotate(f'{height:.3f}', xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=7.5)

# Subplot 2: Confusion Matrix Heatmap (Test Set: N=300)
cm = np.array([
    [164,  9,  1],
    [ 17, 59,  5],
    [  0,  9, 36]
])
classes = ['LOW', 'MED', 'HIGH']

im = ax2.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
ax2.set_title('Test Set Confusion Matrix (N=300)', fontsize=11, fontweight='bold', color='#0f172a')
tick_marks = np.arange(len(classes))
ax2.set_xticks(tick_marks)
ax2.set_xticklabels(classes, fontsize=9, fontweight='bold')
ax2.set_yticks(tick_marks)
ax2.set_yticklabels(classes, fontsize=9, fontweight='bold')
ax2.set_xlabel('Predicted Label', fontsize=9.5, fontweight='bold')
ax2.set_ylabel('Actual Label', fontsize=9.5, fontweight='bold')

# Loop over data dimensions and create text annotations.
thresh = cm.max() / 2.
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax2.text(j, i, format(cm[i, j], 'd'),
                ha="center", va="center",
                color="white" if cm[i, j] > thresh else "#0f172a",
                fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig(f"{IMG_DIR}/diag5_results_visual.png", bbox_inches='tight', dpi=300)
plt.close()
print("Generated Diagram 5: Results & Confusion Matrix")
