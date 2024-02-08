my_list = [43, '22', 12, 66, 210, ["hi"]]

print(my_list.index(210)) #a

my_list.insert(len(my_list), 'hello') #b

my_list.pop(2) #c
print(my_list)

my_list_2 = my_list.copy() #d
my_list_2.clear()
print(my_list)
print(my_list_2)
