from django.http import HttpResponse
from django.shortcuts import render

from books.forms import BookModelForm
from books.models import Book, Author


def index(request):
    return HttpResponse('hello')

def main_page(request):
    return render(request, 'books/main_page.html')

def all_books(request):
    books = Book.objects.all()

    context = {
        'books': books
    }
    return render(request, 'books/all_books.html', context)
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)

    context = {
        'book': book
    }

    return render(request, 'books/book_detail.html', context)

def add_book(request):
    new_book = BookModelForm()
    if request.method == 'POST':
        new_book = BookModelForm(request.POST)
        if new_book.is_valid():
            new_book.save()

        else:
            print('Хаха лох')

    context = {
        'new_book': new_book
    }
    return render(request, 'books/add_book.html', context)