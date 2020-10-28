"""Функция должна распознавать является ли тема письма стрессовой.
Стрессовая тема определяется тем, что все буквы в верхнем регистре,
и / или заканчиваются как минимум тремя восклицательными знаками,
и / или содержат по крайней мере одно из следующих слов-маркеров: "help", "asap", "urgent".
Любое из этих слов-маркеров может быть написано по-разному: «HELP», «help», «HeLp», «H! E! L! P!», «H-E-L-P»,
и даже очень непринужденно «HHHEEEEEEEEELLP»."""

# def is_string_upper(subj:str):
#     if subj.isupper():
#         return True
#     else:
#         return False
#
# def is_string_endwith(subj:str):
#     if subj.endswith("!!!"):
#         return True
#     else:
#         return False
#
# def is_stressful_words_in_text(subj:str):
#     subj = subj.lower()
#     stressful_words = ["help", "asap", "urgent"]
#     for word in stressful_words:
#         if word in subj:
#             return True
#     return False
#
# def processig_words(subj:str):
#     list_subj = subj.split(" ")
#     for stresword in list_subj:
#         new_subj = ""
#         for symb in stresword:
#             if symb.isalpha():
#                 new_subj += symb
#         subj = new_subj
#         if is_stressful_words_in_text(subj):
#             return True
#
# def remove_sticking_symbols(subj:str):
#     list_subj = subj.split(" ")
#     for stresword in list_subj:
#         new_subj = ""
#         for index, symb in enumerate(stresword):
#             if index == len(stresword) - 1:
#                 new_subj += symb
#             elif stresword[index + 1] == symb:
#                 continue
#             else:
#                 new_subj += symb
#         subj = new_subj
#         if is_stressful_words_in_text(subj):
#             return True
#     return False
#
# def is_stressful(subj:str):
#     if is_string_upper(subj):
#         return True
#     elif is_string_endwith(subj):
#         return True
#     elif is_stressful_words_in_text(subj):
#         return True
#     elif processig_words(subj):
#         return True
#     elif remove_sticking_symbols(subj):
#         return True
#     return False
#
#
# import re
#
# def is_stressful(subj):
#     return (subj.isupper() or
#             subj.endswith('!!!') or
#             any(re.search('+[.!-]*'.join(c for c in word), subj.lower())
#                 for word in ['help', 'asap', 'urgent']))

"""
Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).
"""

# def checkio(number: int) -> int:
#     answer = 1
#     for num in str(number):
#         if num != "0":
#             answer *= int(num)
#     return answer

"""
In this mission you need to create a password verification function.
Those are the verification conditions:
the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
a string should not contain the word "password" in any case;
should contain 3 different letters (or digits) even if it is longer than 10
"""

# def is_acceptable_password(password: str) -> bool:
#     is_digit = "1234567890"
#     if len(password) <= 6:
#         return False
#     if "password" in password or "PASSWORD" in password:
#         return False
#     if len(set(password)) < 3:
#         return False
#     if len(password) > 9:
#         return True
#     if password.isdigit():
#         return False
#     for digits in is_digit:
#         if digits in password:
#             return True
#     return False

"""Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return False."""

# def is_all_upper(text: str) -> bool:
#     return True if text.isupper() else False

"""Determine whether the sequence of elements items is ascending so that its each element is strictly larger than (and not merely equal to) the element that precedes it."""

# def is_ascending(items) -> bool:
#     empty_list = [-1000000]
#     index = 0
#     if len(set(items)) == 1 and len(items) > 1:
#         return False
#     for item in items:
#         if item < empty_list[index]:
#             return False
#         index += 1
#         empty_list.append(item)
#     return True

# def is_ascending(items) -> bool:
#     return all(items[i] < items[i+1] for i in range(len(items)-1))

