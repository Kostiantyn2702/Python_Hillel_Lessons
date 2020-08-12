"""
1. Дано целое число (int). Определить сколько нулей в этом числе.
"""

number = 1000
number_of_zeros = str(number).count("0")

print(number_of_zeros)

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

for index_1, number_1 in enumerate(my_list_1):
    if not number_1 % 2:
        my_result.append(my_list_1[index_1])

for index_2, number_2 in enumerate(my_list_2):
    if number_2 % 2:
        my_result.append(my_list_2[index_2])

print(my_result)

#########################################################

"""
4. Дан список my_list. 
Создать список new_list у которого первый элемент из my_list стоит на последнем месте. 
Если my_list [1,2,3,4], то new_list [2,3,4,1]
"""

my_list = [1, 2, 3, 4]
new_list = my_list.copy()
new_list.append(new_list.pop(0))

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

my_str_simple = "43 больше чем 34, но меньше чем 56."
# my_str = "fdb2dfbfd5dfbd 02,wefew5wefhiu   dawd 25 @@#$25"
sum_numbers_str = "" # Пустая строка для накопления цифр до пробелов.
sum_numbers_int = 0 # Переменная в которой будет сложение цифр, которые попали в строку sum_numbers_str до пробелов.

# Я наверно не так понял задание и имелись ввиду числа без сопутствующих букв(например "4А не равно 4" или та абракадабра из my_str).
my_list_simple = my_str_simple.split(" ")
for number in my_list_simple:
    if "," in number or "." in number:
        sum_numbers_int += int(number.strip(",."))
    elif number.isdigit():
        sum_numbers_int += int(number)

print(sum_numbers_int)

# Крутил, вертел, а вышло все также.

# for index, symbol in enumerate(my_str):
#     if index == len(my_str) - 1:
#         if symbol.isdigit():
#             sum_numbers_str += symbol
#             sum_numbers_int += float(sum_numbers_str)
#         else:
#             sum_numbers_int += float(sum_numbers_str)
#     elif symbol == " ":
#         sum_numbers_int += float(sum_numbers_str)
#         sum_numbers_str = "0"
#     elif symbol.isdigit() or symbol == ".":
#         sum_numbers_str += symbol
#
# print(sum_numbers_int)

# Первый вариант

# for index, num in enumerate(my_str):
#     if (index == len(my_str) - 1) and num.isdigit():
#         sum_numbers_str = sum_numbers_str + num
#         sum_numbers_int = sum_numbers_int + int(sum_numbers_str)
#     elif (index == len(my_str) - 1) and num.isalpha():
#         sum_numbers_int = sum_numbers_int + int(sum_numbers_str)
#     elif num.isdigit():
#         sum_numbers_str = sum_numbers_str + num
#     elif num == " ":
#         sum_numbers_int = sum_numbers_int + int(sum_numbers_str)
#         sum_numbers_str = "0"

# print(sum_numbers_int)

#########################################################

"""
7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список. 
Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_'). 
Примеры: 'abcd' -> ['ab', 'cd'], 'abc' -> ['ab', 'c_']
"""

my_str = "abc"
my_list = []
# my_two_symbols = ""
index = 0

# Не уверен что именно это Вы иммели ввиду, но стало короче и без elif .

if len(my_str) % 2:
    my_str = my_str + "_"

while len(my_list) < len(my_str) / 2:
    my_list.append(my_str[index:(index + 2)])
    index += 2


# while index <= len(my_str) - 1:
#     my_two_symbols += my_str[index]
#     if len(my_two_symbols) == 2:
#         my_list.append(my_two_symbols)
#         my_two_symbols = ""
#     elif len(my_two_symbols) == 1 and index == len(my_str) - 1:
#         my_two_symbols += "_"
#         my_list.append(my_two_symbols)
#     index += 1

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
count = 0
index = 0

# В самом условии не напсиано что это сумма двух соседей, а в примере сумма. Меня запутало.
# Поэтому сделал вариант для суммы и для каждого из соседей по отдельности.

# Вариант №1. Для суммы соседей.

for number in list_number[1:-1]:
    if number > list_number[index] + list_number[index + 2]:
        count += 1
    index += 1

# Укороченый прошлый вариант.

# for index, number in enumerate(list_number):
#     if index != 0 and index != len(list_number) - 1 and number > list_number[index + 1] + list_number[index - 1]:
#         count += 1

print(count)

# Вариант №2. Для соседей по отдельности.

# for index, number in enumerate(list_number):
#     if index != 0 and index != len(list_number) - 1 and max(list_number[index + 1] , list_number[index - 1]) < number:
#         count += 1
#
# print(count)