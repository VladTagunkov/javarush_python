from bs4 import BeautifulSoup

# Загрузка HTML-файла
with open('example.html','r') as file:
    html_file = file.read()

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_file,'html.parser')

# Извлечение всех div с классом section
tags = soup.select('div.section')

# Перебор всех найденных секций
for elem in tags:
    h2 = elem.find('h2')
    print(h2.text)
    elems_p = elem.find_all('p')
    for elm in elems_p:
        print(elm.text)
