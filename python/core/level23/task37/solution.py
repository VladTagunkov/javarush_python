import requests

# Определяем URL для проверки
url = "http://example.com/some-nonexistent-page"

# Пытаемся выполнить GET-запрос к указанному URL
res = requests.get(url)
    # Выполняем GET-запрос и проверяем статус ответа
if res.status_code == 200:
    print('Page exist everything is ok.')
elif res.status_code == 404:
    print('Page does not exist.')
elif res.status_code == 403:
    print('Page access denied.')
elif res.status_code == 500:
    print('Internal server error.')
else:
    print('Something went wrong.')
    # Если запрос прошел успешно, выводим информацию о доступности страницы


# Обработка исключений HTTP ошибок с подробным выводом по коду ошибки


# Обработка ошибок сетевого подключения


# Обработка таймаута запроса


# Общая обработка всех остальных ошибок
