from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    fname = "Paul"
    lname = "Chor"
    return render(request, "books/index.template.html", {
        "first_name":fname,
        "last_name":lname
    })