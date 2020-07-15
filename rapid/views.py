from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "rapid/index.html")


def about(request):
    return render(request, "rapid/about.html")


def blog(request):
    return render(request, "rapid/blog.html")


def blog_single(request):
    return render(request, "rapid/blog-single.html")


def hosting(request):
    return render(request, "rapid/hosting.html")


def contact(request):
    return render(request, "rapid/contact.html")


def domain(request):
    return render(request, "rapid/domain.html")
