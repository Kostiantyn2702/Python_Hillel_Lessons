# import string
# import datetime
# import math


"""
Ваше задание здесь создать функцию, которая получает массив(tuple) и возвращает набор с 3 элементами - первым, третьим, вторым с конца.
"""

# def easy_unpack(massive_tuple):
#     result = (massive_tuple[0], massive_tuple[2], massive_tuple[-2])
#     return result

"""Дана строка и нужно найти ее первое слово."""

# def first_word(text: str) -> str:
#     for index, symbol in enumerate(text):
#         if " " not in text:
#             result = text
#         elif symbol == " ":
#             result = text[0:index]
#             break
#     return result

# def first_word(text):
#     index = text.find(" ")
#     return text[:index] if index != -1 else text

"""
In this mission, you need to create a password verification function.
The verification condition is:
the length should be bigger than 6.
"""

# def is_acceptable_password(password: str) -> bool:
#     if len(password) < 6 or len(password) == 6:
#         return False
#     return True

"""You have a positive integer. Try to find out how many digits it has?"""

# def number_length(a: int) -> int:
#     return len(str(a))

"""Попробуйте выяснить какое количество нулей содержит данное число в конце."""

# def end_zeros(num):
#     list_num = list(str(num))
#     result = ""
#     for i in range(len(str(num))):
#         if list_num[-1] == "0":
#             result += list_num.pop()
#     return len(result)

"""You should return a given string in reverse order."""

# def backward_string(val: str) -> str:
#     return val[::-1]

"""Not all of the elements are important. What you need to do here is to remove from the list all of the elements before the given one."""

# def remove_all_before(items: list, border: int):
#     return items[items.index(border):] if border in items else items

"""Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True."""

# def is_all_upper(text: str) -> bool:
#     if text.isupper():
#         return True
#     elif text == "":
#         return True
#     elif text.islower():
#         return False
#     elif text.islower() and text.isupper():
#         return False

# def is_all_upper(text: str) -> bool:
#     return text.upper() == text

"""In a given list the first element should become the last one. An empty list or list with only one element should stay the same."""

# def replace_first(items: list):
#     items.append(items.pop(0)) if len(items) != 0 else items
#     return items

"""You have a number and you need to determine which digit in this number is the biggest."""

# def max_digit(number: int) -> int:
#     for num in str(number):
#         maximum = str(number)[0]
#         if num >= maximum:
#             maximum = num
#         elif len(str(number)) == 1:
#             maximum = number
#     return int(maximum)

"""
Найдите ближайшее значение к переданному.
Вам даны список значений в виде множества (Set) и значение, относительно которого, надо найти ближайшее.
Например, мы имеем следующий ряд чисел: 4, 7, 10, 11, 12, 17. И нам нужно найти ближайшее значение к цифре 9. 
Если отсортировать этот ряд по возрастанию, то слева от 9 будет 7, а справа 10. Но 10 - находится ближе, чем 7, значит правильный ответ 10.

Несколько уточнений:
Если 2 числа находятся на одинаковом расстоянии - необходимо выбрать наименьшее из них;
Ряд чисел всегда не пустой, т.е. размер >= 1;
Переданное значение может быть в этом ряде, а значит оно и является ответом;
В ряде могут быть как положительные, так и отрицательные числа, но они всегда целые;
Ряд не отсортирован и состоит из уникальных чисел.
"""

# def nearest_value(values: set, one: int) -> int:
#     list_values = list(values)
#     min_val = list_values[0]
#     max_val = list_values[-1]
#     for val in list_values:
#         if val < one:
#             min_val = val
#         elif val > one and val < max_val:
#             max_val = val
#     if one in list_values:
#         return one
#     elif (one - min_val) > (max_val - one):
#         return max_val
#     elif (one - min_val) < (max_val - one):
#         return min_val
#     elif (one - min_val) == (max_val - one):
#         return min_val

"""
Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий.

Это упрощенная версия миссии Between Markers.

Начальный и конечный маркеры всегда разные.
Начальный и конечный маркеры всегда размером в один символ.
Начальный и конечный маркеры всегда есть в строке и идут один за другим.
"""

# def between_markers(text: str, begin: str, end: str) -> str:
#     result = text[text.find(begin) + 1:text.find(end)]
#     return result

"""
Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий:

Начальный и конечный маркеры всегда разные
Если нет начального маркера, то началом считать начало строки
Если нет конечного маркера, то концом считать конец строки
Если нет ни конечного, ни начального маркеров, то просто вернуть всю строку
Если конечный маркер стоит перед начальным, то вернуть пустую строку
"""

# def between_markers(text: str, begin: str, end: str) -> str:
#     if begin not in text and end not in text:
#         return text
#     if begin not in text:
#         return text[:text.find(end)]
#     if end not in text:
#         return text[text.find(begin) + len(begin):]
#     if text.find(end) < text.find(begin):
#         return ""
#     result = text[text.find(begin) + len(begin):text.find(end)]
#     return result

# def between_markers(text: str, begin: str, end: str) -> str:
#     begin_idx = text.index(begin) + len(begin) if begin in text else 0
#     end_idx = text.index(end) if end in text else len(text)
#     return text[begin_idx: end_idx]

"""
На вход Вашей функции будет передано одно предложение. 
Необходимо вернуть его исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.
"""

# def correct_sentence(text: str) -> str:
#     if not text.istitle():
#         text = text[0].upper() + text[1:]
#     if not text.endswith("."):
#         text = text + "."
#     return text

# def correct_sentence(text: str):
#     text = text.rstrip(".")
#     return text[0].upper() + text[1:] + "."

"""
In a given text you need to sum the numbers. Only separated numbers should be counted. If a number is part of a word it shouldn't be counted.
The text consists from numbers, spaces and english letters
"""

# def sum_numbers(text: str) -> int:
#     list_text = text.split(" ")
#     result = 0
#     for element in list_text:
#         if element.isdigit():
#             result += int(element)
#     return result

"""
Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного массива. 
Не забудьте, что первый элемент массива имеет индекс 0.
Для пустого массива результат всегда 0 (ноль).
"""

# def checkio(array: list) -> int:
#     sum_numbers = 0
#     for index, number in enumerate(array):
#         if not index % 2:
#             sum_numbers += array[index]
#     result = sum_numbers * array[-1] if len(array) > 0 else 0
#     return result

# def checkio(array: list) -> int:
#     return sum(array[::2]) * sum(array[-1:])

"""
Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми. 
В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left", даже если это часть другого слова. 
Все строки даны в нижнем регистре.
"""

# def left_join(phrases: tuple) -> str:
#     return ",".join(phrases).replace("right", "left")

"""
Дана строка и нужно найти ее первое слово.
При решении задачи обратите внимание на следующие моменты:
В строке могут встречатся точки и запятые
Строка может начинаться с буквы или, к примеру, с пробела или точки
В слове может быть апостроф и он является частью слова
Весь текст может быть представлен только одним словом и все
"""

# def first_word(text: str) -> str:
#     text = text.split(" ")
#     for txt in text:
#         # txt.split(".")
#         if txt != "" and "." not in txt:
#             return txt.rstrip(",")
#     return txt.split(".")[0]

# def first_word(text: str) -> str:
#     text=text.replace('.',' ')
#     text=text.replace(',',' ')
#     text=text.strip()
#     text=text.split(' ')
#     return text[0]

"""
Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами). 
Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд. 
Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
"""

# def checkio(words: str) -> bool:
#     counter = 0
#     split_words = words.split(" ")
#     for value in split_words:
#         if counter == 3:
#             return True
#         elif value.isalpha():
#             counter += 1
#         else:
#             counter = 0
#     return True if counter == 3 else False


"""
У вас есть две даты в кортежах с тремя числами - год, месяц и день. Например, 19 апреля 1982 будет (1982, 4, 19). 
Вы должны найти разницу в днях между имеющимися датами. Например, между сегодня и вчера = 1 день. 
Разница между днями всегда будет положительной или нулем, не забывайте про абсолютное значение.
"""

# def days_diff(a, b):
#     year_a, month_a, day_a = a
#     year_b, month_b, day_b = b
#     result = abs((datetime.date(year_a, month_a, day_a)-datetime.date(year_b, month_b, day_b)).days)
#     return result

# from datetime import date
#
# def days_diff(a, b):
#     return abs((date(*a)-date(*b)).days)

"""You need to count the number of digits in a given string."""

# def count_digits(text: str) -> int:
#     count = 0
#     for i in text:
#         if i.isdigit():
#             count += 1
#     return count

"""In a given string you should reverse every word, but the words should stay in their places."""

# def backward_string_by_word(text: str) -> str:
#     list_text = text.split(" ")
#     new = []
#     for word in list_text:
#         new.append(word[::-1])
#     return " ".join(new)

"""Дана таблица всех доступных продуктов на складе. Данные представлены в виде списка словарей (a list of dicts)
Ваша миссия тут - это найти ТОП самых дорогих товаров. Количество товаров, которые мы ищем, будет передано в первом аргументе, а сами данные по товарам будут переданы вторым аргументом."""

# def sort_dict_key(value_dict:dict) -> int:
#     return value_dict["price"]
#
# def get_sorted_by(list_price) -> list:
#     sorted_by = sorted(list_price, key=sort_dict_key, reverse=True)
#     return sorted_by
#
# def bigger_price(limit: int, data: list) -> list:
#     return get_sorted_by(data)[:limit]

"""Дан непустой массив целых чисел (X). В этой задаче вам нужно вернуть массив, состоящий только из неуникальных элементов данного массива. 
Для этого необходимо удалить все уникальные элементы (которые присутствуют в данном массиве только один раз). 
Для решения этой задачи не меняйте оригинальный порядок элементов. 
Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и результат будет [1, 3, 1, 3]."""

# def checkio(data: list) -> list:
#     new_data = []
#     for i in data:
#         if data.count(i) > 1:
#             new_data.append(i)
#     return new_data

"""Ваша задача в этой миссии определить популярность определенных слов в тексте.
На вход вашей функции передается 2 аргумента. Текст и массив слов, популярность которых необходимо определить.
При решении этой задачи обратите внимание на следующие моменты
Слова необходимо искать во всеx регистрах. Т.е. если необходимо найти слово "one", значит для него будут подходить слова "one", "One", "oNe", "ONE" и.т.д.
Искомые слова всегда указаны в нижнем регистре
Если слово не найдено ни разу, то его необходимо вернуть в словаре со значением 0 (ноль)"""

# def popular_words(text: str, words: list) -> dict:
#     list_text = text.lower().replace("\n", " ").split(" ")
#     print(list_text)
#     new_dict = {}
#     for word in words:
#         new_dict[word] = list_text.count(word)
#     return new_dict

"""Даны 2 строки. Необходимо найти индекс второго вхождения второй строки в первую.

Разберем самый первый пример, когда необходимо найти второе вхождение "s" в слове "sims". 
Если бы нам надо было найти ее первое вхождение, 
то тут все просто: с помощью функции index или find мы можем узнать, что "s" – это самый первый символ в слове "sims", 
а значит индекс первого вхождения равен 0. 
Но нам необходимо найти вторую "s", а она 4-ая по счету. 
Значит индекс второго вхождения (и ответ на вопрос) равен 3."""

# def second_index(text: str, symbol: str) -> [int, None]:
#     count = 0
#     for index, i in enumerate(text):
#         if i == symbol:
#             if count == 1:
#                 return index
#             count = 1
#     return None if count == 0 else None

"""Отсортируйте данный итератор таким образом, чтобы его элементы оказались в порядке убывания частоты их появления, 
то есть по количеству раз, которое они появляются в элементах. 
Если два элемента имеют одинаковую частоту, они должны оказаться в том же порядке, в котором стояли изначально в итераторе."""

# def get_max_count_and_value(my_list):
#     max_count = 0
#     max_count_value = 0
#     for value in my_list:
#         if max_count < my_list.count(value):
#             max_count = my_list.count(value)
#             max_count_value = value
#     return max_count, max_count_value
#
# def del_max_count_and_append_value(my_list, new_list):
#     max_count_value = get_max_count_and_value(my_list)[1]
#     while max_count_value in my_list:
#         for index, value in enumerate(my_list):
#             if value == max_count_value:
#                 new_list.append(my_list.pop(index))
#
# def create_sorted_list(my_list):
#     new_list = []
#     while len(my_list) != 0:
#         del_max_count_and_append_value(my_list, new_list)
#     return new_list
#
# def frequency_sort(my_list):
#     return create_sorted_list(my_list)


# def frequency_sort(items):
#     return sorted(items, key=lambda x: (-items.count(x), items.index(x)))

"""
Шахматы - это стратегическая игра двух игроков, которая разыгрывается на игровой доске с клетками, расположенными в восьми рядах (называемых горизонталями и обозначаемых цифрами от 1 до 8) 
и в восьми колонках (называемых вертикалями и обозначаемых буквами от a до h). 
Каждая клетка доски идентифицируется уникальной парой координат, состоящей из буквы и цифры (например, "a1", "h8", "d6"). 
В этой задаче мы будем иметь дело только с пешками. Пешка может бить пешку противника, которая находится перед ней в соседней клетке по диагонали справа или слева, переходя в эту клетку. 
У белых пешек клетки перед ними имеют номер горизонтали на единицу больше.

Сама по себе пешка является слабой фигурой, но мы можем использовать до восьми пешек для построения оборонительной стены. 
Стратегия оборонительной стены основывается на защите друг друга. Пешка защищена, если её клетка находится по ударом другой своей пешки. 
На игровом поле находятся только белые пешки. Вы должны разработать код, позволяющий определить сколько пешек защищены в этой позиции.

Вам предоставляется набор координат, в которых расставлены белые пешки. Вы должны подсчитать количество защищенных пешек.
"""

# import string
#
# letters = string.ascii_lowercase
#
# def get_conditions(position):
#     pawn_position = letters.find(position[0])
#     first_condition = letters[pawn_position - 1] + str(int(position[1]) - 1)
#     second_condition = letters[pawn_position + 1] + str(int(position[1]) - 1)
#     return first_condition, second_condition
#
# def is_pawn_safe(position, my_dict):
#     first_condition, second_condition = get_conditions(position)
#     if first_condition in my_dict or second_condition in my_dict:
#         return 1
#     else:
#         return 0
#
# def safe_pawns(pawns) -> int:
#     count = 0
#     for position in pawns:
#         if is_pawn_safe(position, pawns):
#             count += 1
#     return count

# def getdiags(pawn):
#     c, r = map(ord, pawn)
#     return chr(c - 1) + chr(r - 1), chr(c + 1) + chr(r - 1)
#
# def safe_pawns(pawns):
#     return len([p for p in pawns if any(d in pawns for d in getdiags(p))]

"""
Ваша задача - определить угол солнца над горизонтом, зная время суток. 
Исходные данные: солнце встает на востоке в 6:00, что соответствует углу 0 градусов. В 12:00 солнце в зените, а значит угол = 90 градусов. 
В 18:00 солнце садится за горизонт и угол равен 180 градусов. 
В случае, если указано ночное время (раньше 6:00 или позже 18:00), функция должна вернуть фразу "I don't see the sun!".
"""

# def sun_angle(time):
#     one_hour_angle = 15
#     one_min_angle = 0.25
#     my_time = time.split(":")
#     if int(my_time[0]) < 6 or int(my_time[0]) > 18 or int(my_time[0]) == 18 and int(my_time[1]) > 0:
#         return "I don't see the sun!"
#     else:
#         return (int(my_time[0]) - 6) * one_hour_angle + (int(my_time[1]) * one_min_angle)
#
# def sun_angle(time):
#     h, m = list(map(int, time.split(':')))
#     angle = 15 * h + m / 4 - 90
#     return angle if 0 <= angle <= 180 else "I don't see the sun!"

"""
You have to split a given array into two arrays. 
If it has an odd amount of elements, then the first array should have more elements. 
If it has no elements, then two empty arrays should be returned.
"""

# def split_list(items: list) -> list:
#     new_list = []
#     if not len(items) % 2:
#         middle = len(items) // 2
#         new_list.append(items[:middle])
#         new_list.append(items[middle:])
#     else:
#         middle = int(len(items) / 2 + 0.5)
#         new_list.append(items[:middle])
#         new_list.append(items[middle:])
#     return new_list
#
# def split_list(items: list) -> list:
#     mid = (len(items) + 1) // 2
#     return [items[:mid], items[mid:]]

"""
В этой миссии Вам надо определить, все ли элементы массива равны.
"""

# my_list = []
# if len(set(my_list)) == 1 or len(set(my_list)) == 0:
#     print("True")
# else:
#     print("False")
#
# def all_the_same(elements):
#    return elements[1:] == elements[:-1]

"""
Компьютерный формат даты и времени обычно выглядит так: 21.05.2018 16:30
Люди предпочитают видеть эту же информацию в более развернутом виде: 21 May 2018 year, 16 hours 30 minutes
Ваша задача - преобразовать дату и время из числового формата и словесно-числовой.
"""

import re

def date_time(time: str) -> str:
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    reg_exp = r"[0-9]{2,4}"
    result = re.findall(reg_exp, time)
    day = str(int(result[0]))
    month = months[int(result[1]) - 1]
    year = result[2]
    hour = int(result[3])
    if hour == 1:
        hour = str(hour) + " hour"
    else:
        hour = str(hour) + " hours"
    minute = int(result[4])
    if minute == 1:
        minute = str(minute) + " minute"
    else:
        minute = str(minute) + " minutes"

    new_string = f"{day} {month} {year} year {hour} {minute}"
    return new_string

print(date_time("01.01.2000 00:00"))