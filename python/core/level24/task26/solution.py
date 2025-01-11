# Импортируем необходимые библиотеки для выполнения HTTP-запросов и парсинга HTML
import requests
from bs4 import BeautifulSoup

# URL-адрес страницы с продуктами и номер страницы для начала
base_url = "http://example.com/products"
page_number = 1

# Начинаем перебор страниц
while True:
    # Формируем URL для текущей страницы
    cur_url = f"{base_url}?page={page_number}"

    # Выполняем GET-запрос к странице
    res = requests.get(cur_url)

    # Создаем объект BeautifulSoup для парсинга HTML-контента
    soup = BeautifulSoup(res, 'html.parser')

    # Извлекаем данные о продуктах с класса 'product'
    tags = soup.select('.product')

    for elem in tags:
        print(elem.text)

# Извлекаем название и цену продукта

# Проверяем, есть ли ссылка "Далее" для перехода на следующую страницу


# Если ссылки "Далее" нет, завершаем перебор страниц

# Переходим к следующей странице
