# def sum_digits(a):
#     l = []  # არ იმახსოვრებს მნიშვნელობას. შემდეგ საფეხურზე ასუფთავებს სიას....
#     if a == 0:
#         return l
#     else:
#         digit = a % 10
#         l.append(digit)
#         sum_digits(a // 10)
#     # return sum(l)


# x = int(input('enter number: '))
# y = sum_digits(x)
# print(y)
# # print(sum(*y))

def recursive(number):
    if number == 0:
        return 0
    else:
        return number % 10 + recursive(number // 10)


input_number = int(input('enter number: '))
res = recursive(input_number)
print(res)
