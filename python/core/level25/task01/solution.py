from selenium import webdriver

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открываем страницу www.example.com
driver.get("http://www.example.com")

# Извлекаем заголовок страницы
print(driver.title)

# Закрываем браузер
driver.quit()

