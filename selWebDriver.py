from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
#from cookies import cookies

chrome_driver_path = "\chromedriver_win32\chromedriver.exe"

# Configure the web driver (in this case, Chrome)
options = ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(executable_path=chrome_driver_path)
driver = Chrome(options=options, service=service)
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, service=Service(chrome_driver_path))


#get all links in an h5 from the page using beautiful soup
def getLinks(url):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('h5')
    return links


driver.get("https://soap2day.to")

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# If a button with the text "Home" exists, click it
continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Home')]")))
if continue_button:
    continue_button.click()


#if a button with the text "Movies" exists, click it
continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Movies')]")))
if continue_button:
    continue_button.click()

#if a button with the text "IMDB Rating" exists, click it
continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'IMDB Rating')]")))
if continue_button:
    continue_button.click()

disabled = False
while not disabled: 
    try:
        time.sleep(1)
        #get current html
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('h5')
        print(links)
        pagination = soup.find('ul', class_='pagination')
    
        # Find the last li element in the pagination list
        last_li = pagination.find_all('li')[-1]
    
        # Find the li element with the active class
        active_li = soup.find('li', class_='active')
        
        # Get the text of the span element inside it
        highlighted_number = active_li.find('span').text
        
        print(highlighted_number)
    
        # Check if the last li element is disabled
        if 'disabled' in last_li.get('class', []):
            print('The last element is disabled')
            disabled = True
            break;
        else:
            print('The last element is enabled')
            nextPageBtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '»')]")))
            nextPageBtn.click()
        break
    except:
        time.sleep(5)
        driver.refresh()
    
print("End")
# Close the web driver
driver.quit()


#maybe add tinydb for storing information on what has been downloaded already and what hasn't