import unittest

# Функция которую тестируем
def string_length(s):
    """Возвращает длину переданной строки."""
    return len(s)


# Класс для тестирования методов работы со строками
class TestStringMethods(unittest.TestCase):
    # Тест для функции string_length
    def test_string_length(self):
        # Проверяем, что длина строки "Hello, World!" равна 13
        len_str = string_length("Hello, World!")
        self.assertEqual(len_str,13)

# Запуск тестов
unittest.main()
