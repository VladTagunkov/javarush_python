# Четкий но случайный

# Напишите программу, которая создает множество из 10 случайных чисел в диапазоне от 1 до 100.
# Программа должна получить подмножество всех четных чисел из этого множества и вывести его.

# Напишите тут ваш код
from random import randrange 

ls_ = set([randrange(1,100) for i in range(10)])
lsch = set([i for i in ls_ if i%2==0])

print(lsch)