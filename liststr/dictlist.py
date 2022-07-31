"""
dictlist.py file!
"""

alien_0 = {
    'color': 'green',
    'point': 5,
}

alien_1 = {
    'color': 'yellow',
    'point': 10,
}

alien_2 = {
    'color': 'red',
    'point': 15,
}
'''
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
'''


# Создает пустой список для хранения наших словарей!
aliens = []

#Создание 30 пришельцев с помощью конструкции for ... in range(): ->!
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#Вывод в терминал первых 5-ти пришельцев!
for alien in aliens[:5]:
    print(alien)
print('...')