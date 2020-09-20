import pytest

from books.models import Book


@pytest.fixture(scope="function")
def add_book():
    def _add_book(title, author, year):
        book = Book.objects.create(title=title, author=author, year=year)
        return book

    return _add_book
