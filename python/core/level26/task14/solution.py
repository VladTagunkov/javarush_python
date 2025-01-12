from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открытие веб-страницы формы опроса
driver.get('http://example.com')

# Явное ожидание загрузки текстового поля
time.sleep(3)

# Ввод текста в текстовое поле
text_fi = driver.find_element(By.NAME,'text_field_name')
text_fi.send_keys('new_text_value')

# Поиск и выбор радиокнопки
radio_bt = driver.find_element(By.ID,'radio_btn')
if not radio_bt.is_selected():
    radio_bt.click()

# Поиск и выбор флажка
check_bt = driver.find_element(By.ID,'checkbox_id')
if not check_bt.is_selected():
    check_bt.click()
    
# Поиск кнопки отправки и отправка формы
send_bt = driver.find_element(By.NAME,'send')
send_bt.click()

# Закрытие веб-драйвера
driver.quit()
