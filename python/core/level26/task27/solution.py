from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

def extract_titles(driver):
    # Здесь предполагается, что заголовки статей имеют тег h2
    elem_h2 = driver.find_elements(By.TAG_NAME,'h2')
    texts = []
    for elem in elem_h2:
        texts.append(elem.text)
    return texts


def main():
    # Создаем экземпляр драйвера браузера
    driver = webdriver.Chrome()

    try:
        # Открытие веб-страницы
        driver.get("http://example.com/articles")
                         # Задержка для загрузки страницы, рекомендуется добавить более надежное ожидание
        time.sleep(3)
        
        while True:
            # Извлечение заголовков
            headers = extract_titles(driver)
            
            try:
                # Переход на следующую страницу
                next_button = driver.find_element(By.LINK_TEXT,'Next')
                next_button.click()
                
                # Задержка, чтобы дать время загрузиться следующей странице
                time.sleep(3)
            except NoSuchElementException:
                # Если кнопка "Next" не найдена, значит, достигнута последняя страница
                print("Достигнута последняя страница.")
                break
    finally:
        # Закрытие драйвера
        driver.quit()

main()