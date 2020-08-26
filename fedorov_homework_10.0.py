import json
import csv
import random

"""
Цель задания - создать функции, которые будут генерировать случайные данные нужного формата
для записи в файлы разных типов.
"""

"""
Функция 1. Создает данные для записи в файл txt.
Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы, знаки препинания.
Также необходимо обязательно использовать РОВНО 9 символов перехода на новую строку (\n) В СЕРЕДИНЕ данной строки.
"""

def create_random_data_for_txt_file():
    my_string = ""
    random_len = random.randint(100, 1000)
    random_char = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm ,.:;"
    len_random_cgar = len(random_char)
    while len(my_string) < random_len:
        if len(my_string) == random_len // 2:
            my_string += "\n" * 9
        my_string += random_char[random.randint(0, len_random_cgar - 1)]
    print(random_len, len(my_string))
    print(my_string)



create_random_data_for_txt_file()

"""
Функция 2. Создает данные для записи в файл json.
Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита.
Значения - целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1, или True/False.
"""

"""
Функция 3. Создает данные для записи в файл csv.
Создает и возвращает список длинны n внутренних списков длинны m (таблица с n строк и m столбцов).
Числа n и m выбираются случайно в диапазоне от 3 до 10.
В таблицу записывать значения или 0 или 1.
Заголовка у таблицы нет.
"""
"""
А теперь основное задание:
Написать функцию file_writer которой принимает один параметр - имя файла(вместе с путем).
В зависимости от расширения файла (txt, csv, json) сгенерировать данные для записи и записать в данный файл.
Если расширение не соответствует заданным, то вывести ошибку "Unsupported file format"
"""