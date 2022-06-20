"""
Лекция 7.
"""

names = [
    'Alice',
    'Bob',
    'Ivan',
    'her',
    ]

# insert() - добавление элемента в список по значению.
# pop() - вытаскивает элемент списка и удалает его.
print(names)

names.insert(0,"John")

print(names)

print(names.pop(0))
# remove() - удаление элемента списка по значению.
print(names)

names.remove('her')

print(names)


