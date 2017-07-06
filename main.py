"""Text Fragmentator v1.0"""

class Book(object):
    """Книга"""
    def __init__(self, filename):
        """Создание книги из файла"""
        with open(filename, 'r') as f: # здесь не получилось указать кодировку
            self.blocks = [GridBlock(string) for string in f.readlines()]
        
    def read(self):
        # print (self.blocks, type(self.blocks))
        for i in self.blocks:
            print(i.length, i.data, '\n')

class GridBlock(object):
    """Блок структуры книги"""

    def __init__(self, text):
        """Создание блока"""
        self.id = None
        self.length = len(text)
        self.data = text.strip()


"""Тестирование"""
print('Cписок файлов для загрузки. Пользователь загружает файл:')

book1 = Book(input())
book1.read()
