from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Path to the ChromeDriver executable
PATH = "C:/chromedriver-win64/chromedriver.exe"

# Create a Service object
service = Service(PATH)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://youtube.com/")  # Method to open ny website
# print(driver.title)   #method to print the title of the website
# driver.close()   #method to close a tab
# driver.quit()    # method to close the whole browser

search = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, 'search_query'))) #this will wait untl the elememt is fount and executed

search = driver.find_element(By.NAME,'search_query')
search.send_keys("test")
search.send_keys(Keys.RETURN)
