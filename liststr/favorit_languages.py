"""
"""

fovorite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


alien_0 = {
    'color': 'green',
    'speed': 'slow',
}
point_value = alien_0.get('point')

information_about = {
  'first_name' : 'Ivan',
  'last_name' : 'Kalko',
  'surname' : 'Ivanovich',
  'age' : 27,
  'city' : 'Moscow izi_pizi',
}

if __name__ == '__main__':
    for k, v in information_about.items():
        print(f'\nKey: {k}')
        print(f"Value: {v}")
    print('-' * 20)
    for name, language in fovorite_languages.items():
        print(f"{name.title()}'s favorite language is {language.title()}.")
    print('-' * 20)

    for name in fovorite_languages.keys():
        print(name.title())
    print('-' * 20)
    for value in fovorite_languages.values():
        print(value.title())
