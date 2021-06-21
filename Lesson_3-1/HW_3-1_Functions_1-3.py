# Задание 1
# Напишите функцию, вычисляющую произведение элементов списка целых.
# Список передаётся в качестве параметра. Полученный результат возвращается из функции.
# Задание 2
# Напишите функцию для нахождения минимума в списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.
# Задание 3
# Напишите функцию, определяющую количество простых чисел в списке целых. Список передаётся в качестве
# параметра. Полученный результат возвращается из функции.


def multiplication(user_list):  # произведение элементов списка целых
    if 0 in user_list:
        print('Произведение всех чисел Вашего списка равно 0')
    else:
        result = 1
        for number in user_list:
            result *= number
        print('Произведение всех чисел Вашего списка: ', result)


def minimum(user_list):  # минимум в списке целых
    min_element = min(user_list)
    print('Минимальный элемент в Вашем списке: ', min_element)


def number_of_primes(user_list):  # количество простых чисел в списке целых
    count = len(user_list)
    for number in user_list:
        for j in range(2, int(number ** 0.5) + 1):
            if number % j == 0:
                count -= 1
    print('Количество простых чисел в списке: ', count)


input_list = input('Введите Ваши числа через пробел: ')
input_str_list = input_list.split()
input_int_list = []
for i in input_str_list:
    input_int_list.append(int(i))
multiplication(input_int_list)
minimum(input_int_list)
number_of_primes(input_int_list)