from django.shortcuts import render

from django.shortcuts import render, HttpResponse , redirect
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
