from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (e.g., for Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get('www.cmrcet.ac.in')

# Locate an element using different methods
element_by_id = driver.find_element(By.ID, 'element_id')
element_by_name = driver.find_element(By.NAME, 'element_name')
element_by_xpath = driver.find_element(By.XPATH, '//*[@id="element_id"]')

# Perform actions on the element (e.g., click, send keys)
element_by_id.click()

# Close the WebDriver
driver.quit()
