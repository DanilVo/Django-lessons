from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *

menu = ["about site", "Add Paragraph", "Feed Back", "enter"]

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html',{'posts': posts, 'menu': menu, 'title':'Main Page'})

def about(request):
    return render(request, 'women/about.html',{'menu': menu, 'title':'Abour Site'})

# def categories(request, catid):
#     if(request.GET):
#         print(request.GET)
#     return HttpResponse(f"<h1>Articles by categories</h1><p>{catid}</p>")

# def archive(request, year):
#     if int(year) > 2020:
#         return redirect('home',permanent=True)

#     return HttpResponse(f"<h1>Articles by years</h1><p>{year}</p>")

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Page Not Found, Search again</h1>')