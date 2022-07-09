"""
user.py  file!
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
    'phil':'python'
}

frends = ['phil', 'sarsh']
for name in favorite_languages.keys():
    print(name.title())

    if name in frends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")






'''
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
'''
'''
for name in favorite_languages.values():
    print(name.title())
'''
