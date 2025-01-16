# Отправка GET-запроса

# Напишите программу, которая отправляет GET-запрос с параметрами на URL и обрабатывает полученный JSON-ответ.

# Напишите тут ваш код
import requests 
params = {"one":1,
          "two":2
}

res = requests.get("http://google.com",params=params)
print(res.status_code)
try:
    print(res.json())
except:
    print("Reply does not have a json!")