from django.shortcuts import render, HttpResponse

# Create your views here.

def first_name(request):
    return HttpResponse("First name: Eli Hammond")