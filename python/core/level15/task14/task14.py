# Люблю список еще больше

# Напишите программу, которая создает динамический массив (список)
# и демонстрирует его основные операции: добавление, удаление, доступ по индексу и изменение элемента.
# Класс list использовать нельзя.

class DynamicArray:
    def __init__(self):
        self.array = []

    def add(self, element):
        return self.array.append(element)
    # Напишите тут ваш код

    def remove(self, index):
        if index < len(self.array):
            self.array.pop(index)
            return self.array
        else:
            return None
    # Напишите тут ваш код

    def get(self, index):
        if index < len(self.array):
            return self.array[index]
        else:
            return None
    # Напишите тут ваш код

    def set(self, index, element):
        if index < len(self.array):
            self.array[index] = element
            return self.array
        else:
            return None
    # Напишите тут ваш код

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)


# Примеры использования:
arr = DynamicArray()
arr.add(1)
arr.add(2)
arr.add(3)
print(arr)  # [1, 2, 3]

arr.remove(2)
print(arr)  # [1, 2]

print(arr.get(1))  # 2

arr.set(1, 5)
print(arr)  # [1, 5]

print(len(arr))  # 2