with open('/Users/avinashsharma/msme_credit_risk_assistant/generate_expanded_final_report.py', 'a') as f:
    f.write('''
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

add_bullet("2. Operational Informality and Accounting Heterogeneity:", "Unlike listed corporations adhering to standardized Ind-AS double-entry accounting certified by statutory auditors, micro and small businesses maintain heterogeneous, fragmented operational ledgers. Many enterprises conduct a substantial fraction of transactions in cash or through fragmented digital wallets, resulting in official financial statements that fail to reflect the enterprise\'s true operational cash velocity.")

add_bullet("3. Backward-Looking Commercial Credit Bureaus:", "Commercial credit bureaus (such as CIBIL Commercial, CRIF High Mark, and Experian Commercial) evaluate creditworthiness strictly through historical debt repayment records. Nascent enterprises under three years of age, first-generation entrepreneurs, and newly formalized businesses suffer from 'thin credit files' or complete absence of bureau footprints, triggering automatic algorithm rejection under standard bank scorecards.")

add_bullet("4. Prohibitive Underwriting and Appraisal Overhead:", "Evaluating a commercial credit application traditionally requires physical branch visits, on-site inventory audits, physical ledger scrutiny, and qualitative committee deliberation. The administrative processing expense of this manual workflow is largely fixed, making small-ticket loan applications (between ₹10 Lakh and ₹50 Lakh) economically unviable for commercial banks relative to large corporate exposures.")

add_heading2("1.3 EVOLUTION OF CREDIT UNDERWRITING: FROM 5 CS TO AUTOMATED ML")
add_body("To appreciate the necessity of machine learning in modern risk appraisal, it is instructive to examine the historical evolution of credit underwriting. For decades, commercial credit assessment rested upon the qualitative '5 Cs of Credit' framework: Character (reputation and integrity of the borrower), Capacity (cash flow ability to service debt), Capital (promoter equity stake), Collateral (pledged asset security), and Conditions (economic and industry environment). While philosophically sound, the operational execution of the 5 Cs was intensely subjective, highly susceptible to loan officer bias, and prone to severe cyclical inconsistency.")

add_body("During the late 20th century, statistical credit scoring emerged through linear discriminant analysis (e.g., the Altman Z-score) and logistic regression scorecards. These models transformed qualitative inquiries into objective point-based scores. However, classical statistical scorecards rely on rigid linear and additive assumptions. They assume that risk increases monotonically with debt and decreases linearly with revenue, completely failing to capture the complex, non-linear interactions characteristic of real-world enterprise operations—such as high operating leverage amplifying seasonal sales dips, or rapid revenue expansion masking severe working capital depletion.")

add_body("Modern machine learning offers the mathematical capacity to model multi-dimensional non-linear interactions, high-degree feature correlations, and heterogeneous operational metrics without imposing artificial distributional assumptions. By automating the extraction of non-linear financial ratios and operational relationships, machine learning transforms credit underwriting from a weeks-long manual investigation into an instantaneous, objective, data-driven analytical process.")

add_heading2("1.4 REGULATORY FRAMEWORK & SUPERVISORY COMPLIANCE")
add_body("While machine learning provides unprecedented predictive precision, deploying automated decision systems in commercial finance is strictly bounded by statutory financial regulations. In the international banking context, the Basel Committee on Banking Supervision (BCBS) under the Basel II and Basel III frameworks establishes rigorous criteria for Internal Ratings-Based (IRB) credit assessment systems. Key regulatory mandates include:")

add_bullet("• Minimum Capital Adequacy and Risk Calibration:", "Banks must demonstrate that their internal credit risk models output calibrated default probabilities that accurately reflect empirical default frequencies across distinct economic cycles.")

add_bullet("• Prohibition of Arbitrary Black-Box Discrimination:", "Under the Equal Credit Opportunity Act (ECOA) and the Reserve Bank of India\'s Fair Lending Practices Code, credit providers are legally prohibited from rejecting loan applicants based on opaque, inexplicable algorithmic outputs. Financial institutions must provide specific, legitimate, and actionable reasons for adverse credit decisions (Adverse Action Notices).")

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

add_body("phi_i(x) = sum_{S subseteq F \\ {i}} [ |S|! (|F| - |S| - 1)! / |F|! ] * [ f_{S cup {i}}(x_{S cup {i}}) - f_S(x_S) ]")

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

add_body("1. Bussmann et al. (2021) [Primary Base Paper]: In 'Explainable Machine Learning in Credit Risk Management' (Computational Economics), the authors investigated the tension between the predictive prowess of machine learning ensembles and regulatory transparency mandates. Analyzing a proprietary dataset of European small and medium enterprises, they demonstrated that Shapley Additive explanations (TreeSHAP) could decompose complex gradient-boosted trees and random forest predictions into exact feature attributions, satisfying supervisory explainability guidelines. However, their research remained strictly an offline analytical study, omitting interactive software implementations, real-time counterfactual simulations, or automated borrower remediation guidance.")

add_body("2. Chawla et al. (2002): In their seminal work 'SMOTE: Synthetic Minority Over-sampling Technique' (Journal of Artificial Intelligence Research), the authors established that simple random over-sampling of minority instances leads to severe model overfitting. By synthesizing artificial minority instances along feature line segments between k-nearest neighbors, SMOTE achieved substantial improvements in minority-class recall. Crucially, the authors cautioned that resampling must never touch validation or test data—a foundational principle strictly enforced in our zero-leakage pipeline design.")

add_body("3. Ciampi et al. (2020): In 'SME Default Prediction with Machine Learning' (European Journal of Operational Research), Ciampi and colleagues benchmarked traditional linear models against tree ensembles across thousands of Italian manufacturing SMEs. Their empirical findings proved that engineered financial ratios—specifically cash flow coverage and debt solvency indicators—dramatically outperformed raw balance sheet quantities. However, their models produced static binary default outputs without actionable borrower feedback.")

add_body("4. Lundberg and Lee (2017): In 'A Unified Approach to Interpreting Model Predictions' (NeurIPS), the authors proposed the SHAP framework, proving that Shapley values represent the unique class of additive feature attributions satisfying local accuracy, missingness, and consistency. Their mathematical proof provides the theoretical bedrock for our local explainability module.")

add_body("5. Altman (1968): In 'Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy' (The Journal of Finance), Edward Altman pioneered the multi-variable Z-score model using Multiple Discriminant Analysis (MDA). While historically revolutionary, Altman\'s formulation enforces rigid linear assumptions that break down when applied to heterogeneous micro-enterprises.")

add_body("6. He et al. (2008): In 'ADASYN: Adaptive Synthetic Sampling Approach for Imbalanced Learning' (IEEE World Congress on Computational Intelligence), the authors introduced an adaptive sampling approach that weights minority instances by their learning difficulty, focusing synthesis along complex decision boundaries.")

add_body("7. Reserve Bank of India (2019): In the 'Report of the Expert Committee on Micro, Small and Medium Enterprises' (chaired by U. K. Sinha), the committee highlighted the massive ₹25 Trillion credit gap in India\'s MSME sector, recommending the urgent adoption of automated, data-driven credit appraisal mechanisms.")

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
    ["Bussmann et al. (2021)", "Shapley Values (SHAP) + XGBoost on European SMEs", "SHAP uncovers non-linear risk drivers; meets supervisory transparency guidelines.", "Transformed offline study into real-time interactive web app with What-If counterfactuals."],
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
''')
print("Successfully wrote append_chapters_1_to_3.py")
