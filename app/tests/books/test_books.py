import pytest

from books.models import Book


@pytest.mark.django_db
def test_book_model():
    book = Book(title="Elantris", author="Brandon Sanderson", year="2005")
    book.save()
    assert book.title == "Elantris"
    assert book.author == "Brandon Sanderson"
    assert book.year == "2005"
    assert book.created_date
    assert book.updated_date
    assert str(book) == book.title
