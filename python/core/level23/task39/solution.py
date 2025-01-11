# Импортируем необходимые библиотеки для выполнения HTTP-запросов, парсинга HTML и работы с CSV
import requests
from bs4 import BeautifulSoup
import csv
import time

# URL страницы, с которой будем извлекать заголовок
url = 'https://google.com'

# Определяем максимальное количество попыток
retry = 3

# Пытаемся выполнить запрос к URL несколько раз при ошибках
try:
    res = requests.get(url,retry=retry)
    soup = BeautifulSoup(res.text, 'html.parser')
    tl = soup.find('title')
    with open('titles.csv',mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tl.text])
except:
    print('Error!')

# Если заголовок извлечен успешно, сохраняем его в CSV файл

