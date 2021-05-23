from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def index(request):
#     return HttpResponse("Hello")

#render a whole HTML file
def index(request):
    return render(request, "hello/index.html") #insted of returning HTTP respond we can render a HTML Template.

# def rahat(request):
#     return HttpResponse("Hello, Rahat!")

# def david(request):
#     return HttpResponse("Hello, David!")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")

# the 3rd argument is optional information that can be provided to the template
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
