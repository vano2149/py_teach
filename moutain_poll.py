"""
mauntain_poll.py file!
"""

personses = {}

polling_active = True

while polling_active:

    name = input("/nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    personses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print(personses.items())

print("\n--- Poll Results ---")
for name, pesronse in personses.items():
    print(f"{name} would like to climb {response}.")

