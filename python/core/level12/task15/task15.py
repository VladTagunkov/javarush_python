# Сериализация помощью pickle

# Напишите программу, которая сериализует и десериализует объект Python с использованием модуля pickle.
# Объектом для сериализации будет словарь, содержащий информацию о студенте: имя, возраст и статус студента.

# Напишите тут ваш код
import pickle
# Объект для сериализации
student_info = {
    'name': 'John Doe',
    'age': 20,
    'status': 'student'
}

# Напишите тут ваш код
with open("stud.pkl",'wb') as file:
    pickle.dump(student_info,file)
    
with open("stud.pkl",'rb') as file:
    res = pickle.load(file)
    
    
print(res)