# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# название модели, год выпуска, производителя, объем двигателя, цвет машины, цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте
# доступ к отдельным полям через методы класса.

class Car:
    """Parameters of different cars"""

    def __init__(self, model, year, manufacturer, engine, colour, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine = engine
        self.colour = colour
        self.price = price

    def get_car_model(self):
        return f'Car model is {self.model}'

    def get_car_year(self):
        return f'{self.model} was manufactured in {self.year}'

    def get_car_manufacturer(self):
        return f'{self.model} was manufactured in {self.manufacturer}'

    def get_car_engine(self):
        return f'The volume of {self.model} engine is {self.engine}'

    def get_car_colour(self):
        return f'The colour of {self.model} is {self.colour}'

    def get_car_price(self):
        return f'Car price is {self.price}$'

    def set_car_price(self, modification_price=0):
        return f'Car price with modification is {self.price + modification_price}$'


mercedes = Car(
    model='Mercedes-Maybach S500', year=2015, manufacturer='Germany',
    engine=4.0, colour='red', price=90000
)

print(mercedes.get_car_model())
print(mercedes.get_car_year())
print(mercedes.get_car_manufacturer())
print(mercedes.get_car_engine())
print(mercedes.get_car_colour())
print(mercedes.get_car_price())
print(mercedes.set_car_price(10000))
print('========================')

# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в полях класса:
# название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.


class Book:
    """Information of different books"""

    def __init__(self, name, year, publisher, genre, author, price, cover='soft'):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.cover = cover  # переплет
        self.price = price

    def get_book_info(self):
        return f'Book: {self.name} is a {self.genre} ' \
               f'written by {self.author}, ' \
               f'published by {self.publisher} in {self.year} '

    def get_book_price(self):
        hard_cover_price = 80  # цена за твердый переплет
        if self.cover == 'soft':
            return f'The price of the book in {self.cover} cover is {self.price} UAH'
        else:
            return f'The price of the book in {self.cover} cover is ' \
                   f'{self.price + hard_cover_price} UAH'


book1 = Book(
    name='Harry Potter and the Prisoner of Azkaban', year=1999,
    publisher='Bloomsbury', genre='fantasy novel', author='J. K. Rowling',
    cover='hard', price=500
)
book2 = Book(
    name='The Kite Runner', year=2003, publisher='Riverhead Books',
    genre='historical fiction', author='Khaled Hosseini',
    price=120
)

print(book1.get_book_info())
print(book1.get_book_price())
print('========================')
print(book2.get_book_info())
print(book2.get_book_price())
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

    def get_stadium_name(self):
        return f'The name of a stadium is {self.name}'

    def get_stadium_opening_date(self):
        return f'The stadium {self.name} was opened in {self.opening_date}'

    def get_stadium_location(self):
        return f'The stadium {self.name} is situated in {self.city}, {self.country}'

    def get_stadium_capacity(self):
        return f'The capacity of the stadium {self.name} is {self.capacity}'


ukr_stadium = Stadium(
    name='The Olympic National Sports Complex', country='Ukraine',
    city='Kyiv', opening_date='12 September 1923', capacity=70050
)

print(ukr_stadium.get_stadium_name())
print(ukr_stadium.get_stadium_opening_date())
print(ukr_stadium.get_stadium_location())
print(ukr_stadium.get_stadium_capacity())
