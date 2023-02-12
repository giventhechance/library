from django.urls import path

from books.views import *

app_name = 'books'

urlpatterns = [
    path('', index, name='index'),
    path('main_page/', main_page, name='main_page'),
    path('all_books/', all_books, name='all_books'),
    path('all_books/sort', all_books_sorted, name='all_books_sorted'),
    path('all_books/<int:pk>/', book_detail, name='book_detail'),
    path('all_books/<int:pk>/giveout/', give_out_book, name='give_out_book'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
]