import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# URL, имя поля ввода, текст для ввода и ID кнопки
url = "http://example.com"  # Замените на нужный URL
input_name = "exampleInputName"  # Замените на нужное имя поля ввода
input_text = "Hello, Selenium!"  # Текст для ввода
button_id = "exampleButtonId"  # Замените на нужный ID кнопки

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открываем указанную веб-страницу
driver.get(url)

# Ждем, чтобы страница полностью загрузилась
time.sleep(3)

# Находим поле ввода по имени и вводим текст
entr_field = driver.find_element(By.NAME,input_name)
entr_field.send_keys(input_text)

# Находим кнопку по ID и нажимаем на нее
id_but = driver.find_element(By.ID,button_id)
id_but.click()

# Ждем, чтобы увидеть результат
time.sleep(3)

# Закрываем браузер
driver.quit()
