"""
"""

requested_toppings = ['mushrooms','green peppers','extra cheese']
"""
for requested_topping in requested_toppings:
    counter = 0
    for i in requested_topping:
        if i == 'e':
            print(i)
            counter += 1
        if counter == 2:
            print(f"adding {requested_topping}")
            break
print(f"\n Finished making your pizza!")
"""
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Soory, we are out of green peppers right now!")
    else:
        print(f"Adding {requested_topping}!")


