# Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке
# часть строковых значений заменить на значения типа example345 (строка+число).
# Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
# Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
# вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных
# подстрок на новое значение и вывод всех подстрок, состоящих из букв и цифр, например: example345.

from os import path
from random import randint


def print_file(some_file):
    with open(some_file, 'r', encoding='utf-8') as s:
        for line in s:
            temp_list = line.split()
            if temp_list[2] in temp_list[0]:
                print(''.join(temp_list))
def file_create():
    file_name = f'{input("Введите имя создаваемого файла: ")}.txt'
    if path.isfile(file_name):
        print('файл с таким именем уже существует')
        return file_create()
    text_list = [''.join([chr(randint(97,122)) for p in range(randint(1,10))]) for q in range(20)]
    number_list = [randint(1,100) for i in range(20)]
    mixed_list = [f'{a}{b}' if randint(1,2)==1 else a for a,b in zip(text_list,number_list)]
    with open(file_name, 'w', encoding='utf-8') as j:
        j.writelines(f'{a} - {b}\n' for a,b in zip(mixed_list, number_list))
    print_file(file_name)


file_create()
