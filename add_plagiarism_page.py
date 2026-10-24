import os
import re

with open('/Users/avinashsharma/msme_credit_risk_assistant/generate_expanded_final_report.py', 'r') as f:
    code = f.read()

# 1. Update Annexure B text with exact iThenticate details from user image
old_annex_b = """add_body("• Project Title: AI-BASED MSME CREDIT RISK ASSISTANT\\n• Candidate Authors: Dhairya Punihani (2314110171), Avinash Sharma (2314110182), Vinay Pratap Singh (2314110217)\\n• Project Guide: Prof. Ruchira Tare\\n• Department: Department of Computer Engineering, BV(DU)COE, Pune\\n• Screening Software: Turnitin Plagiarism Academic Suite\\n• Overall Similarity Index: 8.4% (Permissible University Ceiling: < 15%)\\n• Primary Exclusions: Institutional certificate templates, bibliographical citations, mathematical formulas, and standard statutory clauses.\\n• Verification Status: APPROVED - Fully compliant with institutional originality and research integrity guidelines.\\n• Date of Verification: 20/10/2026")"""

new_annex_b = """add_body("• Project Title: AI-BASED MSME CREDIT RISK ASSISTANT\\n• Candidate Authors: Dhairya Punihani (2314110171), Avinash Sharma (2314110182), Vinay Pratap Singh (2314110217)\\n• Project Guide: Prof. Ruchira Tare\\n• Department: Department of Computer Engineering, BV(DU)COE, Pune\\n• Screening Software: iThenticate / Turnitin Integrity Suite (Page 2 of 51 - Integrity Overview)\\n• Submission ID: trn:oid:::3117342624807\\n• Overall Similarity Index: 7% (Permissible University Ceiling: < 15%)\\n• Top Source Distribution: 1% Internet Sources, 11% Publications, 0% Submitted Works (Student Papers)\\n• Match Groups: 2 Not Cited or Quoted (12%), 0 Missing Quotations (1%), 1 Missing Citation (1%), 0 Cited and Quoted (0%)\\n• Integrity Flags: 0 Integrity Flags for Review (No suspicious text manipulations found)\\n• Verification Status: VERIFIED & APPROVED - Strictly within permissible university guidelines.\\n• Official Verification Certificate: Appended as the final page of this report.")"""

code = code.replace(old_annex_b, new_annex_b)

# 2. Add the iThenticate Certificate page to the very end of the docx (after Annexure D)
old_save_block = """# Save Document to Project Folder and Desktop
print("Saving generated DOCX files...")"""

new_save_block = """# ==============================================================================
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
print("Saving generated DOCX files...")"""

code = code.replace(old_save_block, new_save_block)

# 3. Update TOC to include the Official iThenticate Certificate as the final item
old_toc_annex_d = '["ANNEXURE D: Project Tracker & Milestone Execution Record", "72"]'
new_toc_annex_d = '["ANNEXURE D: Project Tracker & Milestone Execution Record", "72"],\\n    ["Official iThenticate Plagiarism Certificate", "73"]'

code = code.replace(old_toc_annex_d, new_toc_annex_d)

with open('/Users/avinashsharma/msme_credit_risk_assistant/generate_expanded_final_report.py', 'w') as f:
    f.write(code)

print("Updated generate_expanded_final_report.py with iThenticate certificate!")
