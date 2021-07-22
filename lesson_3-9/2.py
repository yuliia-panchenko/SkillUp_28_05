class Animal:
    def __init__(self, age=0, weight=0.0, name=""):
        self.sound = ""
        self.name = name
        self.age = age
        self.weight = weight

    @property
    def friendly(self):
        return True

    def __str__(self):
        return f"{self.name}. I am {self.age}"

    def say(self):
        print('=====================')
        print(f"{self.sound} {self.sound}")
        print('=====================')

class Dog(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = "GAV"

    # def say(self):
    #     super().say("GAV")

class Cat(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = "Miau"

    def shine_in_the_dark(self):
        print("I am a cat!!!")

    @property
    def friendly(self):
        return False

max = Dog(age=10, weight=12.2, name="Max")
kuzia = Cat(age=4, weight=4.2, name="Kuzia")
mark = Dog(age=5, weight=1.2, name="Mark")

print(max)
print(kuzia)
print(mark)

max.say()
kuzia.say()
mark.say()

# max.shine_in_the_dark() # Not working
kuzia.shine_in_the_dark()

print(max.friendly)
print(kuzia.friendly)

# print(isinstance(max, (Cat, Animal)))

print(Dog.__mro__)
# class Animal:
#     def __init__(self, age=0, weight=0.0, name=''):
#         self.sound = ''
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     def __str__(self):
#         return f'{self.name}. I am {self.age}'
#
#     def say(self, sound):
#         print(f'--{sound} {sound}--')
#
#
# class Dog(Animal):
#     # def __init__(self, **kwargs):
#     #     super().__init__()
#     def say(self):
#         super().say('GAV')
#
#
# class Cat(Animal):
#
#     def shine_in_the_dark(self):
#         print('I am a cat!!!')
#
#     def say(self):
#         super().say('Miau')
#
#
# max = Dog(age=10, weight=12.2, name='Max')
# kuzia = Cat(age=4, weight=4.2, name='Kuzia')
# mark = Dog(age=5, weight=1.2, name='Mark')
#
# print(max)
# print(kuzia)
# print(mark)
#
# max.say()
# kuzia.say()
# mark.say()
# print(isinstance(max, (Animal, Cat)))  # or
