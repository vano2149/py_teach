"""
confirmed_users.py file!
"""

topping = []

quit = True

while quit:
    write = input("Введите добавку: ")
    if write != "quit":
        topping.append(write)
        print(topping)
    else:
        quit = False

print(topping)