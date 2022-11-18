import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    def test_element(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, "input.first:required")
        input1.send_keys("Bla")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.second:required")
        input2.send_keys("BlaBla")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.third:required")
        input3.send_keys("Bla@bla.com")
        time.sleep(5)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text,"Congratulations! You have successfully registered!", "No text")  # add assertion here


if __name__ == '__main__':
    unittest.main()