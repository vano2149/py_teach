"""
mauntain_poll.py file!
"""

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which moutine would you like to climb someday? ")

    responses[name] = response

    repead = input("Would you like to let another person respond ? (yes / no) ")
    if repead == 'no':
        polling_active = False

print("\n--- Poll Results ---")

for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
    

