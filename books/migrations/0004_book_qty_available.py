# Generated by Django 4.1.5 on 2023-02-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_author_surname_alter_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='qty_available',
            field=models.IntegerField(default=1, verbose_name='Доступное количество'),
        ),
    ]