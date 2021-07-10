# Задание 1
# Дано два текстовых файла. Выяснить, совпадают ли их строки.
# Если нет, то вывести несовпадающую строку из каждого файла.


print('============Task_1============\n')
file1 = open('file1.txt')
file2 = open('file2.txt')
for line1, line2 in zip(file1, file2):
    if line1 != line2:
        print('Line from first file:', line1, end='')  # несовпадающая строка из первого файла
        print('Line from second file:', line2, end='')  # несовпадающая строка из второго файла
file1.close()
file2.close()

# Задание 2
# Дан текстовый файл. Необходимо создать новый файл и записать в него следующую статистику по исходному файлу:
# ■ Количество символов;
#  ■ Количество строк;
#  ■ Количество гласных букв;
#  ■ Количество согласных букв; ■ Количество цифр.
# Задание 4
# Дан текстовый файл. Найти длину самой длинной строки.

file3 = open('source.txt')
list_all_lines = file3.readlines()  # все строки из файла помещаем в список
file3.close()
string_all_lines = ''.join(list_all_lines)  # преобразуем список всех строк в одну строку


def counter_chars(string, base):
    counter = 0
    for item in string.lower():
        if item in base:
            counter += 1
    return counter


counter_vowels = counter_chars(string_all_lines, 'aeuio')
counter_consonants = counter_chars(string_all_lines, 'bcdfghjklmnpqrstvwxyz')
counter_numbers = counter_chars(string_all_lines, '0123456789')

file3_statistics = open('statistics.txt', 'w')
file3_statistics.write(f'''Number of symbols: {len(string_all_lines)}
Number of lines: {len(list_all_lines)}
Number of vowels: {counter_vowels}
Number of consonants: {counter_consonants}
Number of numbers: {counter_numbers}
Length of the longest line: {len(max(list_all_lines))}''')

# Задание 3
# Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой файл.
file4 = open('file5.txt')
text = file4.readlines()
file5 = open('result_of_delete.txt', 'w')
file5.writelines(text[:-1])
file4.close()
file5.close()

# Задание 5
# Дан текстовый файл. Посчитать сколько раз в нем встречается заданное пользователем слово.

print('\n============Task_5============\n')
file6 = open('file6.txt')
user_word = input('Enter your word: ')
list_file6 = [line.strip() for line in file6]  # удалим \n в конце строки
count_user_word = list_file6.count(user_word)
print('Number of user word in file:', count_user_word)  # количество вхождений пользовательского слова
file6.close()

# Задание 6
# Дан текстовый файл. Найти и заменить в нем заданное слово.
# Что искать и на что заменять определяется пользователем.

file7 = open('file7.txt', 'r+')
str_of_file7 = file7.read()
str_of_file7 = str_of_file7.replace('tree', 'banana')
file7.seek(0)  # перемещаемся в начало файла
file7.write(str_of_file7)
file7.close()
