# Обработка исключений.

# Напишите функцию safe_division, которая принимает два числа и выполняет их деление.
# Обработайте исключения, которые могут возникнуть при делении на ноль
# и при передаче некорректных значений (например, строки вместо чисел).
# Функция должна возвращать сообщение об ошибке или результат деления.

# Напишите тут ваш код

def safe_division(a,b):
    try:
        return a/b 
    except ZeroDivisionError:
        return "Zero Division"
    except TypeError:
        return "Type Error"
    except:
        return "Other Error"
        