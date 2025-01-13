from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открываем веб-страницу
driver.get("http://example.com/articles")

# Ищем все элементы с классом "article-title"
art_title = driver.find_elements(By.CLASS_NAME,"article-title")

# Извлекаем и выводим текст каждого заголовка
for title in art_title:
    print(title.text)

# Закрываем драйвер независимо от результата
driver.quit()
