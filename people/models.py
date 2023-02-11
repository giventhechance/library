from django.db import models

class Reader(models.Model):
    surname = models.CharField('Фамилия читателя', max_length=128)
    name = models.CharField('Имя читателя', max_length=128)
    patronymic = models.CharField('Отчество', max_length=128, blank=True, null=True)
    passport_number = models.CharField('Номер паспорта', max_length=128, blank=True, null=True, unique=True)
    birth_date = models.DateField('Год рождения')
    email = models.EmailField('E-mail', unique=True)
    address = models.CharField('Адрес', max_length=256)

    def __str__(self):
        return f'{self.name} {self.surname}'