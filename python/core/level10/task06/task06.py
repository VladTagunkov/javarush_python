# Преобразование данных.

# Напишите функцию convert_and_sum, которая принимает два аргумента в виде строк,
# преобразует их в целые числа и возвращает их сумму.
# Обработайте исключения, которые могут возникнуть при преобразовании строк в числа
# (например, если переданы некорректные значения).

# Напишите тут ваш код

def convert_and_sum(a,b):
    try:
        return int(a)+int(b)
    except TypeError:
        return "not correct value type"
    except ValueError:
        return "can't convert to int"    
    except:
        return 0