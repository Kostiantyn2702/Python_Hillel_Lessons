"""
1) У вас есть список значений my_list и список индексов my_indexes 
(начинается с нуля и количество элементов совпадает с количеством в my_list. 
Распечатать значения из my_list через обращение по индексу. См. пример выше.
"""

my_list = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven"]
my_indexes = []
n = 0
exit_flag = True

while exit_flag: # Автоматически заполняет список индексов для списка
    if len(my_indexes) < len(my_list):
        my_indexes.append(n)
        n += 1
    else:
        exit_flag = False

for index in my_indexes:
    print(my_list[index])

#####################################################

"""
2) У вас есть два списка my_list_1 и my_list_2 равной длинны и список индексов my_indexes 
(начинается с нуля и количество элементов совпадает с количеством в my_list_1. 
Распечатать пары значений из my_list_1 и my_list_2 через обращение по индексу. 

Например для списков [1, 3] и [2, 4]:
(1, 2)
(3, 4)
"""

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [6, 7, 8, 9, 10]
my_indexes = []
n = 0
exit_flag = True

while exit_flag: # Автоматически заполняет список индексов для списка
    if len(my_indexes) < len(my_list_1):
        my_indexes.append(n)
        n += 1
    else:
        exit_flag = False

for index in my_indexes:
    print((my_list_1[index], my_list_2[index]))

#####################################################

"""
3) У вас есть строка my_string = '0123456789'. 
Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список. 
Задание нужно выполнить ТОЛЬКО через цикл в цикле и приведение типов (См. пример выше). 
Генерирование через range или другие "фишки" я засчитывать не буду ))
"""

my_string_1 = '0123456789'
my_string_2 = '0123456789'
my_list_new = []

for number_1 in my_string_1:
    for number_2 in my_string_2:
        my_list_new.append(int(number_1 + number_2)) # Сначала происходит конкатенцаия, потом приведение, а потом добавляет число в конец списка

print(my_list_new)