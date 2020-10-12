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
