def bubble(x: list)-> list:
    '''Sort list via Bubble method
    '''
    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j +1] = x[j + 1], x[j]


myLyst = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
bubble(myLyst)
print(myLyst)
