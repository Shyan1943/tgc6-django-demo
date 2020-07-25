from django.contrib import admin
from django.urls import path, include
import books.views


urlpatterns = [
    path('', books.views.index),
    path('all', books.views.show_books, name="all_books_route"),
    path('create', books.views.create_book),
    path('update/<book_id>', books.views.edit_book, name='update_book_route'),
    path('delete/<book_id>', books.views.delete_book, name='delete_book_route'),
    path('authors', books.views.show_authors, name="all_authors_route"),
    path('authors/create', books.views.create_author),
    path('authors/<author_id>', books.views.edit_author, name="update_author_route"),
    path('authors/delete/<author_id>', books.views.delete_author, name="delete_author_route"),
]
