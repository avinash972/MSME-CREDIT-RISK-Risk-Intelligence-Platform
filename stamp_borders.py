import os
import shutil
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import pypdf

PDF_SRC = '/Users/avinashsharma/msme_credit_risk_assistant/BTech_Project_Report_MSME_Credit_Risk_Assistant.pdf'
PDF_DEST_PROJ = '/Users/avinashsharma/msme_credit_risk_assistant/BTech_Project_Report_MSME_Credit_Risk_Assistant.pdf'
PDF_DEST_DESK = '/Users/avinashsharma/Desktop/BTech_Project_Report_MSME_Credit_Risk_Assistant.pdf'
TEMP_BORDERED = '/tmp/bordered_final_doc.pdf'

w, h = A4 # 595.27, 841.89

# Create the master double-line border overlay
BORDER_OVERLAY = '/tmp/master_border_overlay.pdf'
c = canvas.Canvas(BORDER_OVERLAY, pagesize=A4)

# Outer Border (1.5 pt black line at 20 pt from page edge)
c.setStrokeColorRGB(0.0, 0.0, 0.0)
c.setLineWidth(1.5)
c.rect(20, 20, w - 40, h - 40)

# Inner Border (0.5 pt black line at 23.5 pt from page edge)
c.setLineWidth(0.5)
c.rect(23.5, 23.5, w - 47, h - 47)

c.save()

# Read the document and overlay the border on EVERY page
reader_doc = pypdf.PdfReader(PDF_SRC)
reader_border = pypdf.PdfReader(BORDER_OVERLAY)
border_page = reader_border.pages[0]

writer = pypdf.PdfWriter()

for idx, page in enumerate(reader_doc.pages):
    page.merge_page(border_page)
    writer.add_page(page)

with open(TEMP_BORDERED, 'wb') as f:
    writer.write(f)

# Replace both destination files with the bordered version
shutil.copyfile(TEMP_BORDERED, PDF_DEST_PROJ)
shutil.copyfile(TEMP_BORDERED, PDF_DEST_DESK)

print(f"Successfully stamped formal double borders onto all {len(writer.pages)} pages of the PDF!")
print(f"1. Updated project PDF: {PDF_DEST_PROJ}")
print(f"2. Updated desktop PDF: {PDF_DEST_DESK}")
