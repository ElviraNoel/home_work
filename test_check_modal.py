import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestModalDialogs(unittest.TestCase):
    def setUp(self):
       
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://demoqa.com/modal-dialogs")
        self.driver.maximize_window()

    def test_small_modal(self):
       
        small_modal_button = self.driver.find_element(By.ID, "showSmallModal")
        small_modal_button.click()
        
       
        time.sleep(1)  # This is a simple wait; consider using WebDriverWait for better practice
        
       
        small_modal = self.driver.find_element(By.CLASS_NAME, "modal-dialog")
        self.assertTrue(small_modal.is_displayed(), "Small modal is not displayed")
      
        close_button = self.driver.find_element(By.ID, "closeSmallModal")
        close_button.click()
        
        
        time.sleep(1)

    def test_large_modal(self):
       
        large_modal_button = self.driver.find_element(By.ID, "showLargeModal")
        large_modal_button.click()
        
       
        time.sleep(1) 
        
        
        large_modal = self.driver.find_element(By.CLASS_NAME, "modal-dialog")
        self.assertTrue(large_modal.is_displayed(), "Large modal is not displayed")
        
        
        close_button = self.driver.find_element(By.ID, "closeLargeModal")
      close_button.click()
        
        
        time.sleep(1)

    def tearDown(self):
       
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
