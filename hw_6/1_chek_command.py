arr = []

while True:
    print(arr)
    x = input('Please input comand"a-append, r-remove, e-exit"{command} {number}: ')
    comand_split = x.split()
    if comand_split[0] == 'e':
        break
    elif comand_split[0] == 'a':
        arr.append(comand_split[1])
        print(arr)
        continue
    elif comand_split[0] == 'r':
        arr.pop()
        continue
