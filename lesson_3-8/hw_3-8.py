# Разработайте класс с полной инкапсуляцией, доступ к атрибутам которого и изменение
# данных реализуются через вызовы методов. Помним, что принято имена методов для извлечения
# данных начинать со слова get (взять), а имена методов, в которых свойствам присваиваются
# значения, – со слова set (установить). Например, get_field, set_field.

class Student:

    def __init__(self, **kwargs):
        self.__name = kwargs.get('name', None)
        self.__surname = kwargs.get('surname', None)
        self.__year_of_studying = kwargs.get('year_of_studying', None)
        self.__speciality = kwargs.get('speciality', None)

    def __str__(self):
        return f'Full name of student: {self.__name} {self.__surname}\n' \
               f'The year of studying: {self.__year_of_studying}\n' \
               f'Speciality is {self.__speciality}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value.capitalize()

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value.capitalize()

    @property
    def year_of_studying(self):
        return self.__year_of_studying

    @year_of_studying.setter
    def year_of_studying(self, value):
        if type(value) != int:
            print('Enter an integer number, please')
        else:
            self.__year_of_studying = value

    @property
    def speciality(self):
        return self.__speciality

    @speciality.setter
    def speciality(self, value):
        self.__speciality = value


student1 = Student(name='John', surname='Wick', year_of_studying=2, speciality='Applied mechanics')
print(student1)
print('================')
student1.surname = 'Snow'
print(student1)
print('================')
student2 = Student(name='Sarah', surname='Parker', year_of_studying=4, speciality='Energy machinery')
student2.speciality = 'Materials Science'
print(student2)
