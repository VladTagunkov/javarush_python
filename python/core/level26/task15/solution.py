import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открываем веб-страницу с формой
driver.get('http://example.com')

# Находим выпадающий список по его идентификатору и выбираем элемент
drop = Select(driver.find_element(By.ID,'drop_id'))
drop.select_by_visible_text('Option 1')

# Находим текстовую область по ее идентификатору и вводим текст
txt_area = driver.find_element(By.ID,"text_area")
txt_area.send_keys("Enter new text")

# Находим кнопку отправки формы по ее идентификатору и кликаем на нее
send_bt = driver.find_element(By.ID,'send_bt')
send_bt.click()

# Даем некоторое время, чтобы убедиться в отправке формы
time.sleep(3)

# Закрываем браузер
driver.quit()
