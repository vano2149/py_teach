"""
Работа цикла while методом input():
"""

a = int(input())
while a != 0: # True False
    if a < 0: # False
        print("Встретилось отрицательное цисло:", a)
        break # Принудительный медтод остановки цикла.
    a = int(input())
else:
    print('Ни одного числа не встретиловь', a)