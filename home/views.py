from django.shortcuts import render, redirect, get_object_or_404
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


def edit_contact(request, item_id):
    contact = get_object_or_404(Item, id=item_id)
    if request.method =='POST':
        form = FormContactItem(request.POST, instance=contact)
        if form.is_valid():
            form.save()
        return redirect('home')
    form = FormContactItem(instance=contact)
    context = {
        'form': form
    }
    return render(request, 'home/edit_contact.html', context)



def delete_contact(request, item_id):
    contact = get_object_or_404(Item, id=item_id)
    contact.delete()
    return redirect('home')