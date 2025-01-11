import requests
import json

# Отправляем HTTP-запрос на сайт
link="https://jsonplaceholder.typicode.com/todos/1"
res = requests.get(link)

# Извлекаем данные из JSON-ответа
print(res.status_code)

# Выводим данные в отформатированном виде
