# Required Libraries: Selenium, Chrome Driver, and Beautiful Soup. 

# ChromeDriver is a separate executable that Selenium WebDriver uses to control Chrome to scrape websites.
# BeautifulSoup extracts content from HTML pages. 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
import random
import requests


# Configuring the options for the Chrome WebDriver in Selenium. 
options = Options()
# Runs the browser in "headless" mode, meaning the browser's graphical user interface is not displayed.  
options.add_argument('--headless')
# Opens the browser in incognito mode to avoid tampering with browsing history. 
options.add_argument("--incognito")
# Disables the use of GPU (Graphics Processing Unit) acceleration in the browser  to prevent compatibility issues.
options.add_argument('--disable-gpu')
# Disables the sandboxing of the browser process to avoid issues. 
options.add_argument('--no-sandbox')
# Disables the use of the "/dev/shm" shared memory space to prevent memory allocation issues.
options.add_argument('--disable-dev-shm-usage')
# Twitter uses JavaScript. This option enables JavaScript execution in the browser to ensure the page is functional. 
options.add_argument('--enable-javascript')





# Selecting a random URL to scrape data from. No information about the user is displayed in the output. 
url = "https://amchainitiative.org/search-by-incident#incident/display-by-date/"
# Establishes chrome driver and leads to URL
driver = webdriver.Chrome(options=options)
driver.get(url)


try:
    # Wait for up to 60 seconds for the presence of a specific element on the page
    WebDriverWait(driver, 60).until(
        # Check for the presence of a tweet
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]'))
    )
except (WebDriverException, TimeoutException) as e:
    # Prints error message if an exception occurs while waiting for the element or if a timeout occurs
    print("An error occurred while waiting for tweets to load:", str(e))
    # Close the browser window (WebDriver)
    driver.quit()
    # Exit the script immediately
    exit()

# Capture HTML after loading
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')

# Find all tweet text elements
posts = soup.find_all(attrs={'data-testid': 'tweetText'})

# Display error message if no tweets are found. 
if not posts:
    print("No tweets found.")

driver.quit()