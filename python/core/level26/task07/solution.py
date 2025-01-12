import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Откройте веб-страницу с таблицей
driver.get("https://www.wikipedia.org")

# Подождите некоторое время, чтобы страница полностью загрузилась
time.sleep(3)

# Найдите таблицу по идентификатору
tb = driver.find_element(By.ID,'Highest-grossing_films')

# Извлеките все строки таблицы
rows = tb.find_elements(By.TAG_NAME,'tr')

# Закройте драйвер
driver.quit()
