from django.contrib import admin
from books.models import Book


@admin.register(Book)
class MotorcycleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'year',
    )
    fields = (
        'id',
        'title',
        'author',
        'year',
        'isbn',
    )
