from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Page app women")

def categories(request, catid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Articles by categories</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home',permanent=True)

    return HttpResponse(f"<h1>Articles by years</h1><p>{year}</p>")

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')