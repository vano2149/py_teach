"""
Multipl.py file!
"""

number = int(input("Enter the number: "))

active = True

while active:
    if number % 10 == 0:
        print(f"Your {number} is multipl 10.")
        active = False
    else:
        print(f"Your {number} isn't multipl 10.")
        active = False