# Pizza -> tomato, cheese, size

# def foo():
#     return 1
#
# class Car:
#     def __init__(self):
#         pass
#
#     def get_name():
#         pass
#
#     # pass
#     # # price = 100
#     # color = ''
#     # # weight = 1500
#     # # engine = 1.5
#
# bmw = Car()
# mers = Car()
#
# bmw.get_name()
# Car.get_name(bmw)
# Car.get_name(mers)


class Dog:
    def __init__(self, name="Unnamed dog", age=0, alive=True):
        self.age = age
        self.name = name
        self.alive = alive

    def description(self):
        return f"Hello my name is {self.name}, I am {self.age}"

    def speak(self, sound: str):
        if self.alive:
            return f"{sound} {sound}"
        else:
            return f"{self.name} is dead"


mikey = Dog(name="Mikey", age=10)
ron = Dog(name="Ron", age=4, alive=False)
billy = Dog()

print(mikey.description())
print(mikey.speak("Wof"))

print(ron.description())
print(ron.speak("Gav"))

print(billy.description())
print(billy.speak("Gav"))
