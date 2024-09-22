from django.contrib import admin
from django.urls import path
from contacts.views import contacts_list, sign_in
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
