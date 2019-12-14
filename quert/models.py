from django.db import models

# Create your models here.

class Contact(models.Model):
    name        =models.CharField(max_length=120)
    email       =models.CharField(max_length=120)
    contact_no  =models.CharField(max_length=120)
    message     =models.TextField(max_length=120)

    def __str__(self):
        return str(self.name)