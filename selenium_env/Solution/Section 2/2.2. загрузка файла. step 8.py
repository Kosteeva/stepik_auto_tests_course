import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys("1@mail.ru")

    current_dir = os.path.abspath(os.path.dirname('file.txt'))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    print(file_path)
    f = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    f.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    print(browser.switch_to.alert.text.split()[-1])
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()