from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Установка и настройка веб-драйвера Chrome
driver_service = Service(ChromeDriverManager().install())

# Инициализация браузера с использованием Selenium
driver = webdriver.Chrome(service=driver_service)

# Открытие указанной веб-страницы
driver.get("http://example.com")



