from bs4 import BeautifulSoup

# Загрузка HTML-файла
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup для парсинга HTML-документа
soup = BeautifulSoup(html_content, 'html.parser')

# Извлекаем все элементы <li> из документа
tags_li = soup.select('li')


# Выводим текст всех найденных элементов <li>
for elem in tags_li:
    print(elem.text)