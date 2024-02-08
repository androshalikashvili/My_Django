def insertion(x: list)-> list:
    '''Sort list via Insertion method
    '''
    for i in range(1, len(x)):
        for j in range(i, 0, -1):
            if x[j] < x[j-1]:
                x[j], x[j-1] = x[j-1], x[j]
            else:
                break


myLyst = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
insertion(myLyst)
print(myLyst)
