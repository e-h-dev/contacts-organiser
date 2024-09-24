from django.db import models

# Create your models here.
class Contacts(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    phone = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    email = models.EmailField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name