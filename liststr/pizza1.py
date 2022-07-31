"""
pizza1.py file!
"""

#Описание информации о заказанной пицце!
pizza = {
    'crust' : 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# Описагние заказа !

print(f"You order a {pizza['crust']} - crust pizza " 
    "with the folowing topings:")

for topping in pizza['toppings']:
    print('\t' + topping)
