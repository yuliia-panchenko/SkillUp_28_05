# Задание 2
# Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа между ними.


def even_numbers(a, b):
    list_of_even_numbers = []
    for i in range(a + 1, b):
        if i % 2 == 0:
            list_of_even_numbers.append(i)
        i += 1
    print('Между введеными числами находятся такие четные:', list_of_even_numbers)


x, y = int(input('Введите начало диапазона: ')), int(input('Введите конец диапазона: '))
even_numbers(x, y)

# # Задание 3
# # Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа.
# # Функция принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# # ■ если она равна True, квадрат заполненный; ■ если False, квадрат пустой.


def square_of_symbols(square_length, symbol, condition_var):
    for z in range(square_length):
        if condition_var:
            # i = 1
            # while i <= square_length:
            print(symbol * square_length)
            # i += 1
        elif z == 0 or z == square_length - 1:
            print(symbol * square_length)
        else:
            print(symbol, ' ' * (square_length - 2), symbol, sep='')


user_length = int(input('Введите длину стороны квадрата: '))
user_symbol = input('Введите символ для заполнения квадрата: ')
user_condition = int(input('Введите 1 для заполнения квадрата и 0 для создания пустого квадрата: '))
square_of_symbols(user_length, user_symbol, user_condition)


# Задание 5
# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне.
# Границы диапазона передаются в качестве параметров. Если границы диапазона перепутаны
# (например, 5 — верхняя граница, 25 — нижняя граница), их нужно поменять местами.


def multiplication_in_range(first_num, last_num):
    if last_num < first_num:
        first_num, last_num = last_num, first_num
    result = 1
    for i in range(first_num, last_num + 1):
        result *= i
    print('Произведение чисел в указанном диапазоне:', result)


f, q = int(input('Введите начало диапазона: ')), int(input('Введите конец диапазона: '))
multiplication_in_range(f, q)


# Задание 6
# Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра.
# Из функции нужно вернуть полученное количество цифр. Например, если передали 3456, количество цифр будет 4.


def number_of_digits(number):
    print('Количество цифр в Вашем числе:', len(number))


input_number = input('Введите Ваше число: ')
number_of_digits(input_number)


# Задание 7
# Напишите функцию, которая проверяет является ли число палиндромом.
# Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции true,
# иначе false.


def is_palindrome(number):
    print(number == number[::-1])


user_value = input('Введите Ваше число, чтобы узнать, является ли оно палиндромом: ')
is_palindrome(user_value)
