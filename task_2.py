from os import listdir, path


def print_directory_contents(sPath):
    temp_dir = listdir(sPath)
    for i in temp_dir:
        print(f'{sPath} - {i}')
        if path.isdir(f'{sPath}\{i}'):
            print('directory')
            print_directory_contents(f'{sPath}\{i}')
