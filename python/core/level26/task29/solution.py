from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Создаем экземпляр драйвера браузера
with webdriver.Chrome() as driver:
    # Открытие начальной страницы (замените URL на нужный)
    driver.get("URL_OF_THE_PAGE")

    while True:
        # Ожидание появления элементов с классом "title_class" и получение заголовков
        try:
            elem_title = WebDriverWait(driver,5).until(EC.presence_of_element_located(By.CLASS_NAME,'title_class'))
            elem_titles = driver.find_elements(By.CLASS_NAME,"title_class")
            # Вывод текста каждого найденного заголовка
            for elem in elem_titles:
                print(elem.text)

        except NoSuchElementException:
            # Если элементы не найдены, вывести сообщение
            print("Заголовки на этой странице не найдены.")

        # Поиск кнопки "Далее" для перехода на следующую страницу
        try:
            next_button = driver.find_element(By.LINK_TEXT,"Далее")
            

            # Нажатие на кнопку "Далее"
            next_button.click()

            # Опционально, ожидание загрузки следующей страницы
            time.sleep(2)

        except NoSuchElementException:
            # Если кнопка "Далее" не найдена, завершить выполнение
            print("Кнопка 'Далее' не найдена. Завершение.")
            break
