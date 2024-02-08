def anagram(a, b):
    if len(a) != len(b):
        return False
    else:
        a1 = sorted(a)
        b2 = sorted(b)
        return a1 == b2
    

res = anagram('abba', 'bbaa')
print(res)
