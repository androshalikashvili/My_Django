def same(arr, ending):
    try:
        filtered_list = list(filter(lambda x: x.endswith(ending), arr))
        return filtered_list
    except TypeError as e:
        return f'Error: {e}'
    except AttributeError as f:
        return f'Error: {f}'
    


params = ['hello', 'world', 'coding', 'nod']
ending_check = 'ing'

result = same(params, ending_check)
print(result)
