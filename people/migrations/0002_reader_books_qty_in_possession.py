# Generated by Django 4.1.5 on 2023-02-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='books_qty_in_possession',
            field=models.IntegerField(default=0, verbose_name='Держит книг'),
        ),
    ]