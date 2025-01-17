import plotly.express as px
import plotly.io as pio

# Используем встроенный датасет iris из Plotly Express
df = px.data.iris()

# Создаем интерактивный график - Scatter plot
fig = px.scatter(df, x="sepal_width", y='sepal_length',color='species')

# Экспортируем график в формате HTML с auto_open=True
pio.write_html(fig, file='graph.html', auto_open=True)