# Задание 4
# Напишите функцию, удаляющую из списка целых некоторое заданное число. Из функции нужно вернуть количество
# удаленных элементов.


def remove_element(user_list, element):
    count_element = user_list.count(element)  # считаем количество вхождений числа
    k = 0
    while k < count_element:
        user_list.remove(element)
        k += 1
    print('Количество удаленных элементов: ', k)


input_list = input('Введите Ваши числа через пробел: ')
delete_number = int(input('Введите число, которое нужно удалить: '))
input_str_list = input_list.split()
input_int_list = []
for i in input_str_list:
    input_int_list.append(int(i))
remove_element(input_int_list, delete_number)