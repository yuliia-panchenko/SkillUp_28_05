# Создать множества: A, B, C c любыми элементами.
# Найти:
# 1. Разные элементы для A и B.
# 2. Одинаковые элементы для A и C.
# 3. Объединение 3-х множеств.

from random import randint

a = set(randint(1, 100) for i in range(1, 10))
b = set(randint(1, 100) for i in range(1, 30))
c = set(randint(1, 100) for i in range(1, 20))
print('a =', a)
print('b =', b)
print('c =', c)
print('=====================')
# Разные элементы для A и B.
unique_elements = a ^ b
print('Different elements for a and b:', unique_elements)
print('=====================')
# Одинаковые элементы для A и C
same_elements = a & c
print('The same elements for a, c', same_elements)
print('=====================')
# 3. Объединение 3-х множеств
union_set = a | b | c
print('Union of a, b, c:', union_set)
print('=====================')
