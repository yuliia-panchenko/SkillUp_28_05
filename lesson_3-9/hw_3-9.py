# Задание 1
# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте класс CoffeeMachine
# (содержит информацию о кофемашине), класс Blender (содержит информацию о блендере),
# класс MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые для работы методы.

class Device:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.year_of_release = kwargs.get('year_of_release', None)
        self.manufacturer = kwargs.get('manufacturer', None)
        self.colour = kwargs.get('colour', None)
        self.power = kwargs.get('power', None)
        self.action = 'do'

    def __str__(self):
        return f'The device is {self.name}, manufactured in {self.manufacturer} ' \
               f'in {self.year_of_release}. Its colour is {self.colour}, ' \
               f'power is {self.power}W'

    def work(self):
        print(f'It can {self.action}')


class CoffeeMachine(Device):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.action = 'make coffee'


class Blender(Device):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.action = 'grind, chop and mix different ingredients'


class MeatGrinder(Device):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.action = 'grind meat'


delonghi = CoffeeMachine(
    name='Delonghi PrimaDonna S Evo', year_of_release=2019, manufacturer='Italy',
    colour='gray', power=1450
)

print(delonghi)
delonghi.work()
print('=' * 25)

bosch = Blender(
    name='Bosch MS8CM6190', year_of_release=2017, manufacturer='Germany',
    power=1000
)

print(bosch)
bosch.work()
print('=' * 25)

tefal = MeatGrinder(
    name='Tefal NE109838', year_of_release=2018, manufacturer='France',
    colour='white', power=1400
)

print(tefal)
tefal.work()
print('=' * 25)

# Задание 2
# Создайте класс Ship, который содержит информацию о корабле.
# С помощью механизма наследования, реализуйте класс Frigate (содержит информацию о фрегате),
# класс Destroyer (содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые для работы методы.


class Ship:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.country = kwargs.get('country', None)
        self.crew = kwargs.get('crew', 0)
        self.purpose = ''

    def __str__(self):
        return f'{self.name} was produced in {self.country}. ' \
               f'Its crew is {self.crew} people'

    def usage(self):
        return f'It is used {self.purpose}'


class Frigate(Ship):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description = 'to protect other warships and merchant-marine ships'


class Destroyer(Ship):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.purpose = 'to defend ships against powerful short range attackers'


class Cruiser(Ship):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.purpose = 'for air defense and shore bombardment'


frigate1 = Frigate(
    name='Type 26 frigates', country='Great Britain', crew=118
)

destroyer1 = Destroyer(
    name='USS Winston S. Churchill', country='The USA', crew=380
)

cruiser1 = Cruiser(
    name='Aurora', country='Russia', crew=570
)

print(frigate1)
print(frigate1.usage())
print('=' * 25)
print(destroyer1)
print(destroyer1.usage())
print('=' * 25)
print(cruiser1)
print(cruiser1.usage())
print('=' * 25)

# Задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.)
# и поле для хранения копеек (центы, евроценты, копейки и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.


class Money:

    def __init__(self, banknote=0, coin=0):
        self.banknote = banknote
        self.coin = coin
        self.currency = 'currency'

    def total(self):
        total_amount = self.banknote + self.coin / 100
        return f'Total amount of money is {total_amount}{self.currency}'


class Dollar(Money):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currency = '$'


class Euro(Money):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currency = '€'


class Hryvnia(Money):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currency = '₴'


dol = Dollar(banknote=1525, coin=45)
print(dol.total())
print('=' * 25)
eur = Euro(banknote=7890, coin=123)
print(eur.total())
print('=' * 25)
uah = Hryvnia(banknote=5432, coin=70)
print(uah.total())
print('=' * 25)
