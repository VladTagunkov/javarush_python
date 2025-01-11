# Импортируем библиотеку для выполнения HTTP-запросов
import requests

# Запрашиваем у пользователя API-ключ OpenWeather и название города
api_key = input("Введите ваш API ключ OpenWeather: ")
city = input("Введите название города: ")

# Формируем URL для запроса данных о погоде
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Пытаемся выполнить запрос к API
try:
    response = requests.get(url)
    response.raise_for_status()  # Проверяем наличие ошибок HTTP
    data = response.json()  # Получаем данные в формате JSON

    # Проверяем наличие ошибок в ответе API
    if data['cod'] != 200:
        print(f"Ошибка: {data['message']}")
    else:
        # Извлекаем необходимые данные о погоде
        main = data['main']
        weather = data['weather'][0]

        # Конвертируем температуру из Кельвинов в Цельсии



        # Выводим данные о погоде
        print(f"Температура: {temperature_celsius:.2f}°C")
        print(f"Влажность: {humidity}%")
        print(f"Описание погоды: {description}")

# Обработка возможных ошибок запроса

