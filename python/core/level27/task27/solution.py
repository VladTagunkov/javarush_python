import requests
from bs4 import BeautifulSoup
import schedule
import time

def fetch_headlines():
    # URL сайта BBC
    url = "https://www.bbc.com/news"

    # Запросим HTML-код страницы
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = soup.find_all('h3')  # Поиск всех тегов <h3> (где обычно находятся заголовки)
        print("Последние заголовки новостей на BBC:")
        for headline in headlines[:10]:  # Берем первые 10 заголовков
            print("-", headline.get_text(strip=True))
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных: {e}")


# Запланировать задание на каждый день в 8:00
schedule.every().day.at("08:00").do(fetch_headlines)

# Постоянное выполнение программы
while True:
    schedule.run_pending()
    time.sleep(1)