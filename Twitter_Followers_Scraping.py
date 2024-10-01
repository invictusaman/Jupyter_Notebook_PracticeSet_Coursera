# Let us start web scraping
# Write a Python program to get the number of followers of a given twitter account.
# Choose any twitter account of your favorite celebrity.

# Install : pip install selenium
# Also, you need Google Chrome latest version

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

try:
    print("\n")
    username = input("Enter the Twitter username: ")
    URL = f"https://x.com/{username}"

    print(f"\nRedirecting to {URL}")
    driver.get(URL)

    # CSS selector to locate the follower count
    css_selector = f"a[href='/{username}/verified_followers'] > span > span"
    
    # Wait for the element and get the follower count
    followers_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )

    followers_count = followers_element.text
    print(f"\nTwitter account @{username} has {followers_count} followers.\n")

except TimeoutException:
    print("\nSome issues with Twitter profile, not able to fetch followers count. MAKE SURE IT IS PUBLIC!\n")
except Exception as e:
    print(f"\nAn error occurred: {e}\n")

finally:
    driver.quit()
