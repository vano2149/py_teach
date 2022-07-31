"""
user.py  file!
Page -> 117!
"""

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
'''
for k, v in user_0.items():
    print(f'\nKey: {k}')
    print(f'Value: {v}')
'''

favorite_languages = {
    "jen": "python",
    "sarsh": "c",
    "edward" : "ruby",
    'phil':'python',
    'eric': 'python',
}

# метод set() -> это множество принемающая в себя только уникальные элементы!
#favorite_languages = {1,2,3,4,5,6,7,8,9} пример создания множества!


print('The following languages have been mentioned!')
for language in set(favorite_languages.values()):
    print(language.title())


'''
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thenk you for taking the poll!")



frends = ['phil', 'sarsh']
for name in favorite_languages.keys():
    print(name.title())

    if name in frends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
    if 'eric' not in favorite_languages.keys():
        print('Eric, pleas take our poll!')


for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
'''
'''
for name in favorite_languages.values():
    print(name.title())
'''
