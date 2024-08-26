import fitz  # PyMuPDF
import re
from bs4 import BeautifulSoup

# Function to extract and clean text from PDF
def extract_text_from_pdf(pdf_path):
    # Open the PDF
    doc = fitz.open(pdf_path)
    text = ""
    
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        # Extract raw text from the page
        raw_text = page.get_text("text")
        
        # Clean the text (remove unnecessary whitespace, newlines, etc.)
        clean_text = re.sub(r'\n+', '\n', raw_text).strip()
        clean_text = re.sub(r'\s+', ' ', clean_text)
        text += clean_text + "\n"
    
    doc.close()
    return text

# Path to your PDF
pdf_path = 'pp_veg_pbi.pdf'
extracted_text = extract_text_from_pdf(pdf_path)

# Save extracted text to a file
with open('cleaned_punjabi_text.txt', 'w', encoding='utf-8') as f:
    f.write(extracted_text)
