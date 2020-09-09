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

