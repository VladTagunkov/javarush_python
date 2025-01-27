# Настоящий массив.

# Создай массив с использованием библиотеки array.
# Добавь в него 10 случайных чисел от 0 до 1000. Отсортируй и выведи на экран.
# Класс list использовать нельзя.

# Напишите тут ваш код
import array
lst2 = array.array('i')
lst2.append(1)
lst2.append(9)
lst2.append(2)
lst2.append(3)
lst2.append(45)
lst2.append(235)
lst2.append(44)
lst2.append(87)
lst2.append(43)
lst2.append(33)

lst2 = sorted(lst2)
print(lst2)

