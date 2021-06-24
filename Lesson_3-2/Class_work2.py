# def square(a):
#     return a**2
#
#
# def cube(a):
#     return a**3


def power_factory(exp):
    def power(base):
        return base**exp
    return power


square = power_factory(2)
cube = power_factory(3)

# s = square(5)
# c = cube(5)
# print(s)
# print(c)
