from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера браузера

def parser(url_,id_):
    driver = webdriver.Chrome()
    
    # Загружаем веб-страницу
    driver.get(url_)
    
    # Находим элемент по его ID и получаем его текст
    elem = driver.find_element(By.ID,id_).text
    
    # Выводим текст элемента
    
    # Закрываем WebDriver
    driver.quit()
    
    return elem
