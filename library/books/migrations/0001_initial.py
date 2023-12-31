# Generated by Django 4.2.7 on 2023-11-23 08:03

import books.utils
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('author', models.CharField(max_length=150, verbose_name='Автор')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1500), books.utils.max_value_current_year], verbose_name='Год издания')),
                ('isbn', models.CharField(max_length=17, verbose_name='ISBN')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
