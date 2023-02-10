from django.forms import ModelForm

from books.models import Book


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'ru_title',
            'orig_title',
            'price',
            'cover_image',
            'day_rate',
            'year',
            'pages',
            'genre',
            'author',
            'qty',
        ]