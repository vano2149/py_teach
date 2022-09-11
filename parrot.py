"""
parrot.py file!
"""

prompt = "\n Tell me somthing, and I will repead it back to you:"
prompt += "\n Enter 'quit' to end the program."

active = True

while active:
    number = int(input("Enter a number, and i'll tell you if it's even or odd "))
    if number == 0:
        active = False
    elif number % 2 == 0:
        print(f"\nThe number {number} is even.")
    else:
        print(f"\nThe number {number} is odd.")


