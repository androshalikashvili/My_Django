import threading
import time


def find_even():
    even_numbers = [num for num in range(30, 51) if num % 2 == 0]
    print("Even numbers:", even_numbers)


def find_odd():
    odd_numbers = [num for num in range(30, 51) if num % 2 != 0]
    print("Odd numbers:", odd_numbers)


t1 = time.time()

thread1 = threading.Thread(target=find_even)
thread2 = threading.Thread(target=find_odd)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# find_even()
# find_odd()

t2 = time.time()

print(f'working time is: {t2 - t1}')
print("Programm finish working...")
