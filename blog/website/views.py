from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_blog(request):
    lista = ["Django", "python", "Git", "Html",
             "Bando de daods",
             "linux", "Nginx"]
    
    data = {"name": "Curso de Django 3", "lista": lista}
    return render(request, 'index.html', data)