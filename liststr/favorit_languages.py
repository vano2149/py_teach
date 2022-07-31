"""
Словари! Глава 6
"""

# Словари это один из структурированных типов данных
# в Python, записываются фигурными скобраки "{}"

# В левай части словоря всегда содержится не мутирующий тип данных. называется ключем "key"
# в правой часте моделжится мутирующий тип данных. называется значением "values"


"""
user = {
    "lastname" : "Ivan",
    "firstname" : "Ivanov",
    "age": 27,
    "birthday" : "23.05.1991",
    "job": "manager",
}

a = user["lastname"]
print(f"Hi {a}! How are you?")
print(user["lastname"])
print(user["age"])
"""

"""
Для того что-бы добавить новую пару ключ/значение см пример ниже.
"""
"""
alien = {
    "color": "black",
    "points" : 5
}

alien["x_position"] = 0
alien["y_position"] = 25
print(alien)
"""

"""
alien_0 = {
    'color': "green",
}
print(f"The alien is {alien_0['color']}!")

alien_0["color"] = "yellow"

print(f"The alien is now {alien_0['color']}!")
"""

"""
alien_0 = {
    'x_position': 0,
    'y_position': 25,
    'speed': "medium",
}

print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == "slow":
    x_incriment = 1
elif alien_0['speed'] == "medium":
    x_incriment = 2
else:
    x_incriment = 3

alien_0['x_position'] = alien_0['x_position'] + x_incriment

print(f" New position: {alien_0['x_position']} !")
"""

alien_0 = {
    'x_position': 0,
    'y_position': 25,
    'speed': "medium",
}

point_value = alien_0.get('z_position', 'No point value assigned!')

print(point_value)



favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
}

for name , languages in favorite_languages.items():
    print(f"\n {name.title()}'s  favorite languages are: ")
    for langusge in languages:
        print(f"\t{langusge.title()}")