# Цикл While.
## Задача 1 
По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.

## Решение

```
n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1
```

## Задача 2

Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.

## Решение

```
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)
```

## Задача 3



### Решение.
```
a = int(input())
while a != 0: # True False
    if a < 0: # False
        print("Встретилось отрицательное цисло:", a)
        break # Принудительный медтод остановки цикла.
    a = int(input())
else:
    print('Ни одного числа не встретиловь', a)
```

## Наименование математических знаков.

= -> Передача переменной какого либо значание
Пример:
```
i = 1
i = "Ghbdtn"
i = [
    "Ghbdtn",
    "Alice",
    "Bob",
]
```
== -> Сравнения значения перененной с значением другой переменной. 
Пример:
```
i = 2
x = 3

if x == i:
    print("x == i")
esle:
    print("x != i")
```

** -> Возведение в степень числа.
Пример:
```
i = 1 
i ** 2 

x = 3 
x ** 3
```
!= -> Знак отрицания.
Пример использования.
```
i = int(input())

x = int(input())

if x != i :
    print("x != i")
else:
    print("x == i")
```
* < - Меньше
* `>` - Больше
* <= - Меньше либо равно.
* `>=` - Больше либо равно.

* % - Остаток от деления.