import PyPDF2
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

