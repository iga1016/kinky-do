from django.http.response import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return render(request, "temp.html")
    #return HttpResponse("<h1>HelloWorld</h1>")
