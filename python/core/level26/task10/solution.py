from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Загрузка веб-страницы
driver.get('http://example.com')

# Поиск элементов по CSS-селектору
elems = driver.find_elements(By.CSS_SELECTOR,'selector')

# Извлечение и вывод текстов элементов
elem_text_list = []
for elem in elems:
    elem_text_list.append(elem.text)

print(elem_text_list)
# Закрытие браузера
driver.quit()

