from django.db import models

# Create your models here.
class Item(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.first_name