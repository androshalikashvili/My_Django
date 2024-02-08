import re

input_phone_number = input('Please input Phone number like "(123)456-789": ')
pattern = r'\(\d{3}\)\s\d{3}\-\d{3}'
x = re.match(pattern, input_phone_number)

if x:
    print(input_phone_number)
else:
    print('Invalid format')
