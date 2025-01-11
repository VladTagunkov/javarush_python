import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открытие веб-страницы
driver.get("https://example.com/products")

# Необходимо немного подождать, чтобы страница полностью загрузилась
time.sleep(3)

# Поиск таблицы с классом "product-table"
tabls = driver.find_element(By.CSS_SELECTOR, ".product-table")

# Извлечение данных с использованием XPath
start_xpath = time.time()
#products_xpath_1 = driver.find_elements(By.XPATH, "//table[@class='product-table']//tr")
products_xpath_1 = driver.find_element(By.CSS_SELECTOR, ".product-table")
products_xpath = driver.find_elements(By.ID, ".tr")
xpath_results = []
for product in products_xpath:  # Пропуская заголовок таблицы
    name = product.find_element(By.XPATH, "./td[1]").text
    price = product.find_element(By.XPATH, "./td[2]").text
    print(f"Product: {name}, Price: {price}")


# Закрытие браузера
driver.quit()