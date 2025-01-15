# Перегрузка операторов индексации

# Напишите класс Matrix, который будет представлять двумерную матрицу и поддерживать перегрузку операторов индексации ([]).
# Реализуйте методы __getitem__ и __setitem__.

class Matrix:
    def __init__(self,key):
        self.h = key[0]
        self.w = key[1]
        self.data = [[0 for _ in range(key[1])] for _ in range(key[0])].
        
    def __getitem__(self,key):
        if key[0] >= self.h or key[1] >= self.w:
            raise IndexError
        return self.data[key[0]][key[1]]
    
    def __setitem__(self, key, val):
        if key[0] >= self.h or key[1] >= self.w:
            raise IndexError
        self.data[key[0]][key[1]] = val
        
        

# Напишите тут ваш код



# Пример использования
matrix = Matrix(3, 3)
matrix[0, 0] = 1
print(matrix[0, 0])  # Вывод: 1