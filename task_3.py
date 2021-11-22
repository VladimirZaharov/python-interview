import itertools

a = [1,2,3,4,5,6,7,8,9,10]
b = ['a','b','c','d','e','f','g','h','i','j']

def make_dict(first_list, second_list):
    new_dict = {}
    if len(first_list)<len(second_list):
        temp_list = second_list[:len(first_list )]
    else:
        temp_list = second_list
    for i,j in itertools.zip_longest(first_list,temp_list):
        new_dict[i] = j
    return new_dict

print(make_dict(a,b))