def sum_list(*args):
    s = 0
    for i in args:
        s += i
    return s


def summing(arr: list) -> int:
    return sum(arr)


x = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

z = sum_list(*x)
y = summing(x)
print(z)
print(y)

