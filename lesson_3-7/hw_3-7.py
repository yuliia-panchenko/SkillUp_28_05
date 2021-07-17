# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# название модели, год выпуска, производителя, объем двигателя, цвет машины, цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте
# доступ к отдельным полям через методы класса.

class Car:
    """Parameters of different cars"""

    def __init__(self, model, year, manufacturer, engine, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine = engine
        self.color = color
        self.price = price

    def car_info(self):
        return f'Car model is {self.model}, ' \
               f'manufactured by {self.manufacturer} in {self.year}, ' \
               f'volume of engine is {self.engine}, ' \
               f'color is {self.color}'

    def car_price(self, design_price=0):
        return f'Car price is {self.price + design_price}$'


mercedes = Car(
    model='Mercedes-Maybach S500', year=2015, manufacturer='Germany',
    engine=4.0, color='red', price=90000
)

porsche = Car(
    model='Porsche Cayenne E-Hybrid', year=2020, manufacturer='Germany',
    engine=3.0, color='green', price=145000
)

vaz = Car(
    model='VAZ 2109', year=1992, manufacturer='Russia',
    engine=1.5, color='black', price=1500
)

print(mercedes.car_info())
print(mercedes.car_price(1000))
print('========================')
print(porsche.car_info())
print(porsche.car_price())
print('========================')
print(vaz.car_info())
print(vaz.car_price())
print('========================')

# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в полях класса:
# название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.


class Book:
    """Information of different books"""

    def __init__(self, name, year, publisher, genre, author, cover, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.cover = cover  # переплет
        self.price = price

    def book_info(self):
        return f'Book: {self.name} is a {self.genre} ' \
               f'written by {self.author}, ' \
               f'published by {self.publisher} in {self.year} ' \
               f'(in {self.cover} cover)'

    def book_price(self):
        hard_cover_price = 80  # цена за твердый переплет
        if self.cover == 'soft':
            return f'Book price is {self.price} UAH'
        else:
            return f'Book price is {self.price + hard_cover_price} UAH'


book1 = Book(
    name='Harry Potter and the Prisoner of Azkaban', year=1999,
    publisher='Bloomsbury', genre='fantasy novel', author='J. K. Rowling',
    cover='hard', price=500
)
book2 = Book(
    name='The Kite Runner', year=2003,
    publisher='	Riverhead Books', genre='historical fiction', author='Khaled Hosseini',
    cover='soft', price=120
)

print(book1.book_info())
print(book1.book_price())
print('========================')
print(book2.book_info())
print(book2.book_price())
print('========================')

# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона,
# дату открытия, страну, город, вместимость. Реализуйте методы класса для ввода данных,
# вывода данных, реализуйте доступ к отдельным полям через методы класса.


class Stadium:
    """Information about stadiums"""

    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def stadium_info(self):
        return f'The name of stadium is {self.name} ' \
               f'was opened in {self.opening_date} in {self.city}, ' \
               f'{self.country}. The capacity of stadium is {self.capacity}.'


ukr_stadium = Stadium(
    name='The Olympic National Sports Complex', country='Ukraine',
    city='Kyiv', opening_date='12 September 1923', capacity=70050
)
eng_stadium = Stadium(
    name='Wembley Stadium', opening_date=2007, city='London',
    country='England', capacity=90000
)

print(ukr_stadium.stadium_info())
print('========================')
print(eng_stadium.stadium_info())
print('========================')
