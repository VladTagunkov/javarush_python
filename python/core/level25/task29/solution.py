from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открытие страницы
driver.get('https://example.com/dynamic_content')

# Ищем первый элемент h1 и выводим его текст
elem = driver.find_element(By.TAG_NAME,'h1').text
print(elem)

# Закрываем браузер
driver.quit()
