import requests

# Задаем URL для проверки IP-адреса
url = 'http://httpbin.org/ip'

# Список прокси-серверов
proxies = [
    {'http': 'http://ip1:port', 'https': 'http://ip1:port'},
    {'http': 'http://ip2:port', 'https': 'http://ip2:port'},
    {'http': 'http://ip3:port', 'https': 'http://ip3:port'}
]

# Проходим по каждому прокси из списка
for proxy in proxies:
    try:
        # Печатаем используемый прокси-сервер
        print(f'We use proxy {proxy}')

        # Выполняем GET-запрос к URL с указанным прокси
        response = requests.get(url, proxies=proxy)
        print(response.status_code)

        # Проверяем статус ответа
        if response.status_code==200:
            print(proxy[0]['http'].split(':')[1].replace('/',''))

        # Если статус успешен, выводим IP-адрес, с которого был выполнен запрос


    # Обрабатываем возможные ошибки запроса
    except Exception as e:
        print(f"We have error - {e}")
