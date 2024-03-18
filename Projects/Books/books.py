from datetime import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class BookManager:
    def __init__(self):
        self.books = []


    def append_book(self, title, author, year):
        while True:
            if not author.isalpha(): # წიგნის ავტორის შეყვანა მხოლოდ ასოების მიღებაზე შემოწმება
                print("Invalid author name. Please enter a name with only alphabetic characters.")
                author = input("Enter the correct author of the book: ")
            else:
                # წიგნის გამოშვების წლის შეყვანა-შემოწმება
                try:
                    year = int(year)
                    current_year = datetime.now().year

                    if year > current_year:
                        print("Invalid year. Publication year cannot be in the future.")
                    else:
                        new_book = Book(title, author, year)
                        self.books.append(new_book)
                        print(f'Book "{title}" added successfully')
                        break  # ცილკიდან გამოსვლა თუ სწორად შევიდა ყველა მონაცემი
                except ValueError:
                    print("Invalid year format. Please enter a valid number.")

                    # არასწორი წლის შეყვანისას ხელახლა მოითხოვს შეყვანას
                    year = input("Enter the correct year of publication of the book: ")


    def search_book_by_title(self, title):
        searched_books = [book for book in self.books if book.title.lower() == title.lower()]
        if not searched_books:
            print(f'Book title "{title}" not found')
        else:
            print('Books found with title "{title}": ')
            for book in searched_books:
                print(f"Author: {book.author}, The year of publishing: {book.year}")


    def book_full_list(self):
        if not self.books:
            print("Books list is empty")
        else:
            print("Books list:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, The year of publishing: {book.year}")


def main():
    book_manager = BookManager()

    while True:
        print("\nMenu:")
        print("1. Add new book")
        print("2. View list of all books")
        print("3. Find a book by title")
        print("4. Exit")

        choice = input("Select action (1-4):")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter the year of publication of the book: ")
            book_manager.append_book(title, author, year)

        elif choice == '2':
            book_manager.book_full_list()
        
        elif choice == '3':
            title = input("Enter the title of the book to search: ")
            book_manager.search_book_by_title(title)
        
        elif choice == '4':
            print("Exit the program. Goodbye!")
            break

        else:
            print("Incorrect choice. Please select from 1 to 4.")


if __name__ == "__main__":
    main()
