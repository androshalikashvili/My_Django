import functools

def multiply(num):
    try:
        result = functools.reduce(lambda x, y: x * y, num)
        return result
    except TypeError:
        return 'Error: Invalid data type. Exepted a list of numbers.'
    

arr = [1, 2, 3, 4, 5, 6]
sum_of_arr = multiply(arr)
print(sum_of_arr)
