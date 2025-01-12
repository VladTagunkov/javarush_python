from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открываем веб-страницу
driver.get("https://www.wikipedia.org")

# Извлекаем все элементы с тегом a
elem_a = driver.find_elements(By.TAG_NAME,'a')

# Собираем все URL из атрибутов href
urls_list = []
for elem in elem_a:
    hr = elem.get_attribute('href')
    urls_list.append(hr)

# Выводим список всех найденных URL
print(urls_list)

# Закрываем драйвер
driver.quit()
