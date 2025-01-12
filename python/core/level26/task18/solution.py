import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# URL и данные для авторизации
url = 'https://example.com/login'
username = 'test_user'
password = 'test_password'

def setup_driver():
    """Устанавливает и настраивает ChromeDriver."""
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        return driver
    except WebDriverException as e:
        logging.error("Ошибка при инициализации ChromeDriver: %s", e)
        return None

def login(driver, url, username, password):
    """Выполняет авторизацию на сайте."""
    try:
        logging.info('We open auth page.')
        # Открытие страницы авторизации
        driver.get(url)

        logging.info('We enter login.')
        # Ввод логина
        username_field = driver.find_element(By.NAME, "username")  # Используем NAME как пример, адаптируйте к странице
        username_field.send_keys(username)

        logging.info('We enter password.')
        # Ввод пароля
        password_field = driver.find_element(By.NAME, "password")  # Используем NAME как пример, адаптируйте к странице
        password_field.send_keys(password)

        logging.info('We press the button.')
        # Нажатие на кнопку входа
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Предполагаем, что это кнопка входа
        login_button.click()


    except WebDriverException as e:


driver = setup_driver()
if driver:
    login(driver, url, username, password)
    driver.quit()

else:
