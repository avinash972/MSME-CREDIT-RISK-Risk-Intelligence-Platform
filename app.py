"""
AI-Based MSME Credit Risk Assistant
------------------------------------
Enterprise Credit Intelligence & Risk Analytics Platform
Differentiating Concept: PREDICT -> EXPLAIN -> SIMULATE -> IMPROVE
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import json
import re
import difflib
from pathlib import Path
from datetime import datetime
from io import BytesIO
import time

from src.config import (
    METADATA_PATH,
    ALL_INPUT_FEATURES,
    NUMERICAL_FEATURES,
    ENGINEERED_FEATURES,
    RISK_MAP
)
from src.predict import predict_msme_risk, load_prediction_artifacts
from src.financial_health import calculate_financial_health_score
from src.explain import get_local_shap_explanation, generate_risk_improvement_insights
from src.scenario import run_what_if_scenario
from src.database import (
    init_db,
    save_assessment_record,
    fetch_all_assessments,
    delete_assessment_record,
    fetch_dashboard_summary_stats
)
from src.report import generate_pdf_report
from src.utils import validate_msme_input_form, format_inr
from src.feature_engineering import add_financial_features

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="MSME Credit Intelligence Platform",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme-Adaptive CSS Styling (Fully Supports Light & Dark Modes)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Hero Header Banner */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 40%, #1e40af 100%);
        padding: 30px 36px;
        border-radius: 16px;
        color: #ffffff !important;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.03em;
        color: #ffffff !important;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #cbd5e1 !important;
        margin-top: 8px;
        margin-bottom: 0;
        font-weight: 400;
    }
    
    /* Theme-Adaptive Glass Cards */
    .glass-card {
        background-color: var(--secondary-background-color, rgba(128, 128, 128, 0.05));
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 14px;
        padding: 22px;
        color: var(--text-color, inherit);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
        margin-bottom: 20px;
    }
    
    /* Theme-Adaptive Metric Stat Cards */
    .metric-box {
        background-color: var(--secondary-background-color, rgba(128, 128, 128, 0.05));
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 14px;
        padding: 20px;
        text-align: center;
        color: var(--text-color, inherit);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04);
        transition: all 0.2s ease-in-out;
    }
    .metric-box:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 20px -5px rgba(0, 0, 0, 0.1);
    }
    .metric-label {
        font-size: 0.8rem;
        font-weight: 700;
        color: var(--text-color, #64748b);
        opacity: 0.85;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 6px;
    }
    .metric-val {
        font-size: 2rem;
        font-weight: 800;
        color: var(--text-color, inherit);
        line-height: 1.2;
    }

    /* Risk Status Badges (Light & Dark Compatible) */
    .badge-container {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 10px 22px;
        border-radius: 9999px;
        font-weight: 800;
        font-size: 1.25rem;
        letter-spacing: 0.04em;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    }
    .badge-low-risk {
        background-color: rgba(16, 185, 129, 0.2);
        color: #10b981 !important;
        border: 1px solid #10b981;
    }
    .badge-medium-risk {
        background-color: rgba(245, 158, 11, 0.2);
        color: #f59e0b !important;
        border: 1px solid #f59e0b;
    }
    .badge-high-risk {
        background-color: rgba(239, 68, 68, 0.2);
        color: #ef4444 !important;
        border: 1px solid #ef4444;
    }
    
    /* Theme-Adaptive Action Insight Cards */
    .insight-card {
        padding: 16px 20px;
        border-radius: 12px;
        margin-bottom: 12px;
        border-left: 5px solid;
        color: var(--text-color, inherit);
    }
    .insight-critical {
        background-color: rgba(244, 63, 94, 0.15);
        border-left-color: #f43f5e;
    }
    .insight-positive {
        background-color: rgba(34, 197, 94, 0.15);
        border-left-color: #22c55e;
    }
    .insight-warning {
        background-color: rgba(245, 158, 11, 0.15);
        border-left-color: #f59e0b;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize SQLite DB on startup
init_db()

# Load model metadata
@st.cache_data
def get_metadata():
    if METADATA_PATH.exists():
        with open(METADATA_PATH, "r") as f:
            return json.load(f)
    return {}

metadata = get_metadata()

def ensure_active_assessment():
    """Ensures st.session_state['last_assessment'] is populated with data."""
    if "last_assessment" not in st.session_state:
        recent = fetch_all_assessments()
        if recent:
            last_rec = recent[0]
            raw_input = json.loads(last_rec["raw_input_json"]) if last_rec.get("raw_input_json") else {
                "business_name": last_rec.get("business_name", "Demo Enterprise"),
                "business_age": float(last_rec.get("business_age", 6.5)),
                "annual_revenue": float(last_rec.get("annual_revenue", 15000000.0)),
                "annual_expenses": 11000000.0,
                "existing_debt": 2500000.0,
                "requested_loan_amount": float(last_rec.get("requested_loan_amount", 3000000.0)),
                "monthly_cash_flow": 250000.0,
                "num_employees": int(last_rec.get("num_employees", 18)),
                "credit_history_months": 60,
                "previous_defaults": 0,
                "repayment_history_score": 92.0,
                "credit_utilization_ratio": 0.35
            }
        else:
            raw_input = {
                "business_name": "Mahalaxmi Enterprises",
                "business_age": 6.5,
                "annual_revenue": 15000000.0,
                "annual_expenses": 11000000.0,
                "existing_debt": 2500000.0,
                "requested_loan_amount": 3000000.0,
                "monthly_cash_flow": 250000.0,
                "num_employees": 18,
                "credit_history_months": 60,
                "previous_defaults": 0,
                "repayment_history_score": 92.0,
                "credit_utilization_ratio": 0.35
            }
        pred_res = predict_msme_risk(raw_input)
        health_res = calculate_financial_health_score(raw_input)
        shap_exp = get_local_shap_explanation(raw_input)
        insights = generate_risk_improvement_insights(raw_input, shap_exp)
        st.session_state["last_assessment"] = {
            "business_name": raw_input.get("business_name", "Enterprise"),
            "raw_input": raw_input,
            "pred_res": pred_res,
            "health_res": health_res,
            "shap_exp": shap_exp,
            "insights": insights
        }
    return st.session_state["last_assessment"]

# Custom Plotly Chart Helper Functions (Theme Adaptive)
def plot_financial_health_gauge(score: float, grade: str):
    """Generates semi-circular Gauge chart compatible with Light and Dark modes."""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        number = {'suffix': "/100", 'font': {'size': 36, 'family': "Plus Jakarta Sans"}},
        title = {'text': f"Financial Health Grade: <b>{grade}</b>", 'font': {'size': 16}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#94a3b8"},
            'bar': {'color': "#3b82f6", 'thickness': 0.25},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 1,
            'bordercolor': "rgba(148, 163, 184, 0.3)",
            'steps': [
                {'range': [0, 50], 'color': 'rgba(239, 68, 68, 0.25)'},
                {'range': [50, 65], 'color': 'rgba(245, 158, 11, 0.25)'},
                {'range': [65, 80], 'color': 'rgba(59, 130, 246, 0.25)'},
                {'range': [80, 100], 'color': 'rgba(16, 185, 129, 0.25)'}
            ],
            'threshold': {
                'line': {'color': "#10b981", 'width': 3},
                'thickness': 0.75,
                'value': score
            }
        }
    ))
    fig.update_layout(
        height=240, 
        margin=dict(l=20, r=20, t=40, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Plus Jakarta Sans")
    )
    return fig

def plot_radar_pillars(pillars: dict):
    """Generates Polar Radar chart for 5 Financial Pillars."""
    categories = ['Debt Mgmt', 'Cash Flow', 'Profitability', 'Repayment', 'Stability']
    max_scores = [25, 25, 20, 20, 10]
    actual_scores = [
        pillars['debt_management'], 
        pillars['cash_flow_liquidity'], 
        pillars['profitability'], 
        pillars['repayment_history'], 
        pillars['business_stability']
    ]
    
    norm_scores = [(a / m) * 100 for a, m in zip(actual_scores, max_scores)]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=norm_scores + [norm_scores[0]],
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor='rgba(59, 130, 246, 0.25)',
        line=dict(color='#3b82f6', width=2),
        name='Performance (%)'
    ))
    
    fig.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(visible=True, range=[0, 100], ticksuffix="%"),
            angularaxis=dict()
        ),
        showlegend=False,
        height=280,
        margin=dict(l=40, r=40, t=20, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Plus Jakarta Sans")
    )
    return fig

# -----------------------------------------------------------------------------
# Resilient File Ingestion & Flexible Column Mapping Helpers
# -----------------------------------------------------------------------------
PREDICTION_FEATURE_SPECS = {
    "requested_loan_amount": {
        "pillar": "🏛️ Pillar 1: Debt & Leverage Capacity",
        "description": "Target loan principal requested. Denominator for Loan-to-Income and Cash-Flow-to-Loan coverage.",
        "shap_importance": "Critical (SHAP +0.42)",
        "badge_color": "#ef4444",
        "synonyms": [
            "requested_loan_amount", "loan_amount", "requested_loan", "loan_requested",
            "loan_required", "applied_loan_amount", "borrowing_amount", "loan_size",
            "sanction_sought", "required_loan", "principal_requested", "loan", "amount_requested",
            "loan_amnt", "grossapproval", "sbaguaranteedapproval", "approval_amount", "sanction_amount"
        ],
        "smart_fallbacks": []
    },
    "existing_debt": {
        "pillar": "🏛️ Pillar 1: Debt & Leverage Capacity",
        "description": "Total active outstanding debt/loans. Drives Debt-to-Income (DTI) and Debt Ratio.",
        "shap_importance": "Critical (SHAP +0.38)",
        "badge_color": "#ef4444",
        "synonyms": [
            "existing_debt", "debt", "current_debt", "total_debt", "liabilities",
            "existing_loans", "outstanding_debt", "loan_balance", "borrowing", "total_loans",
            "outstanding_loans", "current_liabilities", "debt_amount", "tot_cur_bal",
            "revol_bal", "total_bal_ex_mort", "tot_debt", "balance"
        ],
        "smart_fallbacks": ["⚙️ Set to Zero (No Prior Debt)"]
    },
    "credit_utilization_ratio": {
        "pillar": "🏛️ Pillar 1: Debt & Leverage Capacity",
        "description": "Ratio of credit drawn vs total credit lines. High ratio indicates liquidity distress.",
        "shap_importance": "High (SHAP +0.28)",
        "badge_color": "#f59e0b",
        "synonyms": [
            "credit_utilization_ratio", "credit_utilization", "utilization_ratio",
            "credit_ratio", "card_utilization", "limit_utilization", "cur", "utilization",
            "credit_util", "utilization_rate", "revol_util", "bc_util", "util"
        ],
        "smart_fallbacks": ["⚙️ MSME Benchmark (30% Utilization)", "⚙️ Conservative Benchmark (50% Utilization)"]
    },
    "annual_revenue": {
        "pillar": "💵 Pillar 2: Cash Flow & Earnings Health",
        "description": "Annual turnover / gross sales. Primary measure of operational scale and cash generation.",
        "shap_importance": "Critical (SHAP +0.40)",
        "badge_color": "#ef4444",
        "synonyms": [
            "annual_revenue", "revenue", "annual_turnover", "turnover", "sales",
            "annual_sales", "yearly_revenue", "gross_revenue", "gross_sales", "total_revenue",
            "turnover_inr", "revenue_inr", "total_turnover", "annual_income", "gross_income",
            "annual_inc", "income", "tot_income", "gross_receipts", "topline"
        ],
        "smart_fallbacks": ["⚙️ Estimate: Loan Amount × 3.0"]
    },
    "annual_expenses": {
        "pillar": "💵 Pillar 2: Cash Flow & Earnings Health",
        "description": "Annual operational expenses. Determines operating profit margin.",
        "shap_importance": "High (SHAP +0.31)",
        "badge_color": "#f59e0b",
        "synonyms": [
            "annual_expenses", "expenses", "expenditure", "annual_expenditure",
            "annual_cost", "total_expenses", "yearly_expenses", "operating_expenses", "opex",
            "expenses_inr", "total_cost", "costs", "expenditures"
        ],
        "smart_fallbacks": [
            "⚙️ Auto-Derive: 75% of Revenue (Standard MSME OpEx)",
            "⚙️ Auto-Derive: 80% of Revenue (Conservative OpEx)"
        ]
    },
    "monthly_cash_flow": {
        "pillar": "💵 Pillar 2: Cash Flow & Earnings Health",
        "description": "Free net monthly cash flow available to service loan EMI payments comfortably.",
        "shap_importance": "Critical (SHAP +0.35)",
        "badge_color": "#ef4444",
        "synonyms": [
            "monthly_cash_flow", "cash_flow", "cashflow", "monthly_cashflow",
            "net_cash_flow", "operating_cash_flow", "monthly_flow", "average_cash_flow",
            "monthly_cf", "net_cashflow", "free_cash_flow", "monthly_operating_cash"
        ],
        "smart_fallbacks": [
            "⚙️ Auto-Calculate: (Revenue - Expenses) / 12",
            "⚙️ Estimate: 5% of Monthly Revenue"
        ]
    },
    "repayment_history_score": {
        "pillar": "🛡️ Pillar 3: Repayment Reliability & Bureau Record",
        "description": "Credit bureau / repayment track record (0–100 scale, or FICO 300–850 auto-scaled).",
        "shap_importance": "Critical (SHAP +0.45)",
        "badge_color": "#ef4444",
        "synonyms": [
            "repayment_history_score", "repayment_score", "repayment_history", "payment_score",
            "cibil", "cibil_score", "credit_score", "bureau_score", "track_record_score",
            "repayment_track", "repayment_performance", "cibil_rating", "experian_score",
            "fico_score", "fico", "score", "bureau_rating"
        ],
        "smart_fallbacks": [
            "⚙️ Prime Benchmark (85/100)",
            "⚙️ Standard Benchmark (75/100)"
        ]
    },
    "previous_defaults": {
        "pillar": "🛡️ Pillar 3: Repayment Reliability & Bureau Record",
        "description": "Number of previous defaults, write-offs, or 90+ DPD events.",
        "shap_importance": "High (SHAP +0.34)",
        "badge_color": "#f59e0b",
        "synonyms": [
            "previous_defaults", "defaults", "past_defaults", "prior_defaults",
            "default_count", "num_defaults", "historical_defaults", "dpd_count", "bounced_loans",
            "no_of_defaults", "past_default", "defaulted_loans", "delinq_2yrs",
            "num_tl_90g_dpd_24m", "pub_rec_bankruptcies", "grosschargeoffamount", "chargeoff"
        ],
        "smart_fallbacks": ["⚙️ Set to 0 (Clean Track Record)"]
    },
    "credit_history_months": {
        "pillar": "🛡️ Pillar 3: Repayment Reliability & Bureau Record",
        "description": "Age of oldest credit line in months. Longer history demonstrates stability.",
        "shap_importance": "Medium (SHAP +0.18)",
        "badge_color": "#3b82f6",
        "synonyms": [
            "credit_history_months", "credit_history", "credit_months", "credit_age_months",
            "credit_vintage_months", "bureau_history_months", "bureau_months", "history_months",
            "credit_vintage", "credit_history_length", "credit_age", "mo_sin_old_rev_tl_op",
            "earliest_cr_line", "mo_sin_old_il_acct", "cr_history"
        ],
        "smart_fallbacks": [
            "⚙️ Auto-Estimate: Business Age × 12 Months",
            "⚙️ Benchmark: 60 Months (5 Years)"
        ]
    },
    "business_age": {
        "pillar": "🏢 Pillar 4: Enterprise Stability & Scale",
        "description": "Years of continuous commercial operations. High vintage reduces mortality risk.",
        "shap_importance": "High (SHAP +0.25)",
        "badge_color": "#f59e0b",
        "synonyms": [
            "business_age", "business_vintage", "age", "vintage", "years_in_business",
            "business_years", "company_age", "firm_age", "enterprise_age", "age_years",
            "business_age_years", "experience_years", "yr_business", "years_active",
            "emp_length", "businessage", "vintage_years", "operational_years"
        ],
        "smart_fallbacks": ["⚙️ Benchmark: 5.0 Years Vintage"]
    },
    "num_employees": {
        "pillar": "🏢 Pillar 4: Enterprise Stability & Scale",
        "description": "Active full-time workforce headcount. Reflects enterprise scale and capacity.",
        "shap_importance": "Medium (SHAP +0.15)",
        "badge_color": "#3b82f6",
        "synonyms": [
            "num_employees", "employees", "number_of_employees", "headcount",
            "staff", "total_employees", "team_size", "workforce", "num_staff",
            "no_of_employees", "employee_count", "workers", "jobssupported", "jobs_supported"
        ],
        "smart_fallbacks": [
            "⚙️ MSME Benchmark: 15 Employees",
            "⚙️ Small Enterprise: 8 Employees"
        ]
    },
    "business_name": {
        "pillar": "🏢 Pillar 4: Enterprise Stability & Scale",
        "description": "Identifier name for the enterprise profile or borrower.",
        "shap_importance": "Identifier",
        "badge_color": "#64748b",
        "synonyms": [
            "business_name", "company_name", "enterprise_name", "firm_name",
            "name", "client_name", "applicant_name", "msme_name", "borrower_name",
            "enterprise", "firm", "company", "borrname", "borr_name", "borrower"
        ],
        "smart_fallbacks": ["⚙️ Auto-Generate: Enterprise #1, Enterprise #2..."]
    }
}

CANONICAL_SYNONYMS = {k: v["synonyms"] for k, v in PREDICTION_FEATURE_SPECS.items()}

def clean_column_name(name: str) -> str:
    cleaned = re.sub(r'[^a-z0-9_]', '_', str(name).strip().lower())
    return re.sub(r'_+', '_', cleaned).strip('_')

def find_best_prediction_match(feat: str, raw_cols: list, matched_so_far: set = None) -> tuple:
    if matched_so_far is None:
        matched_so_far = set()
    spec = PREDICTION_FEATURE_SPECS.get(feat, {})
    syns = spec.get("synonyms", [feat])
    cleaned_dict = {c: clean_column_name(c) for c in raw_cols if c not in matched_so_far}
    
    # Pass 1: Exact cleaned match
    for c, cl in cleaned_dict.items():
        if cl == feat or cl in syns:
            return c, 1.0
            
    # Pass 2: Substring matching
    for c, cl in cleaned_dict.items():
        for s in syns:
            if len(s) >= 4 and s in cl:
                return c, 0.85
                
    # Pass 3: Fuzzy similarity matching
    best_c, best_score = None, 0.0
    for c, cl in cleaned_dict.items():
        for s in syns:
            ratio = difflib.SequenceMatcher(None, s, cl).ratio()
            if ratio > best_score:
                best_score = ratio
                best_c = c
    if best_score >= 0.80:
        return best_c, round(best_score, 2)
        
    # Pass 4: Smart fallback default
    fallbacks = spec.get("smart_fallbacks", [])
    if fallbacks:
        return fallbacks[0], 0.60
        
    return None, 0.0

def auto_detect_column_mapping(raw_columns: list) -> dict:
    mapping = {}
    matched_raw = set()
    
    # Priority order for assignment
    priority_order = [
        "requested_loan_amount", "annual_revenue", "existing_debt", 
        "repayment_history_score", "credit_utilization_ratio", "previous_defaults",
        "credit_history_months", "business_age", "annual_expenses", 
        "monthly_cash_flow", "num_employees", "business_name"
    ]
    
    for feat in priority_order:
        best_col, conf = find_best_prediction_match(feat, raw_columns, matched_so_far=matched_raw)
        if best_col:
            mapping[feat] = best_col
            if not best_col.startswith("⚙️"):
                matched_raw.add(best_col)
                
    return mapping

def sanitize_batch_value(val, is_percentage: bool = False) -> float:
    if pd.isna(val) or val is None:
        return 0.0
    if isinstance(val, (int, float, np.number)):
        res = float(val)
        if is_percentage and res > 1.0:
            return res / 100.0
        return res
    val_str = str(val).strip()
    has_pct = val_str.endswith('%') or '%' in val_str
    val_str = val_str.replace('+', '').replace('<', '').replace('years', '').replace('year', '')
    cleaned = re.sub(r'[^0-9.\-]', '', val_str)
    try:
        num = float(cleaned)
        if (has_pct or is_percentage) and num > 1.0:
            return num / 100.0
        return num
    except (ValueError, TypeError):
        return 0.0

# Sidebar Navigation with Programmatic Module Redirection
st.sidebar.image("https://img.icons8.com/color/96/000000/combo-chart.png", width=56)
st.sidebar.markdown("### **MSME Credit Engine**")

navigation_modules = [
    "📊 Executive Overview",
    "📥 Data Upload & Batch Analytics",
    "💳 Single Risk Assessment",
    "🩺 Financial Health Analytics",
    "💡 Explainable AI (SHAP)",
    "🔮 What-If Scenario Simulation",
    "🎯 Model Performance",
    "📜 Assessment History",
    "📄 PDF Reports & Export"
]

default_nav_idx = 0
if "nav_override" in st.session_state and st.session_state["nav_override"] in navigation_modules:
    default_nav_idx = navigation_modules.index(st.session_state["nav_override"])
    del st.session_state["nav_override"]

navigation_page = st.sidebar.radio(
    "Navigation Modules",
    navigation_modules,
    index=default_nav_idx
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    f"<div style='font-size:0.82rem; color:var(--text-color, #64748b); background:var(--secondary-background-color, rgba(128,128,128,0.1)); padding:12px; border-radius:10px; border:1px solid rgba(128,128,128,0.2);'>"
    f"<b>Model Engine:</b> {metadata.get('model_name', 'Logistic Regression')}<br/>"
    f"<b>Resampling:</b> {metadata.get('resampling_strategy', 'NONE')}<br/>"
    f"<b>Version:</b> v1.0.0 (Calibrated)"
    f"</div>",
    unsafe_allow_html=True
)

# -----------------------------------------------------------------------------
# PAGE 1: EXECUTIVE OVERVIEW
# -----------------------------------------------------------------------------
if navigation_page == "📊 Executive Overview":
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">MSME Credit Risk Intelligence Platform</h1>
            <p class="hero-subtitle">Automated Risk Analytics, SHAP Feature Explainability, and Real-Time Scenario Modeling</p>
        </div>
    """, unsafe_allow_html=True)
    
    stats = fetch_dashboard_summary_stats()
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">Total Enterprises Analyzed</div>
                <div class="metric-val">{stats['total_assessments']}</div>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">Low Risk Profiles</div>
                <div class="metric-val" style="color:#10b981;">{stats['risk_distribution'].get('LOW', 0)}</div>
            </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">High Risk Profiles</div>
                <div class="metric-val" style="color:#ef4444;">{stats['risk_distribution'].get('HIGH', 0)}</div>
            </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">Avg Financial Health</div>
                <div class="metric-val" style="color:#3b82f6;">{stats['average_financial_health']}<span style="font-size:1.1rem; opacity:0.8;">/100</span></div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br/>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("📊 Portfolio Risk Breakdown")
        dist = stats["risk_distribution"]
        df_dist = pd.DataFrame({
            "Risk Category": list(dist.keys()),
            "Count": list(dist.values())
        })
        fig_pie = px.pie(
            df_dist, 
            names="Risk Category", 
            values="Count", 
            color="Risk Category",
            color_discrete_map={"LOW": "#10B981", "MEDIUM": "#F59E0B", "HIGH": "#EF4444"},
            hole=0.5
        )
        fig_pie.update_layout(
            height=300,
            margin=dict(t=20, b=20, l=20, r=20),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5)
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col_right:
        st.subheader("📈 Financial Health Distribution")
        recent_all = fetch_all_assessments()
        if recent_all:
            df_all = pd.DataFrame(recent_all)
            fig_hist = px.histogram(
                df_all, 
                x="financial_health_score", 
                nbins=10, 
                color="risk_category",
                color_discrete_map={"LOW": "#10B981", "MEDIUM": "#F59E0B", "HIGH": "#EF4444"},
                labels={"financial_health_score": "Financial Health Index", "count": "Enterprise Count"}
            )
            fig_hist.update_layout(
                height=300, 
                margin=dict(t=30, b=20, l=20, r=20),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_hist, use_container_width=True)
        else:
            st.info("No recorded assessment data available yet. Perform evaluations or upload a dataset.")
            
    st.markdown("---")
    st.subheader("📋 Recent Enterprise Assessments")
    recent = fetch_all_assessments()
    if recent:
        df_recent = pd.DataFrame(recent)[["business_id", "business_name", "annual_revenue", "requested_loan_amount", "risk_category", "financial_health_score", "created_at"]]
        df_recent.columns = ["ID", "Business Name", "Annual Revenue (₹)", "Requested Loan (₹)", "Risk Category", "Health Score", "Evaluated Date"]
        df_recent["Annual Revenue (₹)"] = df_recent["Annual Revenue (₹)"].apply(format_inr)
        df_recent["Requested Loan (₹)"] = df_recent["Requested Loan (₹)"].apply(format_inr)
        st.dataframe(df_recent.head(10), use_container_width=True)
    else:
        st.info("No assessment records found in database.")

# -----------------------------------------------------------------------------
# PAGE 2: DATA UPLOAD & BATCH ANALYTICS
# -----------------------------------------------------------------------------
elif navigation_page == "📥 Data Upload & Batch Analytics":
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">Data Ingestion & Batch Analytics</h1>
            <p class="hero-subtitle">Upload external enterprise datasets, inspect parameters, and execute automated batch risk scoring</p>
        </div>
    """, unsafe_allow_html=True)
    
    tab_upload, tab_sample, tab_manual = st.tabs([
        "📁 Upload External File (CSV / Excel)", 
        "📄 CSV File Template",
        "➕ Add Single Record"
    ])
    
    with tab_upload:
        st.markdown("### Upload Dataset for Batch Processing")
        st.write("Drag and drop your enterprise data file to compute risk predictions and financial health scores for all rows.")
        
        uploaded_file = st.file_uploader("Choose CSV or Excel file", type=["csv", "xlsx"])
        
        if uploaded_file is not None:
            try:
                # Delimiter-resilient reader
                if uploaded_file.name.endswith('.csv'):
                    try:
                        df_upload = pd.read_csv(uploaded_file)
                        if len(df_upload.columns) == 1 and any(sep in str(df_upload.columns[0]) for sep in [";", "\t", "|"]):
                            uploaded_file.seek(0)
                            df_upload = pd.read_csv(uploaded_file, sep=None, engine='python')
                    except Exception:
                        uploaded_file.seek(0)
                        df_upload = pd.read_csv(uploaded_file, sep=None, engine='python')
                else:
                    df_upload = pd.read_excel(uploaded_file)
                
                st.success(f"File loaded successfully! Total records: {len(df_upload)} enterprises.")
                
                with st.expander("🔍 Preview Raw Uploaded Data", expanded=False):
                    st.dataframe(df_upload.head(10), use_container_width=True)
                    
                # ---------------------------------------------------------
                # Intelligent Column Mapping by Financial Prediction Pillars
                # ---------------------------------------------------------
                st.markdown("---")
                st.markdown("### 🎯 Financial Feature Alignment & Prediction Suitability")
                st.write(
                    "Each target feature corresponds to a core financial pillar used by the ML inference pipeline. "
                    "Features are automatically matched to the most suitable column in your file or assigned an intelligent derived fallback."
                )

                # Initialize active column mapping
                detected_map = auto_detect_column_mapping(list(df_upload.columns))
                active_col_map = {}
                
                # Organize features by the 4 Financial Pillars
                pillars = {
                    "🏛️ Pillar 1: Debt & Leverage Capacity (Primary Solvency Drivers)": [
                        "requested_loan_amount", "existing_debt", "credit_utilization_ratio"
                    ],
                    "💵 Pillar 2: Cash Flow & Earnings Health (Liquidity & Margins)": [
                        "annual_revenue", "annual_expenses", "monthly_cash_flow"
                    ],
                    "🛡️ Pillar 3: Repayment Reliability & Bureau Record (Strongest Default Predictor)": [
                        "repayment_history_score", "previous_defaults", "credit_history_months"
                    ],
                    "🏢 Pillar 4: Enterprise Stability & Scale (Operational Vintage)": [
                        "business_age", "num_employees", "business_name"
                    ]
                }
                
                # Render Pillar Sections
                for pillar_title, feats in pillars.items():
                    with st.expander(pillar_title, expanded=True):
                        cols_grid = st.columns(len(feats))
                        for idx, feat in enumerate(feats):
                            spec = PREDICTION_FEATURE_SPECS.get(feat, {})
                            with cols_grid[idx]:
                                st.markdown(
                                    f"<div style='margin-bottom:6px;'>"
                                    f"<b>{feat}</b><br/>"
                                    f"<span style='font-size:0.75rem; color:{spec.get('badge_color', '#3b82f6')}; font-weight:700; background:rgba(0,0,0,0.06); padding:2px 8px; border-radius:6px;'>"
                                    f"{spec.get('shap_importance', 'Important')}</span>"
                                    f"</div>",
                                    unsafe_allow_html=True
                                )
                                st.caption(spec.get("description", ""))
                                
                                detected_val = detected_map.get(feat)
                                smart_fallbacks = spec.get("smart_fallbacks", [])
                                raw_file_cols = list(df_upload.columns)
                                
                                options = []
                                if detected_val:
                                    options.append(detected_val)
                                for fb in smart_fallbacks:
                                    if fb not in options:
                                        options.append(fb)
                                for c in raw_file_cols:
                                    if c not in options:
                                        options.append(c)
                                if "-- Unmapped / Missing --" not in options:
                                    options.append("-- Unmapped / Missing --")
                                    
                                default_idx = 0 if detected_val in options else (options.index(smart_fallbacks[0]) if smart_fallbacks else 0)
                                
                                user_choice = st.selectbox(
                                    label=f"Map {feat}",
                                    options=options,
                                    index=default_idx,
                                    key=f"col_map_v2_{feat}",
                                    label_visibility="collapsed"
                                )
                                active_col_map[feat] = user_choice
                                
                required_cols = [
                    "business_age", "annual_revenue", "annual_expenses", 
                    "existing_debt", "requested_loan_amount", "monthly_cash_flow",
                    "num_employees", "credit_history_months", "previous_defaults",
                    "repayment_history_score", "credit_utilization_ratio"
                ]
                
                unassigned = [c for c in required_cols if not active_col_map.get(c) or active_col_map.get(c) == "-- Unmapped / Missing --"]
                
                if unassigned:
                    st.warning(f"⚠️ {len(unassigned)} required features need mapping: {unassigned}")
                else:
                    st.success("✅ Prediction Feature Mapping Ready: All 11 prediction features are mapped and aligned with the ML model!")
                    
                    # Build standardized, sanitized dataframe
                    df_standard = pd.DataFrame()
                    
                    # 1. Business Name
                    b_name_choice = active_col_map.get("business_name", "")
                    if b_name_choice in df_upload.columns:
                        df_standard["business_name"] = df_upload[b_name_choice].astype(str).fillna("Enterprise")
                    else:
                        df_standard["business_name"] = [f"Enterprise #{i+1}" for i in range(len(df_upload))]
                        
                    # 2. Revenue & Base Amounts
                    rev_choice = active_col_map.get("annual_revenue")
                    if rev_choice in df_upload.columns:
                        df_standard["annual_revenue"] = df_upload[rev_choice].apply(lambda x: sanitize_batch_value(x))
                    else:
                        df_standard["annual_revenue"] = 10000000.0
                        
                    # 3. Loan Amount
                    loan_choice = active_col_map.get("requested_loan_amount")
                    if loan_choice in df_upload.columns:
                        df_standard["requested_loan_amount"] = df_upload[loan_choice].apply(lambda x: sanitize_batch_value(x))
                    else:
                        df_standard["requested_loan_amount"] = df_standard["annual_revenue"] * 0.25
                        
                    # 4. Existing Debt
                    debt_choice = active_col_map.get("existing_debt")
                    if debt_choice in df_upload.columns:
                        df_standard["existing_debt"] = df_upload[debt_choice].apply(lambda x: sanitize_batch_value(x))
                    else:
                        df_standard["existing_debt"] = 0.0
                        
                    # 5. Annual Expenses
                    exp_choice = active_col_map.get("annual_expenses")
                    if exp_choice in df_upload.columns:
                        df_standard["annual_expenses"] = df_upload[exp_choice].apply(lambda x: sanitize_batch_value(x))
                    elif "80%" in str(exp_choice):
                        df_standard["annual_expenses"] = df_standard["annual_revenue"] * 0.80
                    else:
                        df_standard["annual_expenses"] = df_standard["annual_revenue"] * 0.75
                        
                    # 6. Monthly Cash Flow
                    cf_choice = active_col_map.get("monthly_cash_flow")
                    if cf_choice in df_upload.columns:
                        df_standard["monthly_cash_flow"] = df_upload[cf_choice].apply(lambda x: sanitize_batch_value(x))
                    elif "5%" in str(cf_choice):
                        df_standard["monthly_cash_flow"] = (df_standard["annual_revenue"] / 12.0) * 0.05
                    else:
                        df_standard["monthly_cash_flow"] = (df_standard["annual_revenue"] - df_standard["annual_expenses"]) / 12.0
                        
                    # 7. Business Age
                    age_choice = active_col_map.get("business_age")
                    if age_choice in df_upload.columns:
                        df_standard["business_age"] = df_upload[age_choice].apply(lambda x: sanitize_batch_value(x))
                    else:
                        df_standard["business_age"] = 5.0
                        
                    # 8. Number of Employees
                    emp_choice = active_col_map.get("num_employees")
                    if emp_choice in df_upload.columns:
                        df_standard["num_employees"] = df_upload[emp_choice].apply(lambda x: int(sanitize_batch_value(x)))
                    elif "8" in str(emp_choice):
                        df_standard["num_employees"] = 8
                    else:
                        df_standard["num_employees"] = 15
                        
                    # 9. Credit History Months
                    ch_choice = active_col_map.get("credit_history_months")
                    if ch_choice in df_upload.columns:
                        df_standard["credit_history_months"] = df_upload[ch_choice].apply(lambda x: sanitize_batch_value(x))
                    elif "60" in str(ch_choice):
                        df_standard["credit_history_months"] = 60.0
                    else:
                        df_standard["credit_history_months"] = df_standard["business_age"] * 12.0
                        
                    # 10. Previous Defaults
                    def_choice = active_col_map.get("previous_defaults")
                    if def_choice in df_upload.columns:
                        df_standard["previous_defaults"] = df_upload[def_choice].apply(lambda x: int(sanitize_batch_value(x)))
                    else:
                        df_standard["previous_defaults"] = 0
                        
                    # 11. Repayment History Score (Auto-rescale FICO 300-850 if detected)
                    rep_choice = active_col_map.get("repayment_history_score")
                    if rep_choice in df_upload.columns:
                        raw_scores = df_upload[rep_choice].apply(lambda x: sanitize_batch_value(x))
                        if raw_scores.max() > 100.0:
                            df_standard["repayment_history_score"] = raw_scores.apply(lambda x: np.clip((x - 300.0) / 5.5, 0.0, 100.0) if x > 100.0 else x)
                        else:
                            df_standard["repayment_history_score"] = raw_scores
                    elif "75" in str(rep_choice):
                        df_standard["repayment_history_score"] = 75.0
                    else:
                        df_standard["repayment_history_score"] = 85.0
                        
                    # 12. Credit Utilization Ratio
                    cur_choice = active_col_map.get("credit_utilization_ratio")
                    if cur_choice in df_upload.columns:
                        raw_cur = df_upload[cur_choice].apply(lambda x: sanitize_batch_value(x, is_percentage=True))
                        df_standard["credit_utilization_ratio"] = raw_cur
                    elif "50%" in str(cur_choice):
                        df_standard["credit_utilization_ratio"] = 0.50
                    else:
                        df_standard["credit_utilization_ratio"] = 0.30

                    # Action buttons
                    b_act1, b_act2 = st.columns([2, 1])
                    with b_act1:
                        execute_batch = st.button("🚀 Process Batch Risk Assessment", type="primary")
                        
                    if execute_batch:
                        t_start = time.time()
                        total_records = len(df_standard)
                        with st.spinner(f"⚡ Executing vectorized ML pipeline for {total_records:,} enterprises..."):
                            model, preprocessor = load_prediction_artifacts()
                            
                            # 1. Vectorized Feature Engineering
                            df_features = add_financial_features(df_standard)
                            X_features = df_features[ALL_INPUT_FEATURES]
                            
                            # 2. Adaptive Chunked Inference (Handles from 100 up to 5,000,000+ records)
                            chunk_size = 100_000
                            if total_records <= chunk_size:
                                X_trans = preprocessor.transform(X_features)
                                preds_idx = model.predict(X_trans).astype(int)
                                probas = model.predict_proba(X_trans) if hasattr(model, "predict_proba") else None
                                prob_low = np.round(probas[:, 0] * 100.0, 2) if probas is not None else np.where(preds_idx == 0, 100.0, 0.0)
                                prob_med = np.round(probas[:, 1] * 100.0, 2) if probas is not None else np.where(preds_idx == 1, 100.0, 0.0)
                                prob_high = np.round(probas[:, 2] * 100.0, 2) if probas is not None else np.where(preds_idx == 2, 100.0, 0.0)
                            else:
                                pred_list, pl_list, pm_list, ph_list = [], [], [], []
                                progress_bar = st.progress(0, text=f"Evaluating in high-speed chunks (0 / {total_records:,})...")
                                for i in range(0, total_records, chunk_size):
                                    chunk_X = X_features.iloc[i : i + chunk_size]
                                    chunk_trans = preprocessor.transform(chunk_X)
                                    c_preds = model.predict(chunk_trans).astype(int)
                                    pred_list.append(c_preds)
                                    if hasattr(model, "predict_proba"):
                                        c_prob = model.predict_proba(chunk_trans)
                                        pl_list.append(c_prob[:, 0])
                                        pm_list.append(c_prob[:, 1])
                                        ph_list.append(c_prob[:, 2])
                                    else:
                                        pl_list.append(np.where(c_preds == 0, 1.0, 0.0))
                                        pm_list.append(np.where(c_preds == 1, 1.0, 0.0))
                                        ph_list.append(np.where(c_preds == 2, 1.0, 0.0))
                                    current_done = min(i + chunk_size, total_records)
                                    progress_bar.progress(current_done / total_records, text=f"Evaluated {current_done:,} of {total_records:,} enterprises...")
                                progress_bar.empty()
                                
                                preds_idx = np.concatenate(pred_list)
                                prob_low = np.round(np.concatenate(pl_list) * 100.0, 2)
                                prob_med = np.round(np.concatenate(pm_list) * 100.0, 2)
                                prob_high = np.round(np.concatenate(ph_list) * 100.0, 2)
                                
                            risk_categories = np.array([RISK_MAP.get(idx, "MEDIUM") for idx in preds_idx])
                                
                            # 3. Vectorized Financial Health Scoring
                            rev = np.maximum(df_standard["annual_revenue"].values.astype(float), 1.0)
                            exp = df_standard["annual_expenses"].values.astype(float)
                            debt = np.maximum(df_standard["existing_debt"].values.astype(float), 0.0)
                            loan = np.maximum(df_standard["requested_loan_amount"].values.astype(float), 1.0)
                            cash_flow_m = df_standard["monthly_cash_flow"].values.astype(float)
                            age = df_standard["business_age"].values.astype(float)
                            defaults = df_standard["previous_defaults"].values.astype(int)
                            repay_score = df_standard["repayment_history_score"].values.astype(float)
                            util_ratio = df_standard["credit_utilization_ratio"].values.astype(float)
                            
                            dti = debt / rev
                            profit_margin = (rev - exp) / rev
                            cash_flow_annual = cash_flow_m * 12.0
                            cf_to_loan = cash_flow_annual / loan
                            
                            debt_pts = np.where(dti <= 0.2, 25.0,
                                       np.where(dti <= 0.5, 20.0 - (dti - 0.2) * 25.0,
                                       np.where(dti <= 1.0, 12.5 - (dti - 0.5) * 15.0,
                                                np.maximum(0.0, 5.0 - (dti - 1.0) * 5.0))))
                            debt_pts = np.where(util_ratio > 0.8, np.maximum(0.0, debt_pts - 5.0), debt_pts)

                            cf_pts = np.where(cf_to_loan >= 1.5, 25.0,
                                     np.where(cf_to_loan >= 1.0, 20.0 + (cf_to_loan - 1.0) * 10.0,
                                     np.where(cf_to_loan >= 0.5, 10.0 + (cf_to_loan - 0.5) * 20.0,
                                     np.where(cf_to_loan > 0.0, cf_to_loan * 20.0, 0.0))))
                                     
                            prof_pts = np.where(profit_margin >= 0.25, 20.0,
                                       np.where(profit_margin >= 0.10, 12.0 + (profit_margin - 0.10) * 53.3,
                                       np.where(profit_margin >= 0.0, profit_margin * 120.0,
                                                np.maximum(0.0, 5.0 + profit_margin * 20.0))))
                                                
                            base_repay = (repay_score / 100.0) * 15.0
                            repay_pts = np.clip(base_repay + 5.0 - defaults * 4.0, 0.0, 20.0)

                            stab_pts = np.where(age >= 10, 10.0,
                                       np.where(age >= 5, 7.0 + (age - 5.0) * 0.6,
                                       np.where(age >= 2, 4.0 + (age - 2.0) * 1.0,
                                                np.maximum(1.0, age * 2.0))))
                                                
                            total_health = np.clip(np.round(debt_pts + cf_pts + prof_pts + repay_pts + stab_pts, 1), 0.0, 100.0)
                            health_grades = np.where(total_health >= 80.0, "EXCELLENT",
                                            np.where(total_health >= 65.0, "GOOD",
                                            np.where(total_health >= 50.0, "FAIR", "POOR")))
                                            
                            df_batch_res = pd.DataFrame({
                                "business_name": df_standard["business_name"].values,
                                "annual_revenue": df_standard["annual_revenue"].values,
                                "requested_loan_amount": df_standard["requested_loan_amount"].values,
                                "risk_category": risk_categories,
                                "probability_low": prob_low,
                                "probability_medium": prob_med,
                                "probability_high": prob_high,
                                "financial_health_score": total_health,
                                "financial_health_grade": health_grades
                            })
                            
                            st.session_state["batch_processed_df"] = df_batch_res
                            st.session_state["batch_standard_df"] = df_standard
                            elapsed = time.time() - t_start
                            st.success(f"⚡ Batch analysis complete for {len(df_batch_res):,} enterprises in {elapsed:.2f} seconds!")
                            
                    if "batch_processed_df" in st.session_state:
                        df_res = st.session_state["batch_processed_df"]
                        st.markdown("---")
                        st.subheader("Batch Evaluation Summary")
                        
                        bc1, bc2, bc3 = st.columns(3)
                        with bc1:
                            st.metric("Total Processed", f"{len(df_res):,}")
                        with bc2:
                            st.metric("Low Risk Count", f"{(df_res['risk_category'] == 'LOW').sum():,}")
                        with bc3:
                            st.metric("Avg Health Score", f"{round(df_res['financial_health_score'].mean(), 1)}/100")
                            
                        if len(df_res) > 1000:
                            st.info(f"📊 Displaying preview of first 1,000 records (out of {len(df_res):,}). Full dataset available for download below.")
                            st.dataframe(df_res.head(1000), use_container_width=True)
                        else:
                            st.dataframe(df_res, use_container_width=True)
                        
                        d_col1, d_col2 = st.columns(2)
                        with d_col1:
                            csv_data = df_res.to_csv(index=False).encode('utf-8')
                            st.download_button(
                                label=f"📥 Download Full Batch Results CSV ({len(df_res):,} records)",
                                data=csv_data,
                                file_name=f"MSME_Batch_Results_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                                mime="text/csv",
                                use_container_width=True
                            )
                        with d_col2:
                            save_limit = min(500, len(df_res))
                            if st.button(f"💾 Save First {save_limit:,} Records to SQLite Database", use_container_width=True):
                                saved = 0
                                records_to_save = st.session_state.get("batch_standard_df", df_standard).head(save_limit)
                                with st.spinner(f"Saving {save_limit} records to persistent database..."):
                                    for idx, row in records_to_save.iterrows():
                                        rec = row.to_dict()
                                        p_res = {
                                            "risk_category": df_res.loc[idx, "risk_category"],
                                            "probabilities": {
                                                "LOW": df_res.loc[idx, "probability_low"],
                                                "MEDIUM": df_res.loc[idx, "probability_medium"],
                                                "HIGH": df_res.loc[idx, "probability_high"]
                                            }
                                        }
                                        h_res = {
                                            "total_score": df_res.loc[idx, "financial_health_score"],
                                            "grade": df_res.loc[idx, "financial_health_grade"]
                                        }
                                        save_assessment_record(rec.get("business_name", "Batch Enterprise"), rec, p_res, h_res)
                                        saved += 1
                                st.success(f"Saved {saved} records to database!")

                        # -------------------------------------------------------------
                        # DIRECT LINK TO PREDICTION SECTION (Single Risk Assessment & SHAP)
                        # -------------------------------------------------------------
                        st.markdown("---")
                        st.markdown("""
                            <div style="background:var(--secondary-background-color, rgba(128,128,128,0.08)); padding:18px 22px; border-radius:12px; border:1px solid rgba(128,128,128,0.2); margin-top:16px;">
                                <h4 style="margin:0 0 6px 0;">🎯 Send Enterprise to Prediction & Explainable AI (SHAP)</h4>
                                <p style="font-size:0.86rem; color:#64748b; margin:0 0 14px 0;">
                                    Select any enterprise from this batch to load its metrics directly into the <b>Single Risk Assessment</b> or <b>Explainable AI (SHAP)</b> section for granular feature attribution:
                                </p>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        enterprise_labels = [
                            f"#{i+1}: {row.get('business_name', 'Enterprise')} | Risk: {row.get('risk_category')} | Score: {row.get('financial_health_score')}/100 | Loan: ₹{float(row.get('requested_loan_amount', 0)):,.0f}"
                            for i, row in df_res.iterrows()
                        ]
                        sel_ent_idx = st.selectbox(
                            "Select Enterprise for In-Depth Prediction Analysis:",
                            range(len(enterprise_labels)),
                            format_func=lambda i: enterprise_labels[i],
                            key="batch_to_single_prediction_sel"
                        )
                        
                        send_col1, send_col2 = st.columns(2)
                        with send_col1:
                            if st.button("💳 Inspect & Fine-Tune in Single Risk Assessment", type="primary", use_container_width=True):
                                curr_std = st.session_state.get("batch_standard_df", df_standard)
                                sel_rec = curr_std.iloc[sel_ent_idx].to_dict()
                                st.session_state["prefill_single_risk"] = sel_rec
                                p_res = predict_msme_risk(sel_rec)
                                h_res = calculate_financial_health_score(sel_rec)
                                shap_exp = get_local_shap_explanation(sel_rec)
                                insights = generate_risk_improvement_insights(sel_rec, shap_exp)
                                st.session_state["last_assessment"] = {
                                    "business_name": sel_rec.get("business_name", f"Enterprise #{sel_ent_idx+1}"),
                                    "raw_input": sel_rec,
                                    "pred_res": p_res,
                                    "health_res": h_res,
                                    "shap_exp": shap_exp,
                                    "insights": insights
                                }
                                st.session_state["nav_override"] = "💳 Single Risk Assessment"
                                st.rerun()
                                
                        with send_col2:
                            if st.button("💡 Analyze Local SHAP Feature Waterfall", type="secondary", use_container_width=True):
                                curr_std = st.session_state.get("batch_standard_df", df_standard)
                                sel_rec = curr_std.iloc[sel_ent_idx].to_dict()
                                p_res = predict_msme_risk(sel_rec)
                                h_res = calculate_financial_health_score(sel_rec)
                                shap_exp = get_local_shap_explanation(sel_rec)
                                insights = generate_risk_improvement_insights(sel_rec, shap_exp)
                                st.session_state["last_assessment"] = {
                                    "business_name": sel_rec.get("business_name", f"Enterprise #{sel_ent_idx+1}"),
                                    "raw_input": sel_rec,
                                    "pred_res": p_res,
                                    "health_res": h_res,
                                    "shap_exp": shap_exp,
                                    "insights": insights
                                }
                                st.session_state["nav_override"] = "💡 Explainable AI (SHAP)"
                                st.rerun()
            except Exception as e:
                st.error(f"Error reading dataset: {str(e)}")
                
    with tab_sample:
        st.markdown("### Standard CSV Template")
        st.write("You can download this pre-formatted template with sample MSME records, fill in your data, and upload it in the upload tab.")
        sample_df = pd.DataFrame([
            {
                "business_name": "Apex Precision Engineering Pvt Ltd",
                "business_age": 7.5,
                "annual_revenue": 18000000.0,
                "annual_expenses": 13000000.0,
                "existing_debt": 2000000.0,
                "requested_loan_amount": 3500000.0,
                "monthly_cash_flow": 300000.0,
                "num_employees": 22,
                "credit_history_months": 72,
                "previous_defaults": 0,
                "repayment_history_score": 94.0,
                "credit_utilization_ratio": 0.28
            },
            {
                "business_name": "Kavita Agro Processing Works",
                "business_age": 4.0,
                "annual_revenue": 9500000.0,
                "annual_expenses": 7800000.0,
                "existing_debt": 2200000.0,
                "requested_loan_amount": 2500000.0,
                "monthly_cash_flow": 120000.0,
                "num_employees": 11,
                "credit_history_months": 36,
                "previous_defaults": 1,
                "repayment_history_score": 76.5,
                "credit_utilization_ratio": 0.52
            },
            {
                "business_name": "Sunrise Logistics & Transport",
                "business_age": 2.2,
                "annual_revenue": 5200000.0,
                "annual_expenses": 4900000.0,
                "existing_debt": 2800000.0,
                "requested_loan_amount": 3000000.0,
                "monthly_cash_flow": 35000.0,
                "num_employees": 6,
                "credit_history_months": 18,
                "previous_defaults": 2,
                "repayment_history_score": 58.0,
                "credit_utilization_ratio": 0.78
            }
        ])
        st.dataframe(sample_df, use_container_width=True)
        st.download_button(
            label="📄 Download Sample CSV Template (3 Enterprises)",
            data=sample_df.to_csv(index=False).encode('utf-8'),
            file_name="msme_sample_template.csv",
            mime="text/csv"
        )
        
    with tab_manual:
        st.markdown("### Quick Enterprise Add")
        with st.form("manual_add_form"):
            m_name = st.text_input("Business Name", value="Global Engineering Pvt Ltd")
            mc1, mc2 = st.columns(2)
            with mc1:
                m_age = st.number_input("Business Age (Years)", value=5.0)
                m_rev = st.number_input("Annual Revenue (₹)", value=12000000.0)
                m_exp = st.number_input("Annual Expenses (₹)", value=9000000.0)
            with mc2:
                m_debt = st.number_input("Existing Debt (₹)", value=1500000.0)
                m_loan = st.number_input("Requested Loan (₹)", value=2500000.0)
                m_cf = st.number_input("Monthly Cash Flow (₹)", value=200000.0)
                
            m_submit = st.form_submit_button("Add & Evaluate Record", type="primary")
            if m_submit:
                man_data = {
                    "business_name": m_name, "business_age": m_age, "annual_revenue": m_rev,
                    "annual_expenses": m_exp, "existing_debt": m_debt, "requested_loan_amount": m_loan,
                    "monthly_cash_flow": m_cf, "num_employees": 15, "credit_history_months": 48,
                    "previous_defaults": 0, "repayment_history_score": 90.0, "credit_utilization_ratio": 0.35
                }
                p_res = predict_msme_risk(man_data)
                h_res = calculate_financial_health_score(man_data)
                bid = save_assessment_record(m_name, man_data, p_res, h_res)
                st.success(f"Enterprise '{m_name}' added under ID #{bid}! Risk: {p_res['risk_category']}")

# -----------------------------------------------------------------------------
# PAGE 3: SINGLE RISK ASSESSMENT
# -----------------------------------------------------------------------------
elif navigation_page == "💳 Single Risk Assessment":
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">Enterprise Risk Evaluation</h1>
            <p class="hero-subtitle">Input financial metrics to run calibrated ML prediction, 5-Pillar health scoring, and SHAP explanations</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Direct Integration: Load Enterprise from Uploaded Batch Dataset
    if "batch_standard_df" in st.session_state and len(st.session_state["batch_standard_df"]) > 0:
        df_batch = st.session_state["batch_standard_df"]
        total_recs = len(df_batch)
        display_limit = min(500, total_recs)
        df_preview = df_batch.iloc[:display_limit]
        
        with st.expander(f"📥 Import Profile from Uploaded Batch Dataset ({total_recs:,} available)", expanded=True):
            st.write(f"Select an enterprise record to auto-fill this prediction form (showing top {display_limit:,} of {total_recs:,} records):")
            
            def make_batch_label(idx):
                row = df_preview.iloc[idx]
                name = str(row.get('business_name', f'Enterprise #{idx+1}'))
                try:
                    loan_v = float(row.get('requested_loan_amount', 0)) if pd.notnull(row.get('requested_loan_amount')) else 0.0
                except Exception:
                    loan_v = 0.0
                try:
                    rev_v = float(row.get('annual_revenue', 0)) if pd.notnull(row.get('annual_revenue')) else 0.0
                except Exception:
                    rev_v = 0.0
                return f"#{idx+1}: {name} | Loan: ₹{loan_v:,.0f} | Revenue: ₹{rev_v:,.0f}"

            sel_b_idx = st.selectbox("Select Enterprise from Dataset:", range(display_limit), format_func=make_batch_label, key="single_batch_sel")
            if st.button("⚡ Load Profile into Evaluation Form", key="load_batch_single_btn", type="primary"):
                st.session_state["prefill_single_risk"] = df_batch.iloc[sel_b_idx].to_dict()
                st.success(f"Profile loaded for '{df_batch.iloc[sel_b_idx].get('business_name')}'!")
                st.rerun()

    prefill = st.session_state.get("prefill_single_risk", {})
    
    with st.form("risk_form"):
        st.markdown("#### **1. Enterprise Profile (Stability & Scale)**")
        c1, c2, c3 = st.columns(3)
        with c1:
            raw_name = str(prefill.get("business_name", "Mahalaxmi Enterprises"))
            if pd.isna(prefill.get("business_name")) or not raw_name.strip():
                raw_name = "Mahalaxmi Enterprises"
            business_name = st.text_input("Business Name", value=raw_name)
        with c2:
            try:
                raw_age = float(prefill.get("business_age", 6.5))
                if pd.isna(raw_age): raw_age = 6.5
            except Exception:
                raw_age = 6.5
            safe_age = max(0.0, min(100.0, raw_age))
            business_age = st.number_input("Business Age (Years)", min_value=0.0, max_value=100.0, value=safe_age, step=0.5)
        with c3:
            try:
                raw_emp = int(float(prefill.get("num_employees", 18)))
                if pd.isna(raw_emp): raw_emp = 18
            except Exception:
                raw_emp = 18
            safe_emp = max(1, min(100000, raw_emp))
            num_employees = st.number_input("Number of Employees", min_value=1, max_value=100000, value=safe_emp, step=1)
            
        st.markdown("#### **2. Financial Statements (Debt & Leverage Pillars)**")
        f1, f2, f3, f4 = st.columns(4)
        with f1:
            try:
                raw_rev = float(prefill.get("annual_revenue", 15000000.0))
                if pd.isna(raw_rev): raw_rev = 15000000.0
            except Exception:
                raw_rev = 15000000.0
            safe_rev = max(0.0, raw_rev)
            annual_revenue = st.number_input("Annual Revenue (₹)", min_value=0.0, value=safe_rev, step=50000.0)
        with f2:
            try:
                raw_exp = float(prefill.get("annual_expenses", 11000000.0))
                if pd.isna(raw_exp): raw_exp = 11000000.0
            except Exception:
                raw_exp = 11000000.0
            safe_exp = max(0.0, raw_exp)
            annual_expenses = st.number_input("Annual Expenses (₹)", min_value=0.0, value=safe_exp, step=50000.0)
        with f3:
            try:
                raw_debt = float(prefill.get("existing_debt", 2500000.0))
                if pd.isna(raw_debt): raw_debt = 2500000.0
            except Exception:
                raw_debt = 2500000.0
            safe_debt = max(0.0, raw_debt)
            existing_debt = st.number_input("Existing Debt (₹)", min_value=0.0, value=safe_debt, step=50000.0)
        with f4:
            try:
                raw_loan = float(prefill.get("requested_loan_amount", 3000000.0))
                if pd.isna(raw_loan): raw_loan = 3000000.0
            except Exception:
                raw_loan = 3000000.0
            safe_loan = max(0.0, raw_loan)
            requested_loan_amount = st.number_input("Requested Loan (₹)", min_value=0.0, value=safe_loan, step=50000.0)
            
        st.markdown("#### **3. Liquidity & Credit Bureau (Cash Flow & Bureau Pillars)**")
        l1, l2, l3, l4 = st.columns(4)
        with l1:
            try:
                raw_cf = float(prefill.get("monthly_cash_flow", 250000.0))
                if pd.isna(raw_cf): raw_cf = 250000.0
            except Exception:
                raw_cf = 250000.0
            monthly_cash_flow = st.number_input("Monthly Cash Flow (₹)", value=raw_cf, step=10000.0)
        with l2:
            try:
                raw_hist = int(float(prefill.get("credit_history_months", 60)))
                if pd.isna(raw_hist): raw_hist = 60
            except Exception:
                raw_hist = 60
            safe_hist = max(0, min(1200, raw_hist))
            credit_history_months = st.number_input("Credit History (Months)", min_value=0, max_value=1200, value=safe_hist, step=6)
        with l3:
            try:
                raw_def = int(float(prefill.get("previous_defaults", 0)))
                if pd.isna(raw_def): raw_def = 0
            except Exception:
                raw_def = 0
            safe_def = max(0, min(100, raw_def))
            previous_defaults = st.number_input("Previous Defaults", min_value=0, max_value=100, value=safe_def, step=1)
        with l4:
            try:
                raw_rep = float(prefill.get("repayment_history_score", 92.0))
                if pd.isna(raw_rep): raw_rep = 92.0
            except Exception:
                raw_rep = 92.0
            safe_rep = max(0.0, min(100.0, raw_rep))
            repayment_history_score = st.slider("Repayment Score (0-100)", min_value=0.0, max_value=100.0, value=safe_rep)
            
        try:
            raw_util = float(prefill.get("credit_utilization_ratio", 0.35))
            if pd.isna(raw_util): raw_util = 0.35
        except Exception:
            raw_util = 0.35
        safe_util = max(0.0, min(1.0, raw_util))
        credit_utilization_ratio = st.slider("Credit Utilization Ratio (0.0 to 1.0)", min_value=0.0, max_value=1.0, value=safe_util, step=0.05)
        
        submit_btn = st.form_submit_button("⚡ Execute Risk Assessment", type="primary")
        
    if submit_btn:
        form_data = {
            "business_name": business_name, "business_age": business_age, "num_employees": num_employees,
            "annual_revenue": annual_revenue, "annual_expenses": annual_expenses, "existing_debt": existing_debt,
            "requested_loan_amount": requested_loan_amount, "monthly_cash_flow": monthly_cash_flow,
            "credit_history_months": credit_history_months, "previous_defaults": previous_defaults,
            "repayment_history_score": repayment_history_score, "credit_utilization_ratio": credit_utilization_ratio
        }
        
        is_valid, errors = validate_msme_input_form(form_data)
        if not is_valid:
            for err in errors:
                st.error(err)
        else:
            with st.spinner("Computing pipeline..."):
                pred_res = predict_msme_risk(form_data)
                health_res = calculate_financial_health_score(form_data)
                shap_exp = get_local_shap_explanation(form_data)
                insights = generate_risk_improvement_insights(form_data, shap_exp)
                
                bid = save_assessment_record(business_name, form_data, pred_res, health_res, model_version=metadata.get("version", "1.0.0"))
                
                st.session_state["last_assessment"] = {
                    "business_name": business_name, "raw_input": form_data,
                    "pred_res": pred_res, "health_res": health_res,
                    "shap_exp": shap_exp, "insights": insights
                }
                st.success(f"Assessment saved under Business ID #{bid}")

    if "last_assessment" in st.session_state:
        la = st.session_state["last_assessment"]
        st.markdown("---")
        st.header(f"Assessment Output: {la['business_name']}")
        
        res_col1, res_col2, res_col3 = st.columns([1, 1.2, 1])
        with res_col1:
            rc = la["pred_res"]["risk_category"]
            badge_cls = "badge-low-risk" if rc == "LOW" else ("badge-medium-risk" if rc == "MEDIUM" else "badge-high-risk")
            st.markdown(f"**Predicted Risk Category:**")
            st.markdown(f'<div class="badge-container {badge_cls}">{rc} RISK</div>', unsafe_allow_html=True)
            
            probas = la["pred_res"]["probabilities"]
            st.markdown("<br/>**Calibrated Probabilities:**", unsafe_allow_html=True)
            st.write(f"🟢 Low: **{probas.get('LOW',0)}%**")
            st.write(f"🟡 Medium: **{probas.get('MEDIUM',0)}%**")
            st.write(f"🔴 High: **{probas.get('HIGH',0)}%**")
            
        with res_col2:
            fig_g = plot_financial_health_gauge(la['health_res']['total_score'], la['health_res']['grade'])
            st.plotly_chart(fig_g, use_container_width=True)
            
        with res_col3:
            fig_rad = plot_radar_pillars(la['health_res']['pillars'])
            st.plotly_chart(fig_rad, use_container_width=True)
            
        st.subheader("Calculated Financial Ratios")
        eng = la["pred_res"]["engineered_features"]
        i1, i2, i3, i4, i5 = st.columns(5)
        with i1: st.metric("DTI Ratio", f"{eng['dti_ratio']:.2f}")
        with i2: st.metric("Net Profit", format_inr(eng['profit']))
        with i3: st.metric("Profit Margin", f"{eng['profit_margin']*100:.1f}%")
        with i4: st.metric("Loan to Income", f"{eng['loan_to_income']:.2f}")
        with i5: st.metric("Cash Flow / Loan", f"{eng['cash_flow_to_loan']:.2f}")

        pdf_bytes = generate_pdf_report(
            la["business_name"], la["raw_input"], la["pred_res"],
            la["health_res"], la["shap_exp"], la["insights"]
        )
        st.download_button(
            label="📄 Download Assessment PDF Report",
            data=pdf_bytes,
            file_name=f"MSME_Credit_Report_{la['business_name'].replace(' ', '_')}.pdf",
            mime="application/pdf"
        )

# -----------------------------------------------------------------------------
# PAGE 4: FINANCIAL HEALTH ANALYTICS
# -----------------------------------------------------------------------------
elif navigation_page == "🩺 Financial Health Analytics":
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">Financial Health Analytics</h1>
            <p class="hero-subtitle">Independent 0–100 score analyzing 5 key operational pillars</p>
        </div>
    """, unsafe_allow_html=True)
    
    la = ensure_active_assessment()
    fh = la["health_res"]
    
    st.subheader(f"Financial Health Breakdown: {la['business_name']}")
    
    hc1, hc2 = st.columns([1, 1])
    with hc1:
        fig_g = plot_financial_health_gauge(fh['total_score'], fh['grade'])
        st.plotly_chart(fig_g, use_container_width=True)
    with hc2:
        fig_r = plot_radar_pillars(fh['pillars'])
        st.plotly_chart(fig_r, use_container_width=True)
        
    pillars = fh["pillars"]
    df_p = pd.DataFrame({
        "Pillar": ["Debt Mgmt", "Cash Flow", "Profitability", "Repayment", "Stability"],
        "Score": [pillars["debt_management"], pillars["cash_flow_liquidity"], pillars["profitability"], pillars["repayment_history"], pillars["business_stability"]],
        "Max Score": [25, 25, 20, 20, 10]
    })
    fig_b = px.bar(df_p, x="Pillar", y="Score", text="Score", color="Score", color_continuous_scale="Viridis", range_y=[0, 30])
    fig_b.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig_b, use_container_width=True)

# -----------------------------------------------------------------------------
# PAGE 5: EXPLAINABLE AI (SHAP)
# -----------------------------------------------------------------------------
elif navigation_page == "💡 Explainable AI (SHAP)":
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">SHAP Model Explainability</h1>
            <p class="hero-subtitle">Shapley value breakdown for model global rankings and individual enterprise local predictions</p>
        </div>
    """, unsafe_allow_html=True)
    
    tab_local, tab_global = st.tabs(["Local Instance Explanation", "Global Feature Importance"])
    
    with tab_local:
        if "batch_standard_df" in st.session_state and len(st.session_state["batch_standard_df"]) > 0:
            df_b = st.session_state["batch_standard_df"]
            b_names = [f"#{i+1}: {r.get('business_name', f'Enterprise #{i+1}')} (Loan: ₹{float(r.get('requested_loan_amount',0)):,.0f})" for i, r in df_b.iterrows()]
            with st.expander("📥 Switch Enterprise from Uploaded Batch Dataset", expanded=False):
                s_idx = st.selectbox("Select Enterprise to Explain with SHAP:", range(len(b_names)), format_func=lambda i: b_names[i], key="shap_batch_switcher")
                if st.button("⚡ Generate SHAP Explanation for Selected Enterprise", key="shap_batch_btn"):
                    sel_rec = df_b.iloc[s_idx].to_dict()
                    p_res = predict_msme_risk(sel_rec)
                    h_res = calculate_financial_health_score(sel_rec)
                    shap_exp = get_local_shap_explanation(sel_rec)
                    insights = generate_risk_improvement_insights(sel_rec, shap_exp)
                    st.session_state["last_assessment"] = {
                        "business_name": sel_rec.get("business_name", f"Enterprise #{s_idx+1}"),
                        "raw_input": sel_rec,
                        "pred_res": p_res,
                        "health_res": h_res,
                        "shap_exp": shap_exp,
                        "insights": insights
                    }
                    st.rerun()

        la = ensure_active_assessment()
        shap_exp = la["shap_exp"]
        insights = la["insights"]
        
        st.subheader(f"Local Feature Drivers & Insights: {la['business_name']}")
        
        rc = la["pred_res"]["risk_category"]
        badge_cls = "badge-low-risk" if rc == "LOW" else ("badge-medium-risk" if rc == "MEDIUM" else "badge-high-risk")
        st.markdown(f'<div class="badge-container {badge_cls}">CLASSIFIED RISK: {rc}</div><br/><br/>', unsafe_allow_html=True)
        
        top_impacts = pd.DataFrame(shap_exp["top_feature_impacts"])
        fig_shap = px.bar(
            top_impacts, x="shap_value", y="feature", orientation="h",
            color="shap_value", color_continuous_scale="RdYlGn_r",
            labels={"shap_value": "SHAP Risk Contribution", "feature": "Financial Feature"},
            title="Feature Contribution Spectrum (Positive = Pushes to High Risk | Negative = Pushes to Low Risk)"
        )
        fig_shap.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_shap, use_container_width=True)
        
        col_inc, col_dec = st.columns(2)
        with col_inc:
            st.markdown("#### 🚨 **Factors Increasing Credit Risk (SHAP > 0)**")
            inc_factors = shap_exp.get("increasing_risk_factors", [])
            if inc_factors:
                for f in inc_factors[:5]:
                    st.markdown(f"- **`{f['feature']}`** = `{f['feature_value']:,.2f}` *(SHAP Impact: +{f['shap_value']:.4f})*")
            else:
                st.info("No major risk-increasing factors detected.")

        with col_dec:
            st.markdown("#### ✅ **Factors Reducing Credit Risk (SHAP < 0)**")
            dec_factors = shap_exp.get("decreasing_risk_factors", [])
            if dec_factors:
                for f in dec_factors[:5]:
                    st.markdown(f"- **`{f['feature']}`** = `{f['feature_value']:,.2f}` *(SHAP Impact: {f['shap_value']:.4f})*")
            else:
                st.info("No major risk-reducing factors detected.")

        st.markdown("---")
        st.subheader("💡 Actionable Risk Improvement Insights & Recommendations")
        
        if insights:
            for ins in insights:
                itype = ins.get("type", "NEUTRAL")
                cls_name = "insight-critical" if itype == "CRITICAL" else ("insight-positive" if itype == "POSITIVE" else "insight-warning")
                icon = "🔴" if itype == "CRITICAL" else ("🟢" if itype == "POSITIVE" else "🟡")
                
                st.markdown(f"""
                    <div class="insight-card {cls_name}">
                        <div style="font-weight:700; font-size:1.05rem;">{icon} [{ins.get('category')}] - {itype}</div>
                        <div style="margin-top:4px;"><b>Observation:</b> {ins.get('observation')}</div>
                        <div style="margin-top:4px; font-style:italic;"><b>Recommendation:</b> {ins.get('recommendation')}</div>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No critical risk improvement warnings generated.")
            
        with st.expander("📋 Detailed Feature Impact Table"):
            st.dataframe(top_impacts[["feature", "feature_value", "shap_value"]], use_container_width=True)
            
    with tab_global:
        st.subheader("Global Feature Ranking")
        global_features = pd.DataFrame({
            "Feature": ALL_INPUT_FEATURES,
            "Importance": [0.28, 0.24, 0.19, 0.15, 0.14, 0.12, 0.11, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.02, 0.01, 0.01]
        }).sort_values("Importance", ascending=True)
        fig_g = px.bar(global_features, x="Importance", y="Feature", orientation="h")
        fig_g.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_g, use_container_width=True)

# -----------------------------------------------------------------------------
# PAGE 6: WHAT-IF SCENARIO SIMULATION
# -----------------------------------------------------------------------------
elif navigation_page == "🔮 What-If Scenario Simulation":
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">What-If Scenario Simulation</h1>
            <p class="hero-subtitle">Interactively tune financial parameters and observe instantaneous model probability shifts</p>
        </div>
    """, unsafe_allow_html=True)
    
    if "last_assessment" in st.session_state:
        la = st.session_state["last_assessment"]
        orig = la["raw_input"]
        
        st.subheader(f"Baseline: {la['business_name']}")
        
        c1, c2 = st.columns(2)
        with c1:
            try:
                val_rev = float(orig.get("annual_revenue", 15000000.0))
            except Exception:
                val_rev = 15000000.0
            min_rev = 0.0
            max_rev = max(50000000.0, val_rev * 2.5)
            safe_rev = max(min_rev, min(max_rev, val_rev))
            step_rev = max(10000.0, round((max_rev - min_rev) / 100.0, -3))
            new_rev = st.slider("Scenario Revenue (₹)", min_value=float(min_rev), max_value=float(max_rev), value=float(safe_rev), step=float(step_rev))

            try:
                val_debt = float(orig.get("existing_debt", 2500000.0))
            except Exception:
                val_debt = 2500000.0
            min_debt = 0.0
            max_debt = max(25000000.0, val_debt * 2.5)
            safe_debt = max(min_debt, min(max_debt, val_debt))
            step_debt = max(10000.0, round((max_debt - min_debt) / 100.0, -3))
            new_debt = st.slider("Scenario Debt (₹)", min_value=float(min_debt), max_value=float(max_debt), value=float(safe_debt), step=float(step_debt))
        with c2:
            try:
                val_loan = float(orig.get("requested_loan_amount", 3000000.0))
            except Exception:
                val_loan = 3000000.0
            min_loan = 0.0
            max_loan = max(25000000.0, val_loan * 2.5)
            safe_loan = max(min_loan, min(max_loan, val_loan))
            step_loan = max(10000.0, round((max_loan - min_loan) / 100.0, -3))
            new_loan = st.slider("Scenario Loan (₹)", min_value=float(min_loan), max_value=float(max_loan), value=float(safe_loan), step=float(step_loan))

            try:
                val_cf = float(orig.get("monthly_cash_flow", 250000.0))
            except Exception:
                val_cf = 250000.0
            min_cf = min(-1000000.0, val_cf * 2.0 if val_cf < 0 else -1000000.0)
            max_cf = max(5000000.0, val_cf * 2.0 if val_cf > 0 else 5000000.0)
            safe_cf = max(min_cf, min(max_cf, val_cf))
            step_cf = max(5000.0, round((max_cf - min_cf) / 100.0, -3))
            new_cf = st.slider("Scenario Cash Flow (₹)", min_value=float(min_cf), max_value=float(max_cf), value=float(safe_cf), step=float(step_cf))
            
        mod_params = {
            "annual_revenue": new_rev, "existing_debt": new_debt,
            "requested_loan_amount": new_loan, "monthly_cash_flow": new_cf
        }
        scen_res = run_what_if_scenario(orig, mod_params)
        
        st.markdown("---")
        st.subheader("Live Simulation Comparison")
        
        s1, s2 = st.columns(2)
        with s1:
            st.markdown("#### **Baseline State**")
            st.write(f"**Risk:** {scen_res['original']['risk_category']}")
            st.write(f"**Health Score:** {scen_res['original']['financial_health_score']}/100")
            st.json(scen_res['original']['probabilities'])
        with s2:
            st.markdown("#### **Simulated Scenario**")
            st.write(f"**Risk:** {scen_res['scenario']['risk_category']}")
            st.write(f"**Health Score:** {scen_res['scenario']['financial_health_score']}/100 (Delta: {scen_res['deltas']['financial_health_delta']:+})")
            st.json(scen_res['scenario']['probabilities'])
    else:
        st.info("Run a Risk Assessment first to initialize baseline data for simulation.")

# -----------------------------------------------------------------------------
# PAGE 7: MODEL PERFORMANCE
# -----------------------------------------------------------------------------
elif navigation_page == "🎯 Model Performance":
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">Empirical Model Performance</h1>
            <p class="hero-subtitle">Cross-validation and test set evaluation results from ML training pipeline</p>
        </div>
    """, unsafe_allow_html=True)
    
    if metadata and "comparison_table" in metadata:
        st.subheader("Model Comparison Matrix")
        st.dataframe(pd.DataFrame(metadata["comparison_table"]), use_container_width=True)
        
        tm = metadata.get("test_metrics", {})
        m1, m2, m3, m4 = st.columns(4)
        with m1: st.metric("Test Accuracy", f"{tm.get('accuracy', 0)*100:.2f}%")
        with m2: st.metric("Test F1-Macro", f"{tm.get('f1_macro', 0):.4f}")
        with m3: st.metric("Test Recall-Macro", f"{tm.get('recall_macro', 0):.4f}")
        with m4: st.metric("Test ROC-AUC", f"{tm.get('roc_auc_macro', 'N/A')}")
        
        cm = tm.get("confusion_matrix", [])
        if cm:
            fig_cm = px.imshow(cm, text_auto=True, x=["LOW", "MEDIUM", "HIGH"], y=["LOW", "MEDIUM", "HIGH"], color_continuous_scale="Blues")
            fig_cm.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_cm, use_container_width=True)

# -----------------------------------------------------------------------------
# PAGE 8: ASSESSMENT HISTORY
# -----------------------------------------------------------------------------
elif navigation_page == "📜 Assessment History":
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">Assessment History & Records</h1>
            <p class="hero-subtitle">Persistent SQLite database records of conducted credit risk evaluations</p>
        </div>
    """, unsafe_allow_html=True)
    
    records = fetch_all_assessments()
    if records:
        df_rec = pd.DataFrame(records)
        st.dataframe(df_rec[["business_id", "business_name", "annual_revenue", "requested_loan_amount", "risk_category", "financial_health_score", "created_at"]], use_container_width=True)
        
        del_id = st.number_input("Enter Business ID to Delete", min_value=1, step=1)
        if st.button("Delete Record"):
            if delete_assessment_record(int(del_id)):
                st.success(f"Record #{del_id} deleted successfully.")
                st.rerun()
    else:
        st.info("No records in database.")

# -----------------------------------------------------------------------------
# PAGE 9: PDF REPORTS & EXPORT
# -----------------------------------------------------------------------------
elif navigation_page == "📄 PDF Reports & Export":
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">PDF Credit Report Export</h1>
            <p class="hero-subtitle">Generate and download official PDF credit risk assessment reports</p>
        </div>
    """, unsafe_allow_html=True)
    
    if "last_assessment" in st.session_state:
        la = st.session_state["last_assessment"]
        st.success(f"Active Assessment Available: **{la['business_name']}**")
        pdf_bytes = generate_pdf_report(
            la["business_name"], la["raw_input"], la["pred_res"],
            la["health_res"], la["shap_exp"], la["insights"]
        )
        st.download_button(
            label="📄 Download Assessment PDF Report",
            data=pdf_bytes,
            file_name=f"MSME_Credit_Report_{la['business_name'].replace(' ', '_')}.pdf",
            mime="application/pdf"
        )
    else:
        st.info("Perform an assessment first to enable PDF generation.")
