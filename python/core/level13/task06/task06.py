# Отправка POST-запроса

# Напишите программу, которая отправляет POST-запрос с JSON-данными на URL и обрабатывает полученный JSON-ответ.

# Напишите тут ваш код

import requests 
params = {"one":1,
          "two":2
}

res = requests.post("http://google.com",json=params)
print(res.status_code)
try:
    print(res.json())
except:
    print("Reply does not have a json!")