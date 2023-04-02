from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from cookies import cookies

# Configure the web driver (in this case, Chrome)
options = ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = Chrome(options=options)

driver.get("https://soap2day.to")

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# If a button with the text "Home" exists, click it
continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Home')]")))
if continue_button:
    continue_button.click()

# Extract the page source and parse it with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
links = soup.find_all('a', href=True)
print(links)

# Close the web driver
driver.quit()
