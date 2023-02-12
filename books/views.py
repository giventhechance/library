from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from books.forms import BookModelForm, BookGiveOut
from books.models import Book, Author


def index(request):
    return HttpResponse('hello')

def main_page(request):
    return render(request, 'books/main_page.html')

def all_books(request):
    books = Book.objects.all().order_by('ru_title')

    context = {
        'books': books
    }
    return render(request, 'books/book_list.html', context)

def all_books_sorted(request):
    sorting = request.POST['sort']
    print(sorting)
    clicked = 0
    if sorting:
        clicked = 1
        print(clicked)
        sorted_books = Book.objects.all().order_by('-ru_title')

        return render(request, 'books/book_list.html', {'books': sorted_books})
    else:
        return redirect('books:all_books')


    # books = Book.objects.all().order_by('ru_title')
    #
    # return render(request, 'books/book_list.html', {'books': books})
    # return HttpResponse('IT FUCKING WORKS! HOW LONG DOES IT TAKE TO MAKE A FUCKING BUTTON WORK! FUCK!!!')

    # return HttpResponse('nope')

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

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
            return redirect('books:all_books')

        else:
            print('Хаха лох')

    context = {
        'new_book': new_book
    }
    return render(request, 'books/add_book.html', context)

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        edited_book = BookModelForm(request.POST, instance=book)
        if edited_book.is_valid():
            edited_book.save()

            return redirect('books:all_books')
        else:
            context = {
                'edited_book': edited_book
            }
            return render(request, 'books/edit_book.html', context)



    else:
        edited_book = BookModelForm(instance=book)
        context = {
            'book': book,
            'edited_book': edited_book
        }
    return render(request, 'books/edit_book.html', context)

def give_out_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    giveout_form = BookGiveOut()

    if request.method == 'POST':
        book = request.POST.get('book')
        reader = request.POST.get('reader')
        print(book, reader)

    context = {
        'book': book,
        'giveout_form': giveout_form
    }
    return render(request, 'books/book_giveout.html', context)




