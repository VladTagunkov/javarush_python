# Обработка ответов сервера с модулем requests

# Напишите программу, которая отправляет GET-запрос на сервер и обрабатывает ответ, включая статус-код, заголовки и тело ответа.

# Напишите тут ваш код
import requests



try:
    res = requests.get("http://google.com")
    print(res.headers)
    requests.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"Other error occurred: {err}")
except:
    print("something wring!")

