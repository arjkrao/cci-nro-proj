import requests
from pdfminer.high_level import extract_text
import io
import requests


'''# Scrape all the PDF links from a certain site and load them into pdf_urls

# URL of the site to scrape
site_url = "https://example.com"

# Send a GET request to the site
response = requests.get(site_url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the <a> tags with href attribute containing ".pdf"
pdf_links = soup.find_all("a", href=lambda href: href and href.endswith(".pdf"))

# Extract the URLs from the <a> tags and append them to pdf_urls
pdf_urls = [link["href"] for link in pdf_links]

# Print the extracted PDF URLs
print("PDF URLs:")
for url in pdf_urls:
    print(url)'''
pdf_urls = [
    'https://static.e-publishing.af.mil/production/1/lemay_center/publication/afi10-1302/afi10-1302.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-1001/afi10-1001.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4/publication/afi25-101/afi25-101.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-1801/afi10-1801.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-201/afi10-201.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-202/afi10-202.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-204/afi10-204.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4/publication/afi10-210/afi10-210.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-217/afi10-217.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-2402/afi10-2402.pdf',
    'https://static.e-publishing.af.mil/production/1/af_sg/publication/afi10-2519/afi10-2519.pdf',
    'https://static.e-publishing.af.mil/production/1/af_sg/publication/afi10-2606/afi10-2606.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a10/publication/afi10-2607/afi10-2607.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-2912/afi10-2912.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-3005/afi10-3005.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-301/afi10-301.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-3503/afi10-3503.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-3504/afi10-3504.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-402/dafi10-402.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4/publication/afi10-403/afi10-403.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4/publication/afi10-404/afi10-404.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-405/afi10-405.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-420/afi10-420.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-4301v1/afi10-4301v1.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-4301v3/afi10-4301v3.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a5/publication/afi10-601/afi10-601.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-701/afi10-701.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-801/afi10-801.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4/publication/afman10-2502/afman10-2502.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afman10-207/afman10-207.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afman10-206/afman10-206.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afman10-1004/afman10-1004.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3_5/publication/afji10-411/afji10-411.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a5_8/publication/afpd10-6/afpd10-6.pdf',
    'https://static.e-publishing.af.mil/production/1/saf_ie/publication/afpd10-5/afpd10-5.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afpd10-45/afpd10-45.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afpd10-43/afpd10-43.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afpd10-4/afpd10-4.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afpd10-36/afpd10-36.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afpd10-30/afpd10-30.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afpd10-3/afpd10-3.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afpd10-29/afpd10-29.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a10/publication/afpd10-26/afpd10-26.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afpd10-24/afpd10-24.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afpd10-21/afpd10-21.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afpd10-18/afpd10-18.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afpd10-10/afpd10-10.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3_5/publication/afpam10-243/afpam10-243.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4/publication/afpam10-219v9/afpam10-219v9.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4_7/publication/afpam10-219v6/afpam10-219v6.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4_7/publication/afpam10-219v5/afpam10-219v5.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4/publication/afpam10-219v4/afpam10-219v4_airfield_damage_repair_capabilities_(camera_ready).pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4/publication/afpam10-219v3/afpam10-219v3.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4/publication/afpam10-219v2/afpam10-219v2.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4_7/publication/afpam10-219v1/afpam10-219v1.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afpam10-1403/afpam10-1403.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afman10-3511/afman10-3511.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afman10-3509/afman10-3509.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afman10-3507/afman10-3507.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afman10-3505v2/afman10-3505v2.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afman10-3505v1/afman10-3505v1.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afman10-3500v2/afman10-3500v2.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afman10-3500v1/afman10-3500v1.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/afman10-2909/afman10-2909.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a5/publication/dodd3000.7_afpd10-42/dodd3000.07_afpd10-42.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a8/publication/dafpd10-9/dafpd10-9.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/dafpd10-8/dafpd10-8.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/dafpd10-7/afpd10-7.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/dafpd10-35/dafpd10-35.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/dafpd10-27/dafpd10-27.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4/publication/dafpd10-25/dafpd10-25.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/dafpd10-2/dafpd10-2.pdf',
    'https://static.e-publishing.af.mil/production/1/lemay_center/publication/dafpd10-13/dafpd10-13.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/dafpd10-11/dafpd10-11.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a5/publication/dafman10-703/dafman10-703.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a5/publication/dafman10-703/dafman10-703.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/dafman10-406/dafman10-406.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a5/publication/dafi10-706/dafi10-706.pdf',
    'https://static.e-publishing.af.mil/production/1/saf_ie/publication/dafi10-503/dafi10-503.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/dafi10-401/dafi10-401.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/dafi10-3601/dafi10-3601.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/dafi10-3002/dafi10-3002.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/dafi10-3001/dafi10-3001.pdf',
    'https://static.e-publishing.af.mil/production/1/saf_mr/publication/dafi10-2702/dafi10-2702.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a3/publication/dafi10-2701/dafi10-2701.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a10/publication/dafi10-2602/dafi10-2602.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a10/publication/dafi10-2601/dafi10-2601.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4/publication/dafi10-2503/dafi10-2503.pdf',
    'https://static.e-publishing.af.mil/production/1/af_a4/publication/dafi10-2501/dafi10-2501.pdf',
    'https://static.e-publishing.af.mil/production/1/saf_aa/publication/dafi10-208/dafi10-208.pdf'
]

texts = []

for pdf_url in pdf_urls:
    response = requests.get(pdf_url)
    pdf_bytes = io.BytesIO(response.content)

    # Extract text from the PDF
    print(f'--------------{pdf_url}--------------')
    text = extract_text(pdf_bytes)

    # Define start and end markers for the section
    start_marker = "ROLES AND RESPONSIBILITIES"
    end_markers = ["REFERENCES", "GLOSSARY"]  # Common sections that might follow the target section

    # Find the start of the "ROLES AND RESPONSIBILITIES" section
    start_index = text.find(start_marker)

    # Skip the table of contents by finding the second occurrence
    start_index = text.find(start_marker, start_index + 1)

    # Adjust the end markers to include "Chapter 3 COLLECTIONS"
    end_markers = ["Chapter 3","REFERENCES", "GLOSSARY", 'PROGRAM OBJECTIVES']

    # Find the earliest occurrence of any end marker after the start of the "ROLES AND RESPONSIBILITIES" section
    end_index = min([text.find(marker, start_index + 1) for marker in end_markers if text.find(marker, start_index + 1) != -1], default=-1)
    if end_index == -1:
        continue

    # Extract and append the "ROLES AND RESPONSIBILITIES" section, stopping before "Chapter 3 COLLECTIONS"
    roles_text = text[start_index:end_index].strip() if end_index != -1 else text[start_index:].strip()
    texts.append(roles_text)

# Print the extracted sections
for i, text in enumerate(texts):
    print(f"Section {i+1}:")
    print(text)
    print()
