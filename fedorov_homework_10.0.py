import json
import csv
import random
import string

# Не знаю оставлять ли условия задачи или нет. С одной стороны без лишнего текста лучше, а с другой удобно когда условия под рукой (для проверки).

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

# Первая задача была тяжкой, поэтому на выходе вышла химера. Но все условия выполняет.        Вроде....

def get_index_in_random_len_range(random_len_string:int) -> list:
    """
    Функция которая генерирует номера позиций(индексы) в заданом случайном интервале.
    :param random_len_string: лучайная длина строкиС
    :return: Список индексов
    """
    index_in_random_len_range = []
    for i in range(random_len_string):
        index_in_random_len_range.append(i)
    return index_in_random_len_range

def get_index_in_random_len_without_first_and_last_positions(random_len_string:int) -> list:
    """
    Функция которая отбрасывает первый и последний индекс. На занятии условились чтобы переносов небыло в начале и конце.
    :param random_len_string: Cлучайная длина строки(пробрасываю через все функции, не уверен реализовал как надо)
    :return: Список индексов без первого и последнего элемента
    """
    index_in_random_len_without_first_and_last_positions = get_index_in_random_len_range(random_len_string)
    index_in_random_len_without_first_and_last_positions.pop(0)
    index_in_random_len_without_first_and_last_positions.pop(-1)
    return index_in_random_len_without_first_and_last_positions

def get_nine_random_carryover_positions(random_len_string:int) -> list:
    """
    Функция которая выдергивает из get_index_in_random_len_without_first_and_last_positions случайные позиции.
    Пытался сделать читабельнее, по сравнению с тем что было в начале уже лучше.
    :param random_len_string: Cлучайная длина строки(пробрасываю через все функции, не уверен реализовал как надо)
    :return: Список из 9 элементов которые обозначают места на которых будут происходить переносы строки.
    """
    len_index_list = len(get_index_in_random_len_without_first_and_last_positions(random_len_string)) # Длина большого списка для переносов
    last_index_in_index_in_index_list = len_index_list - 1 # Последний индекс большого списка для переносов
    positions_list = get_index_in_random_len_without_first_and_last_positions(random_len_string) # Большой список с позициями в заданом случайном диапазоне без первого и последнего элемента
    nine_carryover_positions = [] # Список с случайными позициями для переноса (9 штук)
    while len(nine_carryover_positions) != 9: # Набираем 9 штук.
        random_index = random.randint(0, last_index_in_index_in_index_list) # Случайный индекс
        random_position = positions_list[random_index] # Из большого списка наугад выбираем позицию в заданом диапазоне
        if random_position not in nine_carryover_positions: # Если такого элемента там нет, то записываем.
            nine_carryover_positions.append(random_position)
    return nine_carryover_positions

def create_random_data_for_txt_file(random_len_string=random.randint(100, 1000)) -> str:
    """
    Функция которая создает случайную строку для записи в txt файл.
    :param random_len_string: Cлучайная длина строки(пробрасываю через все функции, не уверен реализовал как надо)
    :return: Строку с переносами
    """
    nine_random_carryover_positions = get_nine_random_carryover_positions(random_len_string) # Наши 9 случайных позиций где нужно сделать перенос
    if len(nine_random_carryover_positions) == 9: # Проверка на случай если что-то пойдет не так и количество переносов будет меньше или больше 9. Это больше было нужно для проверки работы. Но пусть будет.
        my_string = ""
        random_char = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm ,.:;" # Хотел использовать модуль Стринг, но не хотел грузить файл. Двоеточие вроде ж тоже знак препинания(я надеюсь)
        len_random_char = len(random_char) # Выбираем наугад любой символ
        while len(my_string) != random_len_string: # Пока строка не будет заданой длины, то записываем в нее символы
            for position in nine_random_carryover_positions: # Проходим по списку позиций для переноса
                if len(my_string) == position: # Немного моей странной логики. Если в списке из 9 значений будет значение 0, то перенос должен произойти в начале строки. Также для последнего элемента.
                    my_string += "\n"          # От них я избавился в функции get_index_in_random_len_without_first_and_last_positions (наверно можно было и по другому) и тут они не выскочат.
                elif len(my_string) == position + 1: # Это на случай когда два символа переноса идут подряд. Чтобы никто не потерялся
                    my_string += "\n"
            my_string += random_char[random.randint(0, len_random_char - 1)]
        # print("Количество переносов", my_string.count("\n"))
        # print(len(my_string), random_len_string)
        return my_string

"""
Функция 2. Создает данные для записи в файл json.
Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита.
Значения - целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1, или True/False.
"""

def create_random_key() -> str:
    key = ""
    lower_chars = string.ascii_lowercase
    lower_chars_index = len(lower_chars)-1
    while len(key) != 5:
        key += lower_chars[random.randint(0, lower_chars_index)]
    return key

def create_random_value() -> int:
    """Остановил свой выбор на целых числах"""
    value = random.randint(-100, 100)
    return value

def create_random_data_for_json_file() -> dict:
    data = {}
    random_len_key = random.randint(5, 20)
    while len(data) != random_len_key:
        data[create_random_key()] = create_random_value()
    return data


"""
Функция 3. Создает данные для записи в файл csv.
Создает и возвращает список длинны n внутренних списков длинны m (таблица с n строк и m столбцов).
Числа n и m выбираются случайно в диапазоне от 3 до 10.
В таблицу записывать значения или 0 или 1.
Заголовка у таблицы нет.
"""

def create_random_m_list(random_len_data_m = random.randint(3, 10)) -> list:
    """По умолчанию поставил одинаковое рандомное число, чтобы было ровное количство столбцов. Чтобы таблица не была кривой и все такое."""
    data_m = []
    while len(data_m) != random_len_data_m:
        data_m.append(random.randint(0, 1))
    return data_m

def create_random_data_for_csv_file() -> list:
    data_n = []
    random_len_data_n = random.randint(3, 10)
    while len(data_n) != random_len_data_n:
        data_n.append(create_random_m_list())
    return data_n

"""
А теперь основное задание:
Написать функцию file_writer которой принимает один параметр - имя файла(вместе с путем).
В зависимости от расширения файла (txt, csv, json) сгенерировать данные для записи и записать в данный файл.
Если расширение не соответствует заданным, то вывести ошибку "Unsupported file format"
"""

def write_file_in_txt(filename_with_path):
    with open(filename_with_path, 'w') as txt_file:
        txt_file.write(create_random_data_for_txt_file())

def write_file_in_json(filename_with_path):
    with open(filename_with_path, 'w') as json_file:
        json.dump(create_random_data_for_json_file(), json_file)

def write_file_in_csv(filename_with_path):
    with open(filename_with_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(create_random_data_for_csv_file())

def file_writer(filename_with_path):
    if filename_with_path.endswith(".txt"):
        write_file_in_txt(filename_with_path)
    elif filename_with_path.endswith(".json"):
        write_file_in_json(filename_with_path)
    elif filename_with_path.endswith(".csv"):
        write_file_in_csv(filename_with_path)
    else:
        raise Exception("Unsupported file format!")

file_writer("./testdir/1.txt")
file_writer("./testdir/1.json")
file_writer("./testdir/1.csv")
# file_writer("./testdir/1.jpeg")
