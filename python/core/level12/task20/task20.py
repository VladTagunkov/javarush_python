# Исключение несериализуемых полей

# Напишите класс, который содержит несериализуемые поля, такие как открытые файлы или базы данных,
# и реализуйте методы __getstate__() и __setstate__(),
# чтобы исключить эти поля при сериализации и восстановить их при десериализации.

# Напишите тут ваш код
import pickle
import mysql

class CustomClass:
    def __init__(self, first = None, second = None):
        self.first = first
        self.second = second
        #self.internal_state = "internal"
        #self.connection = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="db_test")
        self.internal_state = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="db_test")
        
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['internal_state'] # Исключаем внутреннее состояние
        #del self.connection
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        #self.connection = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="db_test")
        #self.internal_state = "restored internal"  # Восстанавливаем внутреннее состояние
        self.internal_state = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="db_test")
        
    def __repr__(self):
        return f"internal_state={self.internal_state})"
        
 
obj = CustomClass(77)
print(obj)

ser_obj = pickle.dumps(obj)
print(ser_obj)
#print(ser_obj.connection)

deser_obj = pickle.loads(ser_obj)
print(deser_obj)
#print(deser_obj.connection)