# Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
# i. текстовое поле username
# ii. текстовое поле password
# iii. кнопку submit
# c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def check_elements():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")

        if username_field and password_field and submit_button:
            print("Элементы найдены")
    except Exception as e:
        print("Элементы не найдены:", e)
    finally:
        driver.quit()


check_elements()
