# 1. Написать функцию-декоратор, которая подносит к квадрату значения,
# которое возвращает функция, к которой декоратор применяется.


def to_square(func):
    def inner(a):
        result = func(a)
        return result ** 2  # возвращаем квадрат значения, которое возвращает функция

    return inner


@to_square
def simple_func(a):
    return a


print(simple_func(10))
print(simple_func(6))
print(simple_func(3))
