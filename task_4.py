from os import path
from random import randint


def print_file(some_file):
    with open(some_file, 'r', encoding='utf-8') as s:
        for line in s:
            print(line,end='')
def file_create():
    file_name = f'{input("Введите имя создаваемого файла: ")}.txt'
    if path.isfile(file_name):
        print('файл с таким именем уже существует')
        return file_create()
    text_list = [''.join([chr(randint(97,122)) for p in range(randint(1,10))]) for q in range(20)]
    number_list = [randint(1,100) for i in range(20)]
    with open(file_name, 'w', encoding='utf-8') as j:
        j.writelines(f'{a} - {b}\n' for a,b in zip(text_list, number_list))
    print_file(file_name)


file_create()
