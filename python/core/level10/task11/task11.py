# Запуск стандартного исключения

# Напишите функцию check_positive, которая принимает число и проверяет, является ли оно положительным.
# Если число отрицательное или равно нулю, функция должна запустить исключение ValueError с сообщением "Number must be positive".

# Напишите тут ваш код

def check_positive(n):
    if n> 0:
        print(f"Age is {n}")
        return n
    else:
        raise ValueError("Number must be positive")

check_positive(44)

