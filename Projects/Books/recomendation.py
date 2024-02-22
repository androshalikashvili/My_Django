def append_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully")


    def search_book_by_title(self, title):
        searched_books = [book for book in self.books if book.title.lower() == title.lower()]
        if not searched_books:
            print(f'Book title "{title}" not found')
        else:
            print(f'Books found with title "{title}": ')
            for book in searched_books:
                print(f"Author: {book.author}, The year of publishing: {book.year}")


    def book_full_list(self):
        if not self.books:
            print("Books list is empty")
        else:
            print("Books list:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, The year of publishing: {book.year}")