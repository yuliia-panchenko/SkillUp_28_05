# Задание 2
# Создайте программу «Англо-французский словарь». Нужно хранить слово на английском языке и его перевод на
# французский. Требуется реализовать возможность добавления, удаления, поиска, замены данных.
# Используйте словарь для хранения информации.

eng_french_dict = {
    'hello': 'bonjour',
    'day': 'journée',
    'night': 'nuit',
    'sun': 'soleil',
    'moon': 'lune'
}
for key in eng_french_dict:
    print(key, '-', eng_french_dict[key])
print('=====================')

# добавим элемент
eng_french_dict['jump'] = 'sauter'
print('Добавим новое слово')
for key in eng_french_dict:
    print(key, '-', eng_french_dict[key])
print('=====================')

# удалим элемент
del eng_french_dict['sun']
eng_french_dict.popitem()
eng_french_dict.pop('day')
print('Удалим некоторые слова')
for key in eng_french_dict:
    print(key, '-', eng_french_dict[key])
print('=====================')

# поиск элемента
print('day' in eng_french_dict)  # False
print('day' not in eng_french_dict)  # True
print('Перевод hello на французский')
print(eng_french_dict.get('hello'))  # bonjour
print('=====================')

# замена данных
eng_french_dict['hello'] = 'salut'
eng_french_dict.update({'night': 'l\' obscurité', 'bed': 'lit'})  # заменим значение и добавим новое слово
print('Изменим некоторый перевод')
for key in eng_french_dict:
    print(key, '-', eng_french_dict[key])
print('====================')
