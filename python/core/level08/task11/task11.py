# Множество декораторов.

# Напишите программу, которая использует несколько декораторов для одной функции.
# Программа должна:
# Определить два декоратора decorator1 и decorator2, которые логируют свои вызовы.
# Применить оба декоратора к функции say_hello.
# Вызвать функцию say_hello.

# Напишите тут ваш код

def decorator1(func):
    def wrap1():
        print('Start Dec 1')
        func()
    return wrap1

def decorator2(func):
    def wrap2():
        print('Start Dec 2')
        func()
    return wrap2
    
@decorator1
@decorator2
def say_hello():
    print("Hello Vlad!")
    

say_hello()