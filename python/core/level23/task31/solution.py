from bs4 import BeautifulSoup
import pandas as pd
import csv

# Путь к HTML-файлу, который будем анализировать
file_path = "example.html"  # Укажите путь к вашему HTML-файлу

# Открываем HTML-файл и читаем его содержимое
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Парсинг HTML-контента
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение заголовков
tab = soup.find('table')
head = tab.find_all('th')
rows = tab.findAll('tr')
heads = []
rows_ = []
for elem in head:
    heads.append(elem.text)

for row in rows:
    cells = row.findAll('td')
    cell_list = []
    for cell in cells:
        cell_list.append(cell.text)
    rows_.append(cell_list)

# Извлечение данных строк
#print(heads)
res_rows = [heads] + rows_[1:]
df = pd.DataFrame(rows_[1:], columns=heads)
df.to_csv("solution.csv", index=False)

