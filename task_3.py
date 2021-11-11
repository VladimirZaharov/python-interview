# Разработать генератор случайных чисел. В функцию передавать начальное и конечное
# число генерации (нуль необходимо исключить). Заполнить этими данными список и словарь.
# Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”. Вывести содержимое
# созданных списка и словаря.
from time import time, sleep

def random_generator(start_num, end_num):
    if start_num == 0 or end_num == 0:
        raise Exception('Значение не должны равняться нулю!')
    random_list = []
    random_dict = {}
    for i in range(1,11):
        sleep(0.1)
        rand_num = int(((time() - int(time()))*(end_num-start_num))+start_num)
        random_list.append(rand_num)
        random_dict[f'elem_<{i}>']= rand_num
    return random_list,random_dict
