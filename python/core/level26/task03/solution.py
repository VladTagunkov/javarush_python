from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка драйвера Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открытие локальной HTML-страницы


    # Поиск полей формы


    # Заполнение формы


    # Имитирование нажатия кнопки "Submit"


    # Небольшая задержка, чтобы увидеть результат


finally:
    # Закрытие браузера
    driver.quit()
