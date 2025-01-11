from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открытие веб-страницы
driver.get("https://example.com")

# Поиск всех элементов с тегом 'a'
elems = driver.find_elements(By.CSS_SELECTOR,'a')

# Извлечение атрибутов href и вывод их на экран
for elem in elems:
    tag = elem.get_attribute('href')
    print(tag)

# Закрытие браузера
driver.quit()
