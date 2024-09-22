from django.shortcuts import render

# Create your views here.

def sign_in(request):
    return render(request, 'contacts/sign_in.html')

def contacts_list(request):
    return render(request, 'contacts/contacts_list.html')

