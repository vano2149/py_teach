"""
tables.py file!
"""

table = int(input("What table do you want? "))

active = True

while active:
    if table > 8:
        print(f"All tables are busy!")
        active = False
    else:
        print("Your table all ready!")
        active = False
    