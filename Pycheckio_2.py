"""You have a text and a list of words. You need to check if the words in a list appear in the same order as in the given text.

Cases you should expect while solving this challenge:

a word from the list is not in the text - your function should return False;
any word can appear more than once in a text - use only the first one;
two words in the given list are the same - your function should return False;
the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
the text includes only English letters and spaces.
Input: Two arguments. The first one is a given text, the second is a list of words.

Output: A bool."""

# def words_order(text: str, words: list) -> bool:
#     my_words_index = []
#     text_list = text.split(" ")
#     for word in words:
#         if text_list.count(word) != 1 or words.count(word) != 1:
#             return False
#         my_words_index.append(text.find(word))
#     if my_words_index == sorted(my_words_index):
#         if (-1) in my_words_index:
#             return False
#         return True
#     elif my_words_index != sorted(my_words_index):
#         return False

# def words_order(text, words):
#     text_words = {w for w in text.split() if w in words}
#     return list(sorted(text_words, key=text.index)) == words

"""
In a given list the last element should become the first one. An empty list or list with only one element should stay the same
"""

# def replace_last(items: list):
#     if len(items) == 0:
#         return items
#     else:
#         items.insert(0, items.pop())
#         return items

"""
Дан массив с положительными числами и число N. Вы должны найти N-ую степень элемента в массиве с индексом N. 
Если N за границами массива, тогда вернуть -1. Не забывайте, что первый элемент имеет индекс 0.

Давайте посмотрим на несколько примеров:
- массив = [1, 2, 3, 4] и N = 2, тогда результат 3^2 == 9;
- массив = [1, 2, 3] и N = 3, но N за границами массива, так что результат -1.
"""

# def index_power(array: list, n: int) -> int:
#     if n > len(array) - 1:
#         return -1
#     answer = array[n]**n
#     return answer

# def index_power(array, n):
#     try: return array[n] ** n
#     except IndexError: return -1

"""
We have a List of booleans. Let's check if the majority of elements are true.

Some cases worth mentioning: 1) an empty list should return false; 2) if trues and falses have an equal amount, function should return false.
"""

# def is_majority(items: list) -> bool:
#     return True if items.count(True) > items.count(False) else False

"""
Not all of the elements are important. What you need to do here is to remove all of the elements after the given one from list.

For illustration, we have an list [1, 2, 3, 4, 5] and we need to remove all the elements that go after 3 - which is 4 and 5.

We have two edge cases here: (1) if a cutting element cannot be found, then the list shouldn't be changed; (2) if the list is empty, then it should remain empty.
"""

# def remove_all_after(items: list, border: int):
#     new_list = []
#     if border in items:
#         for value in items:
#             if value == border:
#                 new_list.append(value)
#                 return new_list
#             else:
#                 new_list.append(value)
#     else:
#         return items

# def remove_all_after(items: list, border: int) -> list:
#     try:
#         return items[: items.index(border) + 1]
#     except ValueError:
#         return items

"""
Медиана — это числовое значение, которое делит сортированый массив чисел на нижнюю и верхнюю половины. 
В сортированом массиве с нечётным числом элементов медиана — это число в середине массива. 
Для массива с чётным числом элементов, где нет одного элемента точно посередине, медиана — это среднее значение двух чисел, находящихся в середине массива. 
В этой задаче дан непустой массив натуральных чисел. Вам необходимо найти медиану данного массива.
"""

# def checkio(data:list) -> [int, float]:
#     data.sort()
#     index = (len(data) - 1) // 2
#     if len(data) % 2:
#         mediana = data[index]
#         return mediana
#     else:
#         mediana = (data[index] + data[index + 1]) / 2
#         return mediana

# def checkio(data):
#     data.sort()
#     half = len(data) // 2
#     return (data[half] + data[~half]) / 2

"""You have a lot of work to do, so you might want to split it into smaller pieces. This way you'll know which piece you'll do on Monday, which will be for Tuesday and so on.

Split a list into smaller lists of the same size (chunks). The last chunk can be smaller than the default chunk-size. If the list is empty, then you shouldn't have any chunks at all."""

# def chunking_by(items: list, size: int):
#     small = []
#     chunking_items = []
#     for i in items:
#         small.append(i)
#         if len(small) == size:
#             chunking_items.append(small)
#             small = []
#     if len(small):
#         chunking_items.append(small)
#     return chunking_items

# def chunking_by(items: list, size: int):
#     return [items[i:i+size] for i in range(0, len(items), size)]

"""Sort the numbers in an array. But the position of zeros should not be changed"""

# def except_zero(items: list):
#
#     zero_indexes = []
#     counter = 0
#
#     while items.count(0):
#         zero_index = items.index(0)
#         zero_indexes.append(zero_index + counter)
#         items.pop(zero_index)
#         counter += 1
#     sorted_list = sorted(items)
#
#     for indexes in zero_indexes:
#         sorted_list.insert(indexes, 0)
#
#     return sorted_list

# def except_zero(L):
#     s = iter(sorted(filter(None, L)))
#     return [x and next(s) for x in L]

"""Ваше задание - пересортировать список, расположив числа в порядке уменьшения их количества в списке. 
Если несколько чисел встречаются одинаково часто - их необходимо расположить в порядке от меньшего к большему, вне зависимости от того, в каком порядке они встречаются в исходном списке. 
Например: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]"""


# def frequency_sorting(items):
#     items.insert(0, -1)
#     sorted_list = sorted(items, key=lambda x: (-items.count(x), items.index(x), items.sort()))
#     sorted_list.remove(-1)
#     return sorted_list
#
# def frequency_sorting(numbers):
#     return sorted(sorted(numbers), key=numbers.count, reverse=True)

"""
Вам дан Массив(tuple), который состоит из integers и других массивов. И эти массивы тоже могут внутри иметь массивы.
Ваша задача узнать на сколько глубока эта структура или какая глубина вложенности этих массивов.
"""


# def how_deep(structure):
#     structure = str(structure)
#     if "(" in structure:
#         index_scobe = structure.find(")")
#         structure = structure[0:index_scobe]
#         answer = structure.count("(")
#         return answer
#     elif "[" in structure:
#         index_scobe = structure.find("]")
#         structure = structure[0:index_scobe]
#         answer = structure.count("[")
#         return answer


# def how_deep(structure):
#     structure = str(structure)
#     count = structure.count(",(")
#     print(count)
#     return 1
#
# def how_deep(x):
#     if x and isinstance(x, (list, tuple)):
#         return 1 + max(how_deep(i) for i in x)
#     return 0

# def get_depth(list_):
#     return 1 + max(get_depth(itm) for itm in list_) if type(list_) == list else 0
#
# def get_depth(l):
#     if isinstance(l, (list, tuple)):
#         t = ()
#         for itm in l:
#             t += get_depth(itm),
#         return 1 + max(t)
#     return 0

# structure = (1, 2, (3, (4, (5,))))
#
# structure = (1, (2,), (3,))
#
# structure = (((),),)
# structure = [[[],[],[]]]
#
# structure = (1, 2, (3,))
# structure = [1,[2],[2,[3]]]
# structure = (1, ((),), (3,))
# structure = (1, 2, 3)

# structure = str(structure)
# structure = structure.split(",")
# print(structure)

"""Вы современый человек, предпочитающий использовать 24-часовой формат времени. 
Но в некоторых регионах используют 12-часовой формат. 
Ваша задача - переконвертировать время из 12-часового формата в 24-часовой, используя следующие правила:
- выходной формат должен быть 'чч:мм'
- если часы меньше 10 - допишите '0' перед ними. Например: '09:05'"""
# import re
#
# def time_converter(time:str):
#     reg_exp = r"[0-9]{1,2}"
#     split_time = re.findall(reg_exp, time)
#     print(split_time)
#     if time.endswith("p.m."):
#         if int(split_time[0]) == 12:
#             result = f"{int(split_time[0])}:{split_time[1]}"
#             return result
#         result = f"{int(split_time[0]) + 12}:{split_time[1]}"
#         return result
#     elif time.endswith("a.m."):
#         if len(split_time[0]) == 1:
#             result = f"0{int(split_time[0])}:{split_time[1]}"
#             return result
#         elif int(split_time[0]) == 12:
#             result = f"00:{split_time[1]}"
#             return result
#         result = f"{int(split_time[0])}:{split_time[1]}"
#         return result
#
# def time_converter(time):
#     h, m = map(int, time[:-5].split(':'))
#     return f"{h % 12 + 12 * ('p' in time):02d}:{m:02d}"

"""A given list should be "compressed" in a way so, instead of two (or more) equal elements, staying one after another, there is only one in the result Iterable (list, tuple, iterator ...)."""

# def compress(items: list):
#     if items:
#         for index, numb in enumerate(items):
#             if index == len(items) - 1:
#                 return items
#             next_item = items[index + 1]
#             if next_item == numb:
#                 items.pop(index + 1)
#                 return compress(items)
#     else:
#         return items

"""Никола любит классифицировать все вещи. Он классифицировал ряд чисел, и в результате его усилий простая последовательность чисел стала глубоко вложенным списком. 
София и Стефан не понимают, как он организовал числа, и нужно выяснить, что всё это значит.
 Им нужна ваша помощь, чтобы понять сумасшедший список Николы.
Существует список, который содержит целые числа или другие вложенные списки, которые могут содержать ещё несколько списков и целых чисел, которые затем... ну, вы поняли. 
Вы должны поместить все целые значения в один плоский список. Порядок должен быть такой же, как и в первоначальном списке, с представлением строки слева направо.
Мы должны скрыть эту программу от Николы, сделав её маленькой и лёгкой. Поэтому ваш код должен быть короче, чем 140 символов (с пробелами) ."""

# import re
#
# def flat_list(array):
#     answer = []
#     reg_exp = r"[-+]?\d+"
#     result = re.findall(reg_exp, str(array))
#     for i in result:
#         answer.append(int(i))
#     return answer
#
# def flat_list(l):
#     r = []
#     def f(l):
#         for i in l:
#             r.append(i) if type(i) is int else f(i)
#     f(l)
#     return r