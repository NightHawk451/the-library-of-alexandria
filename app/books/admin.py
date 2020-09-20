from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "author",
        "year",
        "created_date",
        "updated_date",
    )
    list_display = (
        "title",
        "author",
        "year",
        "created_date",
        "updated_date",
    )
    readonly_fields = (
        "created_date",
        "updated_date",
    )
