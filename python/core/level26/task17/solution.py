import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()
driver.get('https://example.com/login')

# Невероятно важно подождать, чтобы элементы загрузились
time.sleep(3)

# Поиск поля для логина и ввод логина
login_ = driver.find_element(By.NAME,'username')
login_.send_keys("test_user")

# Поиск поля для пароля и ввод пароля
pass_ = driver.find_element(By.NAME,'password')
pass_.send_keys("test_password")

# Поиск кнопки входа и её нажатие
bt_ = driver.find_element(By.NAME,'submit')
bt_.click()


# Подождите немного, чтобы увидеть, что произошло
time.sleep(4)

# Закрытие браузера
drive.quit()