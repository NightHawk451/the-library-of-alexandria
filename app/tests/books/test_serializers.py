# app/tests/books/test_serializers.py

from books.serializers import BookSerializer


def test_valid_book_serializer():
    valid_serializer_data = {
        "title": "Raising Arizona",
        "author": "none",
        "year": "1987",
    }
    serializer = BookSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_book_serializer():
    invalid_serializer_data = {"title": "Raising Arizona", "author": "none"}
    serializer = BookSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"year": ["This field is required."]}
