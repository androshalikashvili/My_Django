num_list = [44, 23, 11, 8, 20, 56, 33, 55]

x = int(eval(input('Enter a number: ')))

if x > num_list[2] and x < num_list[-1]:
    print('More than list elements')
elif x == num_list[5]:
    print('Equal')
else:
    print('None of the conditions were met')
    