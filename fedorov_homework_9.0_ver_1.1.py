import os

"""
Написать функции (и дать им названия, отражающие то, что они делают) со следующим функционалом:

1) функции передаем полный путь к файлу в виде строки в формате "./path/to/file/filename.ext",
где точка означает текущую директорию.
(Это универсальный способ задать путь. Пользователи виндовс можете почитать это:
https://stackoverflow.com/questions/2953834/windows-path-in-python)
Функция возвращает два параметра: название файла и путь к папке.
Пример использования:
filename, folder_path = first_function(path)

2) функции передаем полный путь к папке в виде строки в формате "./path/to/folder",
где точка означает текущую директорию.
Функция возвращает список ФАЙЛОВ из этой папки. Т.к. listdir возвращает файлы и подпапки,
то такой функционал иногда нужен.
Напомню, что есть метод os.path.isfile(path) который возвращает True, если path указывает на файл.
И обратите внимание на "Щелчек Таноса" из классной работы. Мы там склеиваем путь с помощью os.path.join()
Пример использования:
files = second_function(path)
Значение по умолчанию - текущая папка. Т.е. second_function() вернет файлы из текущей папки.

3) функции передаем полный путь к папке в виде строки в формате "./path/to/folder",
где точка означает текущую директорию.
Функция возвращает СЛОВАРЬ в формате: {"files": [список ФАЙЛОВ из папки], "folders": [список ПОДПАПОК из папки]}.
Пример использования:
path_dict = third_function(path)
Значение по умолчанию - текущая папка. Т.е. third_function() вернет словарь с файлами и подпапками из текущей папки.

4) функции передаем полный путь к папке в виде строки в формате "./path/to/folder",
где точка означает текущую директорию.
Функция создает пустые папки в данной директории по следующему правилу:
- если в этой директории нет подпапок - создает папку 'tmp'
- если в этой директории есть подпапки - создает папки в названии которых дописываем '_tmp'.
Пример. Есть подпапка 'test'. значит создаем 'test_tmp'

P.S. Данные функции никак не обрабатывают ошибки существования файлов.
Т.е. если пользователь передаст путь к несуществующему файлу или папке - он получит ошибку пайтона."""

# Без обработки как написано выше.

def get_filename_and_path_to_folder(path: str):
    if os.path.isfile(path):
        filename = os.path.basename(path)
        path_to_folder = os.path.split(path)[0]
        return filename, path_to_folder

# print(get_filename_and_path_to_folder("./testdir/testdir2/Empty.txt"))

def get_dict_filenames_folders(path="."):
    folder_list = []
    file_list = []
    filenames_and_folder_list = os.listdir(path)
    for object in filenames_and_folder_list:
        object_is_file = os.path.isfile(os.path.join(path, object))
        if object_is_file:
            file_list.append(object)
        elif not object_is_file:
            folder_list.append(object)
    filenames_and_folders_dict = {"files": file_list, "folders": folder_list}
    return filenames_and_folders_dict

# print(get_dict_filenames_folders("./testdir"))

def get_filenames_list_from_folder(path="."):
    return get_dict_filenames_folders(path)["files"]

# print(get_filenames_list_from_folder("./testdir"))

def create_empty_folder_tmp(path:str):
    folder_list = get_dict_filenames_folders(path)["folders"]
    if folder_list == []:
        os.mkdir(os.path.join(path, "tmp"))
    else:
        for object in folder_list:
            old_path_name = os.path.join(path, object)
            os.rename(old_path_name, os.path.join(path, object + "_tmp"))

# create_empty_folder_tmp("./testdir/testdir2")
