from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
#GET and POST http protocol
def homepage(request):
    return render(request, "index.html", {"post": Post.objects.all})