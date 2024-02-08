x = input('Enter text: ')

bytes_text = x.encode('UTF-8')

print(bytes_text)
print()

text = bytes_text.decode('UTF-8')

print(text)
print() 
