

import requests
from pdfminer.high_level import extract_text
import io

# Download the PDF
pdf_url = "https://static.e-publishing.af.mil/production/1/lemay_center/publication/afi10-1302/afi10-1302.pdf"
response = requests.get(pdf_url)
pdf_bytes = io.BytesIO(response.content)

# Extract text from the PDF
text = extract_text(pdf_bytes)

# Define start and end markers for the section
start_marker = "ROLES AND RESPONSIBILITIES"
end_markers = ["REFERENCES", "GLOSSARY"]  # Common sections that might follow the target section

# Find the start of the "ROLES AND RESPONSIBILITIES" section
start_index = text.find(start_marker)

# Skip the table of contents by finding the second occurrence
start_index = text.find(start_marker, start_index + 1)

# Adjust the end markers to include "Chapter 3 COLLECTIONS"
end_markers = ["Chapter 3","REFERENCES", "GLOSSARY"]

# Find the earliest occurrence of any end marker after the start of the "ROLES AND RESPONSIBILITIES" section
end_index = min([text.find(marker, start_index + 1) for marker in end_markers if text.find(marker, start_index + 1) != -1])

# Extract and print the "ROLES AND RESPONSIBILITIES" section, stopping before "Chapter 3 COLLECTIONS"
roles_text = text[start_index:end_index].strip() if end_index != -1 else text[start_index:].strip()
print(roles_text)