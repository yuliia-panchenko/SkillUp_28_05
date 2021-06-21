# Задание 6
# Напишите функцию, высчитывающую степень каждого элемента списка целых. Значение
# для степени передаётся в качестве параметра, список тоже передаётся в качестве параметра.
# Функция возвращает новый список, содержащий полученные результаты.


def power_of_elements(user_list, power):
    new_list = [element**power for element in user_list]
    print('Список из Ваших чисел в степени', power, ': ', new_list)


input_list = input('Введите Ваши числа через пробел: ')
power_for_elements = int(input('Введите степень, в которую нужно возвести: '))
input_str_list = input_list.split()
input_int_list = []
for i in input_str_list:
    input_int_list.append(int(i))
power_of_elements(input_int_list, power_for_elements)