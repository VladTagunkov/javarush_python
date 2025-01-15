import requests
import schedule
import time


# Функция для получения данных о погоде
def get_weather_data(api_key, city):
    # Формируем URL для API-запроса
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # Выполняем GET-запрос к API
    response = requests.get(url)
    # Преобразуем ответ в формат JSON
    data = response.json()
    return data


# Функция для вывода данных о погоде
def print_weather(data):
    # Проверяем, что данные о температуре и описании погоды существуют
    if data.get("main") and data.get("weather"):
        temperature = data["main"]["temp"]  # Температура
        weather_description = data["weather"][0]["description"]  # Описание погоды
        print(f"Текущая температура в Нью-Йорке: {temperature}°C")
        print(f"Описание погоды: {weather_description}")
    else:
        print("Не удалось получить данные о погоде")


# Функция, которая будет выполняться по расписанию
def scheduled_weather_check():
    api_key = "your_api_key"  # Замените 'your_api_key' на ваш реальный API-ключ OpenWeather
    city = "New York"  # Город для отслеживания погоды
    data = get_weather_data(api_key,city)
    print_weather(data)


# Настраиваем расписание для выполнения задачи каждые 15 минут
schedule.every(15).minutes.do(scheduled_weather_check)

# Основной цикл для выполнения задач по расписанию
while True:
    schedule.run_pending()
    time.sleep(1)
