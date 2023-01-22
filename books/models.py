from django.db import models

class Book(models.Model):
    ru_title = models.CharField('Название', max_length=255, unique=True)
    orig_title = models.CharField('Название (оригинал)', max_length=255, null=True, blank=True)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)
    cover_image = models.ImageField('Обложка', upload_to='media/books', null=True, blank=True)
    day_rate = models.DecimalField('Цена за день', max_digits=8, decimal_places=2)
    year = models.IntegerField('Год издания')
    registered = models.DateTimeField(auto_now_add=True)
    pages = models.IntegerField('Страниц')

    genre = models.ManyToManyField('Genre', verbose_name='Жанры')
    author = models.ManyToManyField('Author', verbose_name='Автор(ы)')

    def __str__(self):
        return self.ru_title

class Genre(models.Model):
    name = models.CharField('Жанр', max_length=254)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField('Имя', max_length=128)
    surname = models.CharField('Фамилия', max_length=128)
    image = models.ImageField('media/authors')

    def __str__(self):
        return f'{self.name} {self.surname}'
