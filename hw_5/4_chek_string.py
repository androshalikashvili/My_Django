x = input(' Please Input text: ')

count_digits = 0

if x.isalnum():
    for i in x:
        if i.isdigit():
            count_digits += 1

if count_digits != 1:
    print('This String dont validate!')

else:
    print('That is fine!!! your string is VALIDATE!')

print()