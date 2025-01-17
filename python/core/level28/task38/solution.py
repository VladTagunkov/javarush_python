import plotly.express as px
import plotly.io as pio
import kaleido


# Пример данных для графика (данные для Канады)
data = px.data.gapminder().query("country == 'Canada'")

# Создаем линейный график
fig = px.line(data,title='Canada Graph')

# Настройка параметров экспорта с использованием Kaleido


# Экспорт графика в PNG
pio.write_image(fig,file='canada.png', width=800, height=400, scale=1)

# Экспорт графика в PDF
pio.write_image(fig,file='canada.pdf', width=800, height=400, scale=1)