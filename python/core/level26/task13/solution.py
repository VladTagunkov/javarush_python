import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открытие страницы с формой входа
driver.get('http://example.com')

# Поиск поля для ввода имени пользователя и ввод значения
fi_name = driver.find_element(By.NAME,'name')
fi_name.send_keys('new_name')

# Поиск поля для ввода пароля и ввод значения
fi_pass = driver.find_element(By.NAME,'password')
fi_pass.send_keys("new_password")

# Поиск кнопки входа и нажатие на нее
bt_enter = driver.find_element(By.NAME,'enter')
bt_enter.click()

# Время, чтобы увидеть результат (можно убрать в реальном использовании)
time.sleep(3)

# Закрытие веб-драйвера
driver.quit()
