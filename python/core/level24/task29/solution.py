# Импортируем библиотеку для выполнения HTTP-запросов
import requests

# URL для запроса шутки о программистах
url = "https://v2.jokeapi.dev/joke/Programming?type=single"

# Выполняем GET-запрос к API
response = requests.get(url)

# Проверяем, успешен ли запрос
if response.status_code == 200:
    # Извлекаем данные в формате JSON
    data = response.json()
    # Извлекаем текст шутки и выводим его на экран
    print(data['joke'])
else:
# Сообщение об ошибке, если запрос не удался
    print(response.status_code)
    print('We have error!')
