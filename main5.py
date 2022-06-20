"""
Глава 3 Удаление списка при помощи метода pop().
"""

motocycles = [
    'honda',
    'yamaha',
    'suzuki',
]
print(motocycles)
#print(motocycles.pop(0))
last_owned = motocycles.pop(0)
print(type(last_owned))
print(f"The last motocycle I owned was a {last_owned.title()}.")

