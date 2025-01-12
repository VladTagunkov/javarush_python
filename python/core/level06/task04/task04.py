# Детектив

# Напиши функцию set_detector, которая проходится по списку(кортежу) своих аргументов и определяет - есть среди них множество или нет.
# Вызови функцию set_detector с разными вариантами параметров (с множеством и без).

# Напишите тут ваш код

def set_detector(*args):
    for elem in args:
        if type(elem) == set:
            return True
    return False
    
ex1 = ({1,2,3})
ex2 = (1,2,4)

set_detector(1,2,3)
set_detector({1,2,3},5)