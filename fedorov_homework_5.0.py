"""
1. Дано целое число (int). Определить сколько нулей в этом числе.
"""

number = 1000
print(list(str(number)).count("0"))

#########################################################

"""
2. Дано целое число (int). Определить сколько нулей в конце этого числа.
"""

number = 10011230000
number_list = list(str(number))
count = 0

# Вариант №1
# Второй вариант вышел короче, но этот решил оставить в комментариях.
# for num in number_list[::-1]:
#     if num == "0":
#         count += 1
#     else:
#         print(count)
#         break

# Вариант №2
while number_list.pop() == "0":
    count += 1

print(count)

#########################################################

"""
3. Даны списки my_list_1 и my_list_2. 
Создать список my_result в который вначале поместить четные элементы из my_list_1 и потом нечетные элементы из my_list_2.
"""

my_list_1 = [50, 70, 15, 14, 67, 2435, 3251]
my_list_2 = [657, 546, 23, 123, 43, 54, 676]
my_result = []

for index_1 in range(len(my_list_1)):
    if not index_1 % 2:
        my_result.append(my_list_1[index_1])

for index_2 in range(len(my_list_2)):
    if index_2 % 2:
        my_result.append(my_list_2[index_2])

print(my_result)

#########################################################

"""
4. Дан список my_list. 
Создать список new_list у которого первый элемент из my_list стоит на последнем месте. 
Если my_list [1,2,3,4], то new_list [2,3,4,1]
"""

my_list = [1, 2, 3, 4]
new_list = []

for index, value in enumerate(my_list):
    if index != 0:
        new_list.append(value)

new_list.append(my_list[::-1].pop())

print(new_list)

#########################################################

"""
5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место. [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя!
"""

my_list = [1, 2, 3, 4]
my_list.append(my_list.pop(0))
print(my_list)

#########################################################

"""
6. Дана строка в которой есть числа (разделяются пробелами). 
Например "43 больше чем 34, но меньше чем 56". 
Найти сумму ВСЕХ чисел в этой строке. 
Для данного примера 133.
"""

# my_str = "43 больше чем 34, но меньше чем 56"
my_str = "fdb2dfbfd5dfbd 02,wefew5wefhiu   dawd 25 @@#$25   "
sum_numbers_str = "" # Пустая строка для накопления цифр до пробелов.
sum_numbers_int = 0 # Переменная в которой будет сложение цифр, которые попали в строку sum_numbers_str до пробелов.

# Получилось как-то громоздко, но идей как это можно сжать или другого варианта решения пока нет. :(

for index, num in enumerate(my_str): # Использую enumerate чтобы пройтись и по индексу и по самим символам.
    if (index == len(my_str) - 1) and num.isdigit(): # Первым условием проверяю не в конце ли символ, потому-что в конце строки может не быть пробелов и цифра ли это.
        sum_numbers_str = sum_numbers_str + num # Если это цифра, то добавляем ее в строку.
        sum_numbers_int = sum_numbers_int + int(sum_numbers_str) # А потом суммируем с тем что насобиралось за весь цикл.
    elif (index == len(my_str) - 1) and num.isalpha(): # Условие при котором в конце строки будет стоять символ, тогда добавлять его в строку sum_numbers_str невозможно.
        sum_numbers_int = sum_numbers_int + int(sum_numbers_str) # Поэтому просто суммируем все что накопилось за весь цикл.
    elif num.isdigit(): # По сути основное условие. Если строка это цифра, то добавляем ее в строку sum_numbers_str в которой собираются цифры до пробелов.
        sum_numbers_str = sum_numbers_str + num
    elif num == " ": # Сигнал о том, что пора приводить sum_numbers_str к типу int
        sum_numbers_int = sum_numbers_int + int(sum_numbers_str) # И суммировать его с такими же товарищами.
        sum_numbers_str = "0" # Обнуляем строку sum_numbers_str, потому что там уже есть какие-то цифры, а так как у нас появился разделительный символ, то нужно собирать цифры без учета старых

print(sum_numbers_int)

#########################################################

"""
7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список. 
Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_'). 
Примеры: 'abcd' -> ['ab', 'cd'], 'abc' -> ['ab', 'c_']
"""

my_str = "abcde"
my_list = []
my_two_symbols = ""
index = 0

while index <= len(my_str) - 1:
    my_two_symbols += my_str[index]
    if len(my_two_symbols) == 2:
        my_list.append(my_two_symbols)
        my_two_symbols = ""
    elif len(my_two_symbols) == 1 and index == len(my_str) - 1:
        my_two_symbols += "_"
        my_list.append(my_two_symbols)
    index += 1

print(my_list)

#########################################################

"""
8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit, которые точно находятся в этой строке. 
Причем l_limit левее чем r_limit. В переменную sub_str поместить часть строки между этими символами. 
my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"
"""

my_str = "My_long str"
l_limit = "o"
r_limit = "t"

sub_str = my_str[(my_str.find(l_limit) + 1):my_str.find(r_limit)]

print(sub_str)

#########################################################

"""
9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit, которые точно находятся в этой строке. 
Причем l_limit левее чем r_limit. 
В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами. 
my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
"""

my_str = "My long string"
l_limit = "o"
r_limit = "g"

sub_str = my_str[(my_str.find(l_limit) + 1):my_str.rfind(r_limit)]

print(sub_str)


#########################################################

"""
10. Дан список чисел. 
Определите, сколько в этом списке элементов, которые больше двух своих соседей (слева и справа), и выведите количество таких элементов. 
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей. 
Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
"""

list_number = [2, 4, 1, 5, 3, 9, 0, 7]
number_between_neighbours = 0
count = 0

# В самом условии не напсиано что это сумма двух соседей, а в примере сумма. Меня запутало.
# Поэтому сделал вариант для суммы и для каждого из соседей по отдельности.

# Вариант №1. Для суммы соседей.

for index, number in enumerate(list_number):
    if index == 0:
        continue
    elif index == len(list_number) - 1:
        print(count)
        break
    else:
        if number > list_number[index - 1] + list_number[index + 1]:
            count += 1
        else:
            continue

# Вариант №2. Для соседей по отдельности.

# for index, number in enumerate(list_number):
#     if index == 0:
#         continue
#     elif index == len(list_number) - 1:
#         print(count)
#         break
#     else:
#         if list_number[index + 1] < number > list_number[index - 1]:
#             count += 1
#         else:
#             continue