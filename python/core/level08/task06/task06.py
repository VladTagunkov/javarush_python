# Замыкание.

# Напишите программу, которая создает функцию фильтра с использованием замыканий.
# Программа должна:
# Определить внешнюю функцию make_filter(threshold), которая создает и возвращает внутреннюю функцию filter_func(value).
# Внутренняя функция filter_func(value) должна возвращать True, если value больше threshold.
# Создать несколько функций фильтров с различными пороговыми значениями и
# использовать их для фильтрации списка данных, выводя результат на экран.

# Напишите тут ваш код

def make_filter(threshold):
    def filter_func(value):
        if value>threshold:
            return True
    return filter_func
    
f1 = make_filter(5)
f2 = make_filter(10) 

print(f1(3))
print(f1(20))
print(f2(14))

f3 = make_filter(7)
l1 = [1,2,3,8,9,10] 
print(list(filter(f3,l1)))