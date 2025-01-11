from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открываем веб-страницу www.example.com
driver.get("http://www.example.com")

# Ищем первый элемент <p> на странице
elem = driver.find_element(By.TAG_NAME,'p')

# Извлекаем текст из найденного элемента
print(elem.text)

# Выводим текст параграфа на экран


# Закрываем браузер
driver.quit()
