# Защищайтесь.

# Создайте класс Car, который будет иметь публичный атрибут brand и защищенный атрибут _model_.
# Добавьте методы для получения и установки значения защищенного атрибута _model.
# Создайте объект класса Car, установите значения атрибутов и выведите их на экран.

# Напишите тут ваш код
class Car:
    brand = "Opel"
    _model_ = "Astra" 
    
    def get_model(self):
        return self._model_
        
    def set_model(self,new_model):
        self._model_ = new_model
        
        
        
car = Car()
car.brand = "BMW" 
car.set_model('X6')

print(car.brand)
print(car.get_model())        