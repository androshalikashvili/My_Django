x = input("please enter text: ")

x1 = ' '.join(x.strip().split())

x2 = x1.lower() + " Python"

if 'python' in x2:
    x2 = x2.replace('python', 'Python')

print(x2)
 