import os


def check_directory(file_name):
    FOLDER_PATH = './../parsed_data'
    FILE_PATH = os.path.join(FOLDER_PATH, file_name)

    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w', encoding='utf-8'):
            pass

    return FILE_PATH
