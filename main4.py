"""
Обращение к отдельным элементам списка.
"""

names = ['Ivan', 'alice','bob', 'Vasya']

massage1 = 'What is your name?'
message2 = f'Hi my name is {names[1].title()}.'
print(massage1, message2)

print(f"Hi my name is , {names[0].title()}")
print(f"Hi my name is , {names[1].title()}")
print(f"Hi my name is , {names[2].title()}")
print(f"Hi my name is , {names[3].title()}")

print('---------------------------')


