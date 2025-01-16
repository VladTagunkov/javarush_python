# Использованиее метода reduce()

# Напишите класс, который управляет своей сериализацией с помощью метода __reduce__(),
# чтобы при сериализации и десериализации сохранялись только определенные поля.

# Напишите тут ваш код
import pickle

class CustomSer:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    
    def __reduce__(self):
        cls = self.__class__
        args = (self.name,self.age)
        return (cls,args)
        
        
cl1 = CustomSer("Vasia",22)

sr1 = pickle.dumps(cl1)
de1 = pickle.loads(sr1)

print(cl1)
print(de1.name)
print(de1.age)
# try:
#     print(de1.adress)
# except:
#     print("No fields exist in deserialized object.")

