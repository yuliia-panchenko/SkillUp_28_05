# Задание 1
# Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и его рост.
# Требуется реализовать возможность добавления, удаления, поиска, замены данных.
# Используйте словарь для хранения информации.

basketball_players = {
    'Шакил О’Нил': 216,
    'Майкл Джордан': 198,
    'Карим Абдул-Джаббар': 218,
    'Уилт Чемберлен': 216,
    'Леброн Джеймс': 206,
    'Коби Брайант': 198,
    'Билл Расселл': 208
}
for key in basketball_players:
    print(key, '-', basketball_players[key], 'см')
print('=====================')

# добавим элемент
basketball_players['Мэджик Джонсон'] = 206
for key in basketball_players:
    print(key, '-', basketball_players[key], 'см')
print('=====================')

# удалим элемент
del basketball_players['Карим Абдул-Джаббар']
basketball_players.popitem()
basketball_players.pop('Уилт Чемберлен')
for key in basketball_players:
    print(key, '-', basketball_players[key], 'см')
print('=====================')

# поиск элемента
print('Коби Брайант' in basketball_players)  # True
print('Уилт Чемберлен' not in basketball_players)  # True
print(basketball_players.get('Майкл Джордан'))  # 198
print('=====================')

# замена данных
basketball_players['Шакил О’Нил'] = 220
basketball_players.update({'Леброн Джеймс': 210, 'Оскар Робертсон': 196})  # заменим значеник и добавим нового игрока
for key in basketball_players:
    print(key, '-', basketball_players[key], 'см')
print('====================')

