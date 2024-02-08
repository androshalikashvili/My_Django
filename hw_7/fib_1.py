def fib(n):
    fib_numbers = []
    a, b = 0, 1
    for i in range(n):
        fib_numbers.append(a)
        a, b = b, a + b
    return fib_numbers


x = int(input('Please choose Integer number: '))
res = fib(x)
print(*res)
