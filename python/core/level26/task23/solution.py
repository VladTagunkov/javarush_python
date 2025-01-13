# Импортируем библиотеки для логирования и работы с веб-драйвером
import logging
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Логируем начало инициализации веб-драйвера
logging.info('Webdriver initialize.')

try:
    # Создаем экземпляр драйвера браузера
    driver = webdriver.Chrome()

    # Открытие страницы python.org

    driver.get("https://www.python.org")

    # Извлечение и логирование заголовка страницы
    title = driver.title
    logging.info("We parse page title.")

# Обработка ошибок веб-драйвера
except WebDriverException as e:
    logging.error(f"We have error - {e}")


# Обработка других ошибок
except Exception as e:
    logging.error(f"We have error - {e}")

# Закрытие веб-драйвера и логирование завершения работы скрипта
finally:
    logging.info("Close parser.")
    driver.quit()
    
