# Задание 1
# Есть три кортежа целых чисел, необходимо найти элементы, которые есть во всех кортежах.
# Задание 2
# Есть три кортежа целых чисел необходимо найти элементы, которые уникальны для каждого списка.
# Задание 3
# Есть три кортежа целых чисел необходимо найти элементы, которые есть в каждом из кортежей и
# находятся в каждом из кортежей на той же позиции.

from random import randint

t1 = tuple(randint(1, 10) for i in range(1, 10))
t2 = tuple(randint(1, 10) for i in range(1, 10))
t3 = tuple(randint(1, 10) for i in range(1, 10))
print('t1 =', t1)
print('t2 =', t2)
print('t3 =', t3)
print('=====================')
print('Elements that are in all tuples:', tuple(set(t1) & set(t2) & set(t3))) # Задание 1
print('=====================')
print(
    'Elements that are unique:',
    tuple(set(t1) - set(t2) - set(t3) | set(t2) - set(t1) - set(t3) | set(t3) - set(t2) - set(t1))) # Задание 2
print('=====================')
z = 0
for z in range(len(t1)):             # Задание 3
    if t1[z] == t2[z] == t3[z]:
        print(t1[z], 'index -', z)
    z += 1
print('=====================')