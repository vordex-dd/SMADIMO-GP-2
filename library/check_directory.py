import os


def check_directory(file_name):
    folder_path = './../parsed_data'
    file_path = os.path.join(folder_path, file_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8'):
            pass

    return file_path
