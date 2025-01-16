import matplotlib.pyplot as plt

# Создание массива значений для оси X (от 1 до 47)
x_values = list(range(1,47))

# Создание массива значений для оси Y (массива из 47 нулей)
y_values = [0] * 47

# Построение графика
plt.plot(x_values, y_values)

# Название графика
plt.title('Женщины-президенты США')

# Подписи осей
plt.xlabel('Номер президента')
plt.ylabel('Количество женщин-президентов')

# Отображение графика
plt.show()