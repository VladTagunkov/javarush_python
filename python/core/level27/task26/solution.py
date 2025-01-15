import requests
import schedule
from datetime import datetime
import time

# URL для получения данных о курсе валют
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"


# Функция для получения курсов обмена валют
def get_exchange_rates():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Вызывает ошибку при плохом ответе
        data = response.json()
        # Возвращаем только курсы для EUR и GBP
        return {
            "EUR": data['rates'].get("EUR"),
            "GBP": data['rates'].get("GBP")
        }
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных: {e}")
        return None


# Функция для отображения курсов обмена валют
def display_rates():
    rates = get_exchange_rates()
    if rates:
        # Получаем текущее время
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Время: {now}")
        print(f"Курс USD к EUR: {rates['EUR']}")
        print(f"Курс USD к GBP: {rates['GBP']}")
    else:
        print("Не удалось получить курсы обмена валют.")


# Настройка расписания для выполнения задачи каждый час
schedule.every(1).hour.do(display_rates)

# Основной цикл для выполнения задач по расписанию
while True:
    schedule.run_pending()
    time.sleep(1)
