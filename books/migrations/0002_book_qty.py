# Generated by Django 4.1.5 on 2023-02-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='qty',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
    ]
