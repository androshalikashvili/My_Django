from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Book
# from django.http

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}

    return render(request, "books/all_books.html", context)


def create_book(request):
    if request.method == "POST":
        # csrr_token

        title = request.POST['title']
        authors = request.POST['authors']
        publication_date = request.POST['publication_date']
        isbn = request.POST['isbn']

        new_book = Book(
            title=title,
            authors=authors,
            publication_date=publication_date,
            isbn=isbn
        )

        new_book.save()

        context = {'text': "Book Created Succssesfully"}

        return render(request, 'books/create_book.html', context)
    
    return render(request, 'books/create_book.html')


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {'book': book}

    return render(request, 'books/book_detail.html', context)


def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.authors = request.POST['authors']
        book.publication_date = request.POST['publication_date']
        book.isbn = request.POST['isbn']

        book.save()

        return redirect('book_detail', book_id=book.id)
    
    context = {'book': book}
    return render(request, 'books/update_book.html', context)


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')
    
    context = {'book': book}
    return render(request, 'books/delete_book.html', context)