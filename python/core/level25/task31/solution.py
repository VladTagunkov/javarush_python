from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открываем веб-страницу
driver.get('https://example.com')

# Находим таблицу по заданному идентификатору
tb = driver.find_element(By.ID,'table')

# Извлекаем все строки таблицы
rows = tb.find_elements(By.TAG_NAME,'tr')

for row in rows:
    # Извлекаем все ячейки текущей строки
    cells = row.find_elements(By.TAG_NAME,'td')
    for cell in cells:
        data_id = cell.get_attribute('data-id')
        # Извлекаем текст ячейки
        if data_id:
            print(f"{cell.text} - data-id: {data_id}")
        else:
            print(f"{cell.text}")
        # Извлекаем значение атрибута 'data-id', если он присутствует


        # Формируем строку вывода


# Закрываем драйвер
driver.quit()
