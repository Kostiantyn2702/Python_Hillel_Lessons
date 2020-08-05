"""
1) У вас есть список my_list с значениями типа int.
Распечатать те значения, которые больше 100.
Задание выполнить с помощью цикла for.
"""

my_list = [100, 50, 120, 125, 1, 14, 78, 500]

for number in my_list:
    if number > 100:
        print(number)

#####################################################

"""
2) У вас есть список my_list с значениями типа int, и пустой список my_results. 
Добавить в my_results те значения, которые больше 100. 
Распечатать список my_results. Задание выполнить с помощью цикла for
"""

my_results = []

for number in my_list:
    if number > 100:
        my_results.append(number)

print(my_results)

#####################################################

"""
3) У вас есть список my_list с значениями типа int. 
Если в my_list количество элементов меньше 2, то в конец добавить значение 0. 
Если количество элементов больше или равно 2, то добавить сумму последних двух элементов. 
Количество элементов в списке можно получить с помощью функции len(my_list)
"""

my_list = [2, 2, 4, 6]
# my_list = []
exit_flag = True

while exit_flag:
    if len(my_list) < 2:
        my_list.append(0)
    elif len(my_list) >= 2:
        my_list.append((my_list[-1] + my_list[-2]))
        exit_flag = False

print(my_list)

#####################################################

"""
4) Пользователь вводит value - число с запятой (например 3.14) с клавиатуры. 
Вы приводите это value к типу float и выводите результат выражения value ** -1. 
Написать программу, которая вычисляет данное выражение и корректно обрабатывает возможные исключения. 
"""

value = "str"

while type(value) != type(3.14) or value == 0:
    try:
        value = float(input("Введите число с заппятой: ")) # Все числа типа int могут быть приведены к типу float.
        result = value ** -1
        print(result)
    except ValueError:
         print("Вы ввели набор символов. Попробуйте еще раз.")
    except ZeroDivisionError: # Вроде других ошибок быть не должно, но может я чего-то не знаю.
        print("Вы ввели ноль. Попробуйте еще раз.")