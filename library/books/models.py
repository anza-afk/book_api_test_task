from django.db import models
from django.core.validators import MinValueValidator

from books.utils import max_value_current_year


class Book(models.Model):
    title = models.CharField(
        'Название',
        max_length=150
    )
    author = models.CharField(
        'Автор',
        max_length=150
    )
    year = models.IntegerField(
        'Год издания',
        validators=[
            MinValueValidator(1500),
            max_value_current_year
        ]
    )
    isbn = models.CharField(
        'ISBN',
        max_length=17
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self) -> str:
        return ' ,'.join(self.title, self.author, self.year)
