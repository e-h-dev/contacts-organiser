from django.contrib import admin
from django.urls import path
from home.views import index, add_contact
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add', views.add_contact, name='add'),
]
