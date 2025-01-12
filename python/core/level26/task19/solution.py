import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL и данные для авторизации
URL = 'https://example.com/login'
USERNAME = 'test_user'
PASSWORD = 'test_password'

def setup_driver():
    """Устанавливает и настраивает ChromeDriver."""
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        logging.info("Веб-драйвер Chrome успешно инициализирован.")
        return driver
    except WebDriverException as e:
        logging.error("Ошибка при инициализации ChromeDriver: %s", e)
        return None

def open_login_page(driver, url):
    """Открывает страницу авторизации."""
    try:
        driver.get(url)
        logging.info("Открыта страница: %s", url)
    except WebDriverException as e:
        logging.error("Ошибка при открытии страницы %s: %s", url, e)

def enter_credentials(driver, username, password):
    """Вводит логин и пароль в поля ввода."""
    try:
        username_field = driver.find_element(By.NAME, "username")
        username_field.send_keys(username)
        logging.info("Введен логин: %s", username)

        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(password)
        logging.info("Введен пароль.")
    except WebDriverException as e:
        logging.error("Ошибка при вводе учетных данных: %s", e)

def click_login_button(driver):
    """Нажимает кнопку для входа на сайт."""
    try:
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        logging.info("Нажата кнопка для входа на сайт.")
    except WebDriverException as e:
        logging.error("Ошибка при нажатии кнопки входа: %s", e)

def close_driver(driver):
    """Закрывает веб-драйвер."""
    try:
        driver.quit()
        logging.info("Веб-драйвер закрыт.")
    except WebDriverException as e:
        logging.error("Ошибка при закрытии веб-драйвера: %s", e)

def main():
    driver = setup_driver()
    
    try:
        open_login_page(driver,URL)
        enter_credentials(driver, USERNAME, PASSWORD)
        click_login_button(driver)
    finally:
        close_driver()




main()
