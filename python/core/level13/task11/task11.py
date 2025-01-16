# Использование прокси-сервера с модулем requests

# Напишите программу, которая отправляет GET-запрос через прокси-сервер с использованием библиотеки requests.

# Напишите тут ваш код
import requests
import json 

url = 'http://httpbin.org/ip'
proxies = {'http':'http://10.11.12.13',
           'https':'http://10.11.12.14'
}

try:
    res = requests.get(url,proxies=proxies)
    print(res.json())
except Exception as e:
    print(f"We have error {e}")

