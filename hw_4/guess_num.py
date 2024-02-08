import random
from time import sleep

random_number = random.randint(1, 1000)

x = 0
n =0
print('Try guess number from 1 to 1000')
# აქ მიუთითე საიდან სადამდეა ჩაფიქრებული რიცხვი
# გამოიტანოს ინფორმაცია

while x != random_number:
    n += 1
    print()
    x = int(input(f'{n} enter number: '))
    sleep(1)
    if x == random_number:
        print('You Win')
        break
    elif x > random_number:
        print('your number is too much')
    else:
        print('Your number is low')
        
sleep(2)
print()
print('you can start again ;)')
print()
