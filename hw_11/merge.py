


def merge_2_list(a: list, b: list)-> list:
    '''merge two sorted list'''
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    elif j < len(b):
        c +=b[j:]
    return c


def merge_sort(x: list)-> list:
    '''sort list via Merge method
    '''
    if len(x) == 1:
        return x
    middle = len(x) // 2
    right = merge_sort(x[middle:])
    left = merge_sort(x[:middle])
    return merge_2_list(left, right)


myLyst = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
print(merge_sort(myLyst))
