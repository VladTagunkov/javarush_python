import requests
import pandas as pd

# URL для получения данных о криптовалютах из CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 100,
    'page': 1,
    'sparkline': 'false'
}
tmp_list = []
# Выполнение запроса к API
res = requests.get(url,params = params)
data = res.json()
print(data)
for elem in data:
    tmp_list.append({'name':elem['name'],
                     'current_price':elem['current_price'],
                     'market_cap':elem['market_cap']})
df = pd.DataFrame(tmp_list)
print(df.sort_values(by='current_price',ascending=False).head())

# Сортировка криптовалют по текущей цене в порядке убывания


# Вывод информации о пяти самых дорогих криптовалютах
