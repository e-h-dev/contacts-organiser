from django.shortcuts import render

# Create your views here.

def log_in(request):
    return render(request, 'contacts/login.html')

def contacts_list(request):
    return render(request, 'contacts/contacts_list.html')

