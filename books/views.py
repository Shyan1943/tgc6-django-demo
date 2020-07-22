from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book, Author
from .forms import BookForm, AuthorForm

# Create your views here.


def index(request):
    fname = "Paul"
    lname = "Chor"
    return render(request, "books/index.template.html", {
        "first_name": fname,
        "last_name": lname
    })


def show_books(request):
    all_books = Book.objects.all()
    return render(request, "books/all_books.template.html", {
        "books": all_books
    })


@login_required
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        form.save()
        messages.success(request, "New book has been created")
        return redirect(reverse(show_books))

    else:
        form = BookForm()
        return render(request, "books/create_book.template.html", {
            "form": form
        })

@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        form.save()
        messages.success(request, "book has been updated")
        return redirect(reverse(show_books))
    else:
        form = BookForm(instance=book)
        return render(request, "books/edit_book.template.html", {
            "form": form
        })

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        book.delete()
        messages.success(request, "Book has been deleted")
        return redirect(reverse(show_books))
    else:
        return render(request, "books/delete_book.template.html", {
            "book": book
        })


def show_authors(request):
    all_authors = Author.objects.all()
    return render(request, "books/all_authors.template.html", {
        "authors": all_authors
    })

@login_required
def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        messages.success(request, "New author has been created")
        return redirect(reverse(show_authors))
    else:
        form = AuthorForm()
        return render(request, "books/create_author.template.html", {
            "form": form
        })

@login_required
def edit_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        form.save()
        messages.success(request, "Author has been updated")
        return redirect(reverse(show_authors))

    else:
        form = AuthorForm(instance=author)
        return render(request, "books/edit_author.template.html", {
            "form": form
        })

@login_required
def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == "POST":
        author.delete()
        messages.success(request, "Author has been deleted")
        return redirect(reverse(show_authors))
    else:
        return render(request, "books/delete_author.template.html", {
            "author": author
        })
