# При старте приложения запускаются три потока.
# Первый поток заполняет список случайными числами.
# Два других потока ожидают заполнения. Когда список
# заполнен оба потока запускаются. Первый поток находит
# сумму элементов списка, второй поток средне арифметическое значение в списке.
# Полученный список, сумма и средне арифметическое выводятся на экран.

from threading import Thread
from random import randint
from time import sleep


def create_list():
    random_list = [randint(1, 100) for i in range(10)]
    print('Create random list function')
    print('Start sleeping')
    sleep(1)
    print(random_list)
    return random_list


def total(input_list):
    print('Sum of random list function')
    total_sum = sum(input_list)
    print('Start sleeping')
    sleep(2)
    print(f'Total sum is {total_sum}')


def average(input_list):
    average_number = sum(input_list) / len(input_list)
    print('Average number function')
    print('Start sleeping')
    sleep(3)
    print(f'Average number is {average_number}')


user_list = create_list()

# total(user_list)
# average(user_list)

t1 = Thread(target=create_list)
t1.start()
t1.join()
t2 = Thread(target=total, args=(user_list,))
t3 = Thread(target=average, args=(user_list,))
t2.start()
t3.start()
t2.join()
t3.join()
