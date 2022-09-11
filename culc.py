"""
culc.py file
"""

'''
1 Складывать +
2 Вычитать +
3 умножать +
4 делить
5 Ввести знак!
'''



active = True
while active:
    x = input("Enter the first number : ")
    y = input("Enter the second number : ")
    sign = input("Enter the sign : ")
    if sign == '+' and sign != "quit" and x != "quit" and y != "quit":
        x = int(x)
        y = int(y)
        print(x + y)

    elif sign == "-" and sign != "quit" and x != "quit" and y != "quit":
        x = int(x)
        y = int(y)
        print(int(x - y))
    
    elif sign == "*" and sign != "quit" and x != "quit" and y != "quit":
        x = int(x)
        y = int(y)
        print(int(x * y))

    elif sign == "/" and sign != "quit" and x != "quit" and y != "quit":
        x = int(x)
        y = int(y)
        print(int(x / y))
    else:
        active = False
