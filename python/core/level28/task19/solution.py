import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Произвольные данные для распределения времени
activities = ['Работа', 'Отдых', 'Спорт', 'Сон']
time_spent = [8, 2, 2, 12]  # Часы на каждую активность

def plot_pie_chart(start_angle):
    plt.clf()  # Очистка текущей фигуры
    plt.pie(time_spent, labels=activities, startangle=start_angle, autopct='%1.1f%%')
    plt.title('Распределение времени в течение дня')
    plt.draw()

def update(val):
    angle = slider.val
    plot_pie_chart(angle)

# Создание фигуры и осей
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)

# Первоначальная отрисовка круговой диаграммы
plot_pie_chart(0)

# Настройка ползунка для изменения начального угла
ax_angle = plt.axes([0.1, 0.1, 0.8, 0.05])
slider = Slider(ax_angle, 'Начальный угол', 0, 360, valinit=0)

slider.on_changed(update)

plt.show(block=True)