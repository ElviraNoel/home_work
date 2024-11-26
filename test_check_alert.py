import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAlert(unittest.TestCase):
    def setUp(self):
     
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/alerts")

    def test_timer_alert(self):
       
        timer_alert_button = self.driver.find_element(By.ID, "timerAlertButton")
        
      
        self.assertIsNotNone(timer_alert_button, "Timer alert button is not present on the page.")
        
       
        timer_alert_button.click()
  
        time.sleep(5)
        
       
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert text: {alert_text}")
            alert.accept()  # Accept the alert
        except Exception as e:
            self.fail(f"Alert did not appear: {str(e)}")

    def tearDown(self):
        
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
