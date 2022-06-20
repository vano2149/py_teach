# Лекция 2 Работа со строчками.

## Шаг 0.

Для того чтобы передать переменную в строчку необходимо использовать конструкцию приведенную ниже 

```
first_name = "alice"

last_name = "John"

print(f"ahsdfjkasbdf{first_name} {last_name}")
```

Шаг 1. 

В Python -> существует нестолько методов приобразования наших строчек.

```
first_name = "alice"

last_name = "JOHN"

print(first_name.upper())
print(last_name.lower())
```

метод `title()` 
он пишнт наше имя и фамилию с заглавной быквы

```
last_name = "alice"

first_name = "john"

print(f"{last_name.title()}\n{first_name.title()}")

```
## Вывод из терминала
```
Alice
John
```

Метод `rstrip()` , `lstrip()`

```
rstrip() -> удаление всех пробелов справа.
lstrip() -> удаление всех пробелов слева.
```
## Дз -> Глава 2 до ЧИСЕЛ (до стр. 43) 