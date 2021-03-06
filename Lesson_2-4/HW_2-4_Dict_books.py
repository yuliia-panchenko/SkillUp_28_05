# Задание 4
# Создайте программу «Книжная коллекция». Нужно хранить информацию о книгах: автор,
# название книги, жанр, год выпуска, количество страниц, издательство. Требуется реализовать
# возможность добавления, удаления, поиска, замены данных. Используйте словарь для хранения информации.
from pprint import  pprint
books = {
    'Джоан Роулинг': {
        'название книги': 'Гарри Поттер и тайная комната', 'жанр': 'фентези', 'год выпуска': 1998,
        'количество страниц': 295, 'издательство': 'Bloomsbury Publishing'
    },
    'Антуан де Сент-Экзюпери': {
        'название книги': 'Маленький принц', 'жанр': 'философская сказка', 'год выпуска': 1943,
        'количество страниц': 96, 'издательство': 'Новый свет'
    },
    'Халед Хоссейни': {
        'название книги': 'Бегущий за ветром', 'жанр': 'роман', 'год выпуска': 2003,
        'количество страниц': 416, 'издательство': 'Riverhead Books'
    }
}
pprint(books)
print('=====================')

# добавим элемент
books['Ли Харпер'] = {
        'название книги': 'Убить пересмешника', 'жанр': 'роман', 'год выпуска': 1960,
        'количество страниц': 380, 'издательство': 'J. B. Lippincott & Co.'
    }
print('Добавим нового автора')
pprint(books)
print('=====================')

# удалим элемент
del books['Антуан де Сент-Экзюпери']
print('Удалим автора Антуан де Сент-Экзюпери')
pprint(books)
print('=====================')

# поиск элемента
print('Есть ли автор Ли Харпер?')
print('Ли Харпер' in books)  # True
print('Книга Халеда Хоссейни')
print(books.get('Халед Хоссейни'))
print('=====================')

# замена данных
print('Заменим издательство Джоан Роулинг')
books['Джоан Роулинг']['издательство'] = 'Scholastic Corporation'
pprint(books)
print('====================')


