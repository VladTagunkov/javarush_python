from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# URL страницы и ID кнопки
url = "http://example.com"  # Замените на нужный URL
button_id = "dynamic-button-id"  # Замените на нужный ID кнопки
wait_time = 10  # Время ожидания кнопки в секундах

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

try:
    # Открываем URL


    # Устанавливаем ожидание появления кнопки


    # Ожидаем появления кнопки с указанным ID и кликаем на нее


except :
    # Выводим сообщение, если кнопка не появилась в течение заданного времени


finally:
    # Закрываем веб-драйвер
    driver.quit()
