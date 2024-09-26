from django.contrib import admin
from django.urls import path
from home.views import index, add_contact, delete_contact
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('add', views.add_contact, name='add'),
    path('edit/<item_id>', views.edit_contact, name='edit'),
    path('delete/<item_id>', views.delete_contact, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
