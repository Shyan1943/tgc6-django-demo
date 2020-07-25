from django.shortcuts import render, HttpResponse
from .forms import ReviewForm

# Create your views here.
def index(request):
    return render(request, 'review/index.template.html')

def create_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("Review is created")
        else:
            return HttpResponse("Form has error")
    else:        
        form = ReviewForm()
        return render(request, "review/create_review.template.html", {
            "form": form
        })