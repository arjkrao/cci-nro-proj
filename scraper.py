from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# URL of the webpage
url = "https://www.e-publishing.af.mil/Product-Index/igphoto/2002044553/#/?view=pubs&orgID=10141&catID=1&series=-1&modID=449&tabID=131"

# Setup Selenium Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Optional: run in headless mode to hide browser window
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # Load the webpage
    driver.get(url)
    
    # Wait for the page to fully render (adjust the timeout as needed)
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
    
    # Find all links on the page
    all_links = driver.find_elements(By.TAG_NAME, 'a')
    
    # Look for the first PDF link
    first_pdf_url = None
    for link in all_links:
        href = link.get_attribute('href')
        if href and href.endswith('.pdf'):
            first_pdf_url = href
            break
    
    if first_pdf_url:
        print("First PDF URL:", first_pdf_url)
    else:
        print("No PDF URLs found on the page.")

finally:
    # Quit the WebDriver
    driver.quit()
