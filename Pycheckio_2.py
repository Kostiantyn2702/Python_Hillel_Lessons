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
