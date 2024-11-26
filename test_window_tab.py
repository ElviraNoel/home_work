from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

try:
  
    driver.get("https://demoqa.com/links")

   
    home_link = driver.find_element(By.LINK_TEXT, "Home")

   
    assert home_link.text == "Home", "Link text does not match expected value."


    assert home_link.get_attribute("href") == "https://demoqa.com", "Link href does not match expected value."


    home_link.click()

    time.sleep(2)


    driver.switch_to.window(driver.window_handles[1])

    
    assert driver.current_url == "https://demoqa.com", "New tab URL does not match expected value."
  print("All assertions passed. Test case executed successfully.")

finally:
  
    driver.quit()

    print("All assertions passed. Test case executed successfully.")

finally:
   
    driver.quit()
