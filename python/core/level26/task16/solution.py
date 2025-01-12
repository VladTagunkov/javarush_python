from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Путь к файлу, который будет загружен
file_path = "/path/to/your/file.txt"

# URL страницы с формой загрузки файла
url = "http://example.com/upload"

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Переходим на указанную страницу
driver.get(url)

# Ожидаем, пока элемент загрузки файла станет доступным, и находим его
time.sleep(3)
elem = driver.find_element(By.NAME,'file_upload_id')

# Указываем путь к файлу для загрузки
elem.send_keys(file_path)

# Находим и нажимаем кнопку отправки формы
btn_send = driver.find_element(By.NAME,'send')
btn_send.click()

# Ожидаем подтверждение успешной загрузки файла
time.sleep(3)

# Проверяем текст подтверждения
if 'Success' in driver.page_source:
    print("We successfully upload file")
else:
    print("We have error!")

# Закрываем браузер
driver.quit()
