from django import forms

from books.models import Book
from people.models import Reader


class BookModelForm(forms.ModelForm):
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

    # qty_available = forms.IntegerField()


class BookGiveOut(forms.Form):
    # book = forms.ModelChoiceField(label='Книга', queryset=Book.objects.all())
    reader = forms.ModelChoiceField(label='Читатель', queryset=Reader.objects.all())
