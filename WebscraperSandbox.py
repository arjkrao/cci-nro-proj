'''from pdfquery import PDFQuery
import requests
from io import BytesIO
from lxml import etree

# Download the PDF (if necessary)
pdf_url = "https://static.e-publishing.af.mil/production/1/af_a4/publication/afi20-110/afi20-110.pdf"
response = requests.get(pdf_url)
pdf_file = BytesIO(response.content)

# Load the PDF into PDFQuery
pdf = PDFQuery(pdf_file)
pdf.load()
print(etree.tostring(pdf.tree, pretty_print=True))
# Extract the text in the type Ltextlinehorizontal
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements.items()]

print(text)'''

'''import PyPDF2
import requests
import io

url = "https://static.e-publishing.af.mil/production/1/af_a4/publication/afi20-110/afi20-110.pdf"

response = requests.get(url)
f = io.BytesIO(response.content)
reader = PyPDF2.PdfReader(f)
pages = reader.pages
# get all pages data
text = "".join([page.extract_text() for page in pages])

print(text)

#Initial pdf scraping, just downladed some libraries and currently getting all text from 
#one of those example air force pages

'''

import os
import requests
from pdfminer.high_level import extract_text

def download_pdf(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

def pdf_to_text(filename):
    return extract_text(filename)

def extract_section(text, start_keyword, end_keyword=None):
    start_index = text.find(start_keyword)
    if start_index == -1:
        return "Section not found"
    if end_keyword:
        end_index = text.find(end_keyword, start_index)
        return text[start_index:end_index] if end_index != -1 else text[start_index:]
    else:
        return text[start_index:]

def process_pdfs(pdf_urls, download_path, start_keyword, end_keyword=None):
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    for i, url in enumerate(pdf_urls):
        filename = os.path.join(download_path, f"document_{i}.pdf")
        download_pdf(url, filename)
        text = pdf_to_text(filename)
        print(text)
        section = extract_section(text, start_keyword, end_keyword)
        print(f"--- Extracted Section from {filename} ---")
        print(section)
        # Optionally, save the section to a file or further process it here

#tests


# Example usage
pdf_urls = ['https://static.e-publishing.af.mil/production/1/af_a4/publication/afi20-110/afi20-110.pdf', 'https://static.e-publishing.af.mil/production/1/saf_cn/publication/afi33-320/afi33-320.pdf']
process_pdfs(pdf_urls, 'downloaded_pdfs', 'ROLES AND RESPONSIBILITIES', 'Qualifications')