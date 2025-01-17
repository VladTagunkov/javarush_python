import plotly.express as px
import plotly.io as pio

# Данные для графика
df = px.data.iris()
fig = px.scatter(df,x="sepal_width", y='sepal_length', color='species')

# Создаем интерактивный график


# Сохраняем график в формате HTML
pio.write_html(fig, file='scatter_plot.html', auto_open=True)