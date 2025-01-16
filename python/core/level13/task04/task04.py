# Использование декодера

# Напишите программу, которая десериализует JSON-строку в объект Python с использованием
# пользовательского декодера для преобразования строк ISO в объекты datetime.

# Напишите тут ваш код
import json 
import datetime 

def cust_dec(dat):
    if isinstance(dat,str):
        return datetime.datetime.fromisoformat(dat)
    return dat
            
j_str = '''{"dat":"2023-05-15T14:30:00"} '''

res = json.loads(j_str,object_hook=cust_dec)