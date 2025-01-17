import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание линейного графика
plt.plot(x,y)

# Установка заголовка и подписей к осям
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Best Chart You Ever Seen.')
# Сохранение графика как изображения в формате PNG
plt.savefig("simple_plot.png")

# Отображение графика
plt.show()