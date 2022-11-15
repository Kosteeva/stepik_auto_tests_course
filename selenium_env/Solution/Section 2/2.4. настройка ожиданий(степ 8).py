from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(link)

    price = WebDriverWait(driver, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    btn = driver.find_element(By.ID, 'book')
    btn.click()

    value = driver.find_element(By.ID, 'input_value')
    x = value.text
    y = calc(x)

    field = driver.find_element(By.ID, 'answer')
    field.send_keys(y)

    submit = driver.find_element(By.ID, 'solve')
    submit.click()
    print(driver.switch_to.alert.text.split()[-1])
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()


