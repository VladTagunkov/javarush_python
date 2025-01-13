from selenium import webdriver
from selenium.webdriver.common.by import By
# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открываем веб-страницу
driver.get("http://example.com/start-page")

# Здесь можно добавить любые дополнительные действия, если необходимо


# Закрываем браузер
driver.quit()
