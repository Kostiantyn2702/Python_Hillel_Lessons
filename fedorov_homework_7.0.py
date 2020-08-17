import random

"""
1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
Задание можно выполнить и через обычный цикл и через генератор списков.
"""

my_list = [random.randint(1, 100) for number in range(1,21)]

print(my_list)

########################################################################

"""
2) Создать словарь triangle в который записать точки A B C, и их координаты (кортежи) ,
созданные случайным образом с помощью модуля random.
"""

point_A = (random.randint(1, 100), random.randint(1, 100))
point_B = (random.randint(1, 100), random.randint(1, 100))
point_C = (random.randint(1, 100), random.randint(1, 100))

triangle = {"A" : point_A, "B" : point_B, "C" : point_C}

print(triangle)

########################################################################

"""
3) Создать функцию my_print, которая принимает строку и печатает ее
с тремя символами * вначале и в конце строки.
Пример:
my_str = 'I'm the string'
Печатает ***I'm the string***
"""

def my_print(string:str):
    symbol = "*" * 3
    result = f"{symbol}{string}{symbol}"
    print(result)

my_print("String, no!")

########################################################################

"""
4)Создать функцию my_print, которая принимает строку и печатает ее
с символами * НАД и ПОД строкой. КОЛИЧЕСТВО СИМВОЛОВ * РАВНО КОЛИЧЕСТВУ СИМВОЛОВ В СТРОКЕ
Пример:
my_str = 'I'm the string'
Печатает
**************
I'm the string
**************
"""

def my_print(string:str):
    symbol = "*" * len(string)
    result = f"{symbol}\n{string}\n{symbol}"
    print(result)

my_print("123456")

########################################################################

"""
5) То же, что 4, но ответ должен выглядеть так:
********************
***I'm the string***
********************
"""

def my_print(string:str):
    symbol = "*" * (len(string) + 6)
    result = f"{symbol}\n***{string}***\n{symbol}"
    print(result)

my_print("123456")
