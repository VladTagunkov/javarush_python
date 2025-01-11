from bs4 import BeautifulSoup

# Загрузка HTML-файла
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Находим все строки таблицы
tag_ro = soup.select('tr')
#print(tag_ro)

# Итерируем по строкам и ячейкам, извлекая текст
for elem in tag_ro:
    tag_td = elem.select('td')
    for el in tag_td:
        print(el.get_text(strip=True))
        # Используем .get_text() с параметром strip=True для извлечения только текста, игнорируя вложенные теги
