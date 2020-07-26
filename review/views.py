from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import ReviewForm
from books.models import Book
from .models import Review
from .forms import CommentForm

# Create your views here.


def index(request):
    return render(request, 'review/index.template.html')


def create_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return HttpResponse("Review is created")
        else:
            return HttpResponse("Form has error")
    else:
        form = ReviewForm()
        return render(request, "review/create_review.template.html", {
            "form": form,
            "book": book
        })


def create_comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            return HttpResponse("Comment created")
        else:
            return HttpResponse("Problem with input")
    else:
        form = CommentForm()
        return render(request, "review/create_comment.template.html", {
            "form": form,
            "review": review
        })