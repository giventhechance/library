# Generated by Django 4.1.5 on 2023-02-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='surname',
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Имя и фамилия'),
        ),
    ]
