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
    driver.get(url)

    # Устанавливаем ожидание появления кнопки
    btn = WebDriverWait(driver,wait_time).until(EC.presence_of_element_located((By.ID,button_id)))

    # Ожидаем появления кнопки с указанным ID и кликаем на нее
    btn.click()

except TimeoutException as e:
    # Выводим сообщение, если кнопка не появилась в течение заданного времени
    print(f"Button is not appear duting waiting time. - {e}")

finally:
    # Закрываем веб-драйвер
    driver.quit()
