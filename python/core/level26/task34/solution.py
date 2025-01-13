from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL страницы, которую нужно открыть
url = 'https://example.com'  # Замените на нужный URL
element_id = 'target-element-id'  # Замените на нужный ID элемента

# Инициализация веб-драйвера (например, для Chrome)
driver = webdriver.Chrome()

try:
    # Открытие веб-страницы
    driver.get(url)

    # Явное ожидание появления элемента с указанным ID
    elem1 = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.ID,element_id)))
    
    # Если элемент найден, выводим сообщение
    print("Элемент найден")

except Exception as e:
    # Обработка исключений, если элемент не найден или возникла другая ошибка
    print("Элемент не найден в течение указанного времени:", e)

finally:
    # Закрытие драйвера
    driver.quit()