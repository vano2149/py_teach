"""
Словари!!!
"""


"""
Словарь опребеляется ключевым словом 'dict()', либо {}
Первый дип данных 'не мутирующий тип данных' ключ - key 
Второй тип данных 'мутирующий' - значение - value
"""

a = {
    'user1':{
        "name": "John",
        "email": "john@example.com",
        "password": "*********",
        "age":27,
    },
    "user2" : {
        "name": "Bob",
        "email": "bob@example.com",
        "password": "password2",
        "age":20,
    },
    }

"""
for i in a.keys():
    if i == "user1":
        for j in a[i]:
            print(f'Hi user : {a[i][j]}')
"""
a['user3'] = {
    "name": "Alice",
    "email": "Alice@example.com",
    "password": "password3",
    "age":19,
}

print(a)