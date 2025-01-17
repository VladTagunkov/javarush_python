import matplotlib.pyplot as plt
import numpy as np

# Данные для графика
x = np.arange(0, 6, 1)
y1 = np.square(x)
y2 = np.power(x, 3)

# Создание графика


# Первая линия для квадрата значений
plt.plot(x,y1,label = 'Square number')

# Вторая линия для куба значений
plt.plot(x,y2,label = 'Cube number')

# Добавление легенды
plt.legend()

# Настройка цвета осей
plt.xlabel('Numbers',color='magenta')
plr.ylabel('Power numbers value',color='red')

# Добавление сетки
plt.grid(True,color='pink')

# Настройка меток на оси X
plt.xticks(np.arange(0, 6, 1))

# Названия осей


# Показать график
plt.show()