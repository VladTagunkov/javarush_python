from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открываем веб-страницу по переданному URL
driver.get("https://www.wikipedia.org")

# Ищем первый элемент с тегом <h1> и извлекаем его текст
elem = driver.find_element(By.TAG_NAME,'h1').text

# Выводим текст элемента h1
print(elem)

# Закрываем браузер
driver.quit()
