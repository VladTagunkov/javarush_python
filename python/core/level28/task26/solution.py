import matplotlib.pyplot as plt

# Данные для графика
y_values = [1, 4, 9, 16, 25]

# Создание линейного графика
plt.plot(y_values)

# Удаляем дополнительные поля вокруг графика


# Сохранение графика с заданными параметрами
plt.savefig("high_resolution_plot.png",dpi='150', bbox_inches='tight')
plt.show()