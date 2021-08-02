class Person:
    def __init__(self, name, surname):
        self.name = name
        self._surname = surname

    @property
    def info(self):
        return f'{self.name} {self._surname}'


class AdvPerson(Person):

    @property
    def new_info(self):
        return f'Surname is {self._surname}'


p1 = Person('Greg', 'Red')
p2 = AdvPerson('Kate', 'Hudson')
print(p1._surname)
print(p2.info)
print(p2.new_info)
