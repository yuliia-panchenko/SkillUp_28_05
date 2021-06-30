def wrapper_function():
    def hello():
        print("Hello")

    hello()


# wrapper_function()


def decorator_function(func):
    def wrapper():
        print("Функция-обёртка")
        func()
        print("Выходим из функции")

    return wrapper


@decorator_function
def hello():
    print("Я функция hello")


@decorator_function
def bye():
    print("Я функция bye")


hello()
bye()

# a = decorator_function(hello)
# b = a()

# a = decorator_function(bye)
# b = a()