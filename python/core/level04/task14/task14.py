# Случайный аргумент

# Напишите функцию  print_random(a,b,c), которая выводит на экран случайно выбранный переданный аргумент.

# Напишите тут ваш код

import random 

def print_random(a,b,c):
    l=[a,b,c]
    num = random.randint(0,2)
    return print(l[num])