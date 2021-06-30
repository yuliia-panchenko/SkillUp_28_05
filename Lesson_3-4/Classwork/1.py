def decorator_function():
    def wrapper():
        print('Функция-обертка')
        print('Наша функция:')

        print('Наша функция')
    return wrapper


a = decorator_function()
print(a)
b = a()
print(b)


def hello():
    print('Я функция hello')


def bye():
    print('Я функция bye')

