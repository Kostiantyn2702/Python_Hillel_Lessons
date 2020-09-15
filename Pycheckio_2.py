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

