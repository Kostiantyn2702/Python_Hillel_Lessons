def get_filename_and_path_to_folder(path: str):
    if os.path.isfile(path):
        filename = os.path.basename(path)
        path_to_folder = os.path.split(path)[0]
        return filename, path_to_folder

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

def get_filenames_list_from_folder(path="."):
    return get_dict_filenames_folders(path)["files"]

def create_empty_folder_tmp(path:str):
    folder_list = get_dict_filenames_folders(path)["folders"]
    if folder_list == []:
        os.mkdir(os.path.join(path, "tmp"))
    else:
        for object in folder_list:
            old_path_name = os.path.join(path, object)
            os.rename(old_path_name, os.path.join(path, object + "_tmp"))
