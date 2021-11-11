def mult_table(a,b):
    for i in range(1,a+1):
        temp_list=[]
        for j in range(1,b+1):
            temp_list.append(str(i*j))
        temp_str = (lambda n: '\t'.join(n))(temp_list)
        print(temp_str)
