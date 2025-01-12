# НДС

# Напишите функцию calculate_total_cost(price, tax=0.2), которая принимает цену товара и необязательный параметр налог (по умолчанию 20%).
# Функция должна вычислять и выводить общую стоимость товара с учетом налога.
# Затем напишите программу, которая вызывает эту функцию с различными параметрами.

# Напишите тут ваш код

def calculate_total_cost(price, tax=0.2):
    total_sum = price *(1+tax)
    print(total_sum)
    return total_sum
    

calculate_total_cost(55, tax=0.2)

calculate_total_cost(68)

calculate_total_cost(77, 0.24)