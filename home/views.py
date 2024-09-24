from django.shortcuts import render, redirect
from .models import Item
from .form import FormContactItem

# Create your views here.

# def index(request):
#     """ Aview to return index page """
#     return render(request, 'home/index.html')


def index(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'home/index.html', context)


def add_contact(request):
    if request.method =='POST':
        form = FormContactItem(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    form = FormContactItem()
    context = {
        'form': form
    }
    return render(request, 'home/add_contact.html', context)