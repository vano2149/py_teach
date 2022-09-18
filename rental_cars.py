"""
Rental_cars.py
"""

rental_car = input("Enter car name wich need to find!: ")

active = True

while active:
    if rental_car != "quit":
        print(f"Let me see if I can find you {rental_car}")
        break
    else:
        active = False