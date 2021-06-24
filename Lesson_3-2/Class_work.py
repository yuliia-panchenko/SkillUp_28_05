# a = 20
#
#
# def foo():
#     a = 10
#     print(a)
#
#
# def bar():
#     print(a)
#
#
# foo()
#
# bar()
#
# import math
#
# print(math.cos())


def outer_func():
    var = 100

    def inner_func():
        print(f'Printing var from inner_func(): {var}')

    inner_func()

    print(f'Printing var from outer_func(): {var}')


outer_func()

var = 100


def foo():
    global var
    print(var)

    var = 200


print(var)

from pprint import pprint

source_dict = {
    'key': 'value',
    'key2': 'value',
    'key3': 'value',
    'key4': 'value',
    'key5': 'value',
}

def pprint(anything):
    print('********')
    print(anything)
    print('********')

pprint(source_dict)

del pprint

pprint(source_dict)