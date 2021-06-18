numbers = []
for i in range(10):
    numbers.append(i)
print(numbers) 

numbers = [i for i in range(10)]
print(numbers)

from pprint import pprint
# students = {
#     'математика': {
#         'Вася Пупкин': 5,
#         'Коля Сергеев': 3,
#         'Сергей Сидоров': 4,
#         'Маша Гегель': 4,
#         'Сергей Помидоров': 2,
#         'Александр Чесноков': 4,
#         },
#     'физо': {
#         'Вася Пупкин': 5,
#         'Коля Сергеев': 3,
#         'Сергей Сидоров': 4,
#         'Маша Гегель': 4,
#         'Сергей Помидоров': 2,
#         'Александр Чесноков': 4,
#         },    
# }
# students = {
#     'Вася Пупкин'

# }
marks = {
    'Математика': 0,
    'Физо': 1
}

students = {
    'Вася Пупкин': [2, 4],
    'Коля Сергеев': [3, 3],
    'Сергей Сидоров': [4, 1],
    'Маша Гегель': [4, 4],
    'Сергей Помидоров': [2, 4],
    'Александр Чесноков': [4, 3]   
}

pprint(students)
pprint(students['Сергей Сидоров'][marks['Физо']])
print(len(students))
del students['Александр Чесноков']
pprint(students)
print(students.get('Маша Гегельvmkh'))
print(students.items())
pprint(students.keys())
pprint(students.values())

#student = students.pop('Маша Гегель')
student = students.popitem()
print(student)
pprint(students)

new_students = {
    'Jhon Doe': [5, 5, 5]
}
students.update(new_students)
pprint(students)

students_2 = students.copy()
del students_2['Jhon Doe'] 
pprint(students)
pprint(students_2)
students_2.clear()
print('=============')
pprint(students)
pprint(students_2)

#=======Tuple=========
t = (2.3, 'ABCD', False, (3, 5))
print(t[3][1])

t1 = (12, 'Hello', [1, 2, 3])
t1[2].append(5)
print(t1)
print(t1[1])
print(t1[:2])
print(2 in t1)
print({'a', 5, 'text'})
print({1,2,3,4,5})
x = {1, 2, 3, 5}
y = {2, 8}
print(x - y)
print(y - x)
print(x | y)
print(x & y)
print(x ^ y)
x.add(10)
x.remove(10)
x.remove(1) # если делать дважды, будет ошибка
x.discard(2) # будет удалять без ошибок
x.clear() # очистить множество
