from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Book, Author
from .forms import BookForm, AuthorForm

# Create your views here.

def index(request):
    fname = "Paul"
    lname = "Chor"
    return render(request, "books/index.template.html", {
        "first_name":fname,
        "last_name":lname
    })

def show_books(request):
    all_books = Book.objects.all()
    return render(request, "books/all_books.template.html",{
        "books": all_books
    })

def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        form.save()
        return redirect(reverse(show_books))

    else:
        form = BookForm()
        return render(request, "books/create_book.template.html", {
            "form": form
        })


def show_authors(request):
    all_authors = Author.objects.all()
    return render(request, "books/all_authors.template.html",{
        "authors": all_authors
    })


def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return redirect(reverse(show_authors))
    else:
        form = AuthorForm()
        return render(request, "books/create_author.template.html", {
            "form": form
        })
    