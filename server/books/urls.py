from django.urls import path

from .views import BookDetail, BookList

urlpatterns = [
    path("api/books/", BookList.as_view()),
    path("api/books/<int:pk>/", BookDetail.as_view()),
]
