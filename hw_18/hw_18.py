class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y


    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.__x + other.__x, self.__y + other.__y)
        else:
            raise TypeError("Unsupported operand Type")


    def __str__(self):
        return f'({self.__x}, {self.__y})'
    

class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.__title == other.__title and self.__author == other.__author
        


#===========================

# 1 exercise
        
v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)


# 2 exercise

book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')
print(book1 == book2)  # Output: True
print(book1 == book3)  # Output: False
