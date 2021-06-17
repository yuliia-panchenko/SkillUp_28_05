my_list = list(range(1, 11))
print(my_list)
to_find = 5
found_index = 0

for index, number in enumerate(my_list):
    if number == to_find:
        print('Я нашел этот элемент:', number, 'Индекс:', index)
        found_index = index
        break
    else:
        print(number)

print('Элемент:', my_list[found_index])
