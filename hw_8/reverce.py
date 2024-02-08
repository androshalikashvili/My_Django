def reverce(a:str)->str:
    if len(a) == 0:
        return ""
    else:
        return a[-1] + reverce(a[:-1])


x = input('Input a word: ')
res = reverce(x)
print(res)
