import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

# Настройка логирования
logging.basicConfig(level=logging.INFO)

try:
    logging.info("Create browser.")
    # Создаем экземпляр драйвера браузера
    driver = webdriver.Chrome()
    
    logging.info("Get page")
    # Открытие страницы
    driver.get('https://example.com')

    # Задержка для загрузки страницы
    time.sleep(2)
    
    logging.info("Find button to click")
    # Поиск элемента по id и взаимодействие с ним
    btn = driver.find_element(By.ID,'next')
    
    logging.info("Click the button")
    # Пример взаимодействия (например, клик)
    btn.click()

except NoSuchElementException as e:
    driver.save_screenshot("no_element_found.png")
    logging.error(f"We have no find element error - {e}")
    

except Exception as e:
    driver.save_screenshot("other_exception.png")
    logging.error(f"We have other exception - {e}")

finally:
    # Закрытие браузера
    logging.info("Browser closed")
    driver.quit()