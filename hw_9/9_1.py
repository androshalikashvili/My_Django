def zip_list(arr1, arr2):
    paired_list = list(zip(arr1, arr2))
    return paired_list


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = zip_list(list1, list2)
print(result)
