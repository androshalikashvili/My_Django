def adlist(a: int):
    # global int_list
    int_list.append(a)
    # return int_list


int_list=[10, 20, 30, 40]
x = int(input('which number add list: '))
adlist(x)
print(int_list)
