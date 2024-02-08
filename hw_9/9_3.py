def odds(arr):
    a = list(filter(lambda x: x % 2 != 0, arr))
    return a


arr1 = [1, 2, 3, 4, 5, 6, 7]
result = odds(arr1)
print(result)
