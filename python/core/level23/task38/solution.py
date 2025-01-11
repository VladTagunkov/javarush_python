import logging
import time
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

# Настраиваем логирование, указываем файл для записи ошибок и формат сообщений
logging.basicConfig(filename='scraper.log',level=logging.INFO)
# Указываем URL, который будем сканировать
url = 'https://google.com'
# Пытаемся выполнить GET-запрос к указанному URL с тайм-аутом 5 секунд
try:
    res = requests.get(url,timeout=5)
    print(res.text)
except requests.exceptions.HTTPError as err:
    logging.error('HTTP Error!',err)
except requests.exceptions.ConnectionError as err:
    logging.error('Connection error',err)
except requests.exceptions.Timeout as err:
    logging.warning('Timeout error',err)
    time.sleep(5)
except requests.exceptions.RequestException as err:
    logging.error('Request error',err)
# Обработка исключений при возникновении HTTP ошибки

# Обработка исключений при возникновении ошибки соединения

# Обработка исключений при превышении времени ожидания

# Общая обработка всех остальных ошибок
