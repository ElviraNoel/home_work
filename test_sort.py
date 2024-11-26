import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()  # Make sure to have the correct WebDriver for your browser
driver.get("https://demoqa.com/webtables")


WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "rt-table")))


headers = driver.find_elements(By.XPATH, "//div[@class='rt-resizable-header-content']")


for header in headers:
    header.click()  # Click the header to sort
    time.sleep(1)  # Wait for the sorting to take effect

  
    rows = driver.find_elements(By.XPATH, "//div[@class='rt-tbody']//div[@class='rt-tr-group']")
  
    first_row_class = rows[0].get_attribute("class")
    print(f"Sorting by '{header.text}' resulted in first row class: {first_row_class}")

    
    header.click()
    time.sleep(1)  

driver.quit()
