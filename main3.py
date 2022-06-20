"""
Глава 3 Списки.

1) Список объявляется как обычкая переменная
2) В список морно добавлять разные типы данных
    int -> Целое число.
    float -> Число с плавоющей запятой.
    str -> Строчка.

3) Для того чтобы вывести любой элемент списка,
необходимо знать index того элемента который хотим вывести в терминал.

4) Индексы начинаются не с 1 а С 0.
    Для того чтобы обратиться к последнему
    элементу списка используем данную конструкцию print(bicycles[-1]).
"""

bicycles = ['trek', "cannondale", 'redline','specialized']

num = [1,2,3,4,5,6,7,8,9]
print(bicycles)
print(num)
print("---------------------")
print(bicycles[0]) # -> Вывод в терминал первого элемента списка без изменений.
print('---------------------')
print(bicycles[0].title()) # -> Вывод в терминал первого элемента списка измененного методом .title()
print(bicycles[-2]) # -> Вывод в терминал последнего элемента списка.
print('---------------------')
print(bicycles[1]) # -> Вывод второго элемента нашего списка.