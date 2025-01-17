import matplotlib.pyplot as plt
import numpy as np

# Создаем значения x от 0 до 5
x = np.linspace(0, 5, 100)

# Вычисляем значения y для трех функций
y1 = x
y2 = x**2
y3 = x**3

# Создаем график
plt.plot(x,y1, label = "y = x", color = 'red',linestyle='-')
plt.plot(x,y2, label = "y = x^2", color = 'green',linestyle='--')
plt.plot(x,y3, label = "y = x^3", color = 'blue',linestyle=':')

# Добавляем линии на график
plt.legend(loc='best')

# Настраиваем оси
plt.xlim(-1,6)
plt.ylim(-1,6)

# Добавляем аннотацию для точки пересечения (0, 0)
plt.annotate('Intersection',xy=(0,0),xytext=(0,0),
        arrowprops=dict(facecolor="black", shrink=0.05))

# Добавляем легенду


# Добавляем обозначения осей
plt.xlabel('Values')
plt.ylabel('Functions range')

# Отображаем график
plt.show()