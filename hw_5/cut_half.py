x = input('please input text: ')
# full = len(x)
# half = full // 2
# y = x[:half] 

x2 = []

for i in x[:len(x) // 2]:
   x2.append(i)

print(''.join(x2))

# print(y)
