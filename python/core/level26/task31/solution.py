from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Базовый URL и количество страниц для обработки
BASE_URL = "https://example.com/page/"
TOTAL_PAGES = 5  # Задаем общее количество страниц для обхода

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

def collect_data_from_page(driver, page_number):
    """Собирает данные с элементов класса 'content_item' на текущей странице."""
    data_items = []
    try:
        elements = driver.find_elements(By.CLASS_NAME, "content_item")
        data_items = [element.text for element in elements]
        logging.info("Собрано %d элементов данных на странице %d.", len(data_items), page_number)
    except NoSuchElementException:
        logging.warning("Элементы с классом 'content_item' не найдены на странице %d.", page_number)
    return data_items

def main():
    driver = setup_driver()
    res_d = {}
    try:
        for page in range(1,TOTAL_PAGES+1):
            url = f"{BASE_URL}{page}"
            driver.get(url)
            page_data = collect_data_from_page(driver,page)
            res_d[page] = page_data
            time.sleep(2)
    finally:
        print(res_d)
        driver.quit()
main()

