# Использование энкодера

# Напишите программу, которая сериализует объект Python, содержащий дату и время, в JSON-строку
# с использованием пользовательского кодера для преобразования объектов datetime в строковый формат ISO.

# Напишите тут ваш код
import json
from datetime import datetime

class CustomCoder(json.JSONEncoder): 
    def default(self,obj):
        if isinstance(obj,datetime)
            return obj.isoformat()
        return super().default(obj)
        
        
dat = {"dat":datetime.now()}

res = json.dumps(dat,cls = CustomCoder)
print(res)