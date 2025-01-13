from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL и количество страниц
URL = "https://example.com/page"
total_pages = 5  # Задаем общее количество страниц для сбора данных

def setup_driver():
    """Инициализирует и возвращает ChromeDriver."""
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        logging.info("Веб-драйвер Chrome успешно инициализирован.")
        return driver
    except WebDriverException as e:
        logging.error("Ошибка при инициализации ChromeDriver: %s", e)
        return None

def collect_data_from_page(driver):
    """Собирает данные из элементов с идентификатором 'data_item' на текущей странице."""
    data_items = []
    try:
        elements = driver.find_elements(By.ID, "data_item")
        data_items = [element.text for element in elements]
        logging.info("Собрано %d элементов данных на текущей странице.", len(data_items))
    except NoSuchElementException:
        logging.warning("Элементы с идентификатором 'data_item' не найдены на текущей странице.")
    return data_items

def go_to_next_page(driver, page_number):
    """Переходит на указанную страницу, используя нумерованные ссылки."""
    try:
        next_page_link = driver.find_element(By.LINK_TEXT, str(page_number))
        next_page_link.click()
        logging.info("Перешел на страницу %d.", page_number)
        return True
    except NoSuchElementException:
        logging.warning("Ссылка на страницу %d не найдена.", page_number)
        return False

def main():
    driver = setup_driver()
    driver.get(URL)
    res = []
    page_num = 1
    try:
        while True:
           res += collect_data_from_page(driver)
           if not go_to_next_page(driver,page_num):
               break 
           time.sleep(3)
           page_num += 1
    finally:
        print(res)
        driver.quit()



  

main()
