"""
"""
'''
pizzas = ['Pipironi', 'Margarita', 'Shkol"naya']

for pizza in pizzas:
    print(f"I like {pizza}, pizza!")
'''

pizza = {
    'crust': 'thick',
    'toppings': ['mashrooms', 'extra cheese']
}

print(f"You orders a {pizza['crust']}")

for topping in pizza['toppings']:
    print(f"\t " + topping)