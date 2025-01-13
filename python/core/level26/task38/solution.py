import unittest

def add_item(lst, item):
    """Добавляет элемент в список."""
    lst.append(item)

def remove_item(lst, item):
    """Удаляет элемент из списка."""
    lst.remove(item)

class TestListOperations(unittest.TestCase):
    def test_add_and_remove_item(self):
        # Создаем пустой список
        tmp_lst = []
        
        # Добавляем элемент
        add_item(tmp_lst,1)
        
        # Проверяем, что элемент был добавлен
        self.assertEqual(len(tmp_lst),1)
        
        # Удаляем элемент
        remove_item(tmp_lst,1)
        
        # Проверяем, что список снова пустой
        self.assertEqual(len(tmp_lst),0)

unittest.main()