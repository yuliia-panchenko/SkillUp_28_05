# Задание 5
# Напишите функцию, которая получает два списка в качестве параметра и возвращает список,
# содержащий элементы обоих списков.


def list_of_two_lists(user_list_1, user_list_2):
    print('Список, содержащий элементы обоих списков: ', user_list_1 + user_list_2)


input_list1 = input('Введите первый список: ')
input_list2 = input('Введите второй список: ')
input_str_list1 = input_list1.split()
input_str_list2 = input_list2.split()
input_int_list1 = []
input_int_list2 = []
for i in input_str_list1:
    input_int_list1.append(int(i))
for i in input_str_list2:
    input_int_list2.append(int(i))
list_of_two_lists(input_int_list1, input_int_list2)