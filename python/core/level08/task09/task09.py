# Декоратор.

# Напишите программу, которая создает простой декоратор для логирования вызовов функции.
# Программа должна:
# Определить декоратор log_decorator, который выводит сообщение перед и после вызова функции.
# Применить декоратор к функции greet(), которая выводит приветственное сообщение.
# Вызвать функцию greet().

# Напишите тут ваш код
def log_decorator(func):
    def internal():
        print("Before the function")
        func()
        print("After function")
        
    return internal        
    
@log_decorator
def greet():
    print("hello user!")
    
    
greet()