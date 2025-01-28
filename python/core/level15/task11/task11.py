# Создаем свой массив

# Создай массив с использованием библиотеки numpy.
# Добавь в него 10 случайных чисел от 0 до 1000. Отсортируй и выведи на экран.
# Класс list использовать нельзя.

# Напишите тут ваш код
import numpy as np
import random 

arr2 = np.array([])
for i in range(10):
    arr2 = np.append(arr2,random.randint(0,1000))

arr2.sort()
print(arr2)