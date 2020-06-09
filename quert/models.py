from django.db import models

# Create your models here.

class Contact(models.Model):
    name        =models.CharField(max_length=120)
    email       =models.CharField(max_length=120)
    contact_no  =models.IntegerField()
    message     =models.TextField(max_length=120)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    title        =models.CharField(max_length=120)
    subtitle     =models.CharField(max_length=120)
    photo        = models.ImageField(upload_to='photos')
    description  =models.CharField(max_length=120)
    site         =models.CharField(max_length=120)
    order_img    =models.IntegerField()
    order_text    =models.IntegerField()

    def __str__(self):
        return str(self.title)


class Price(models.Model):
    title       =models.CharField(max_length=50)
    price       =models.IntegerField()
    list        =models.CharField(max_length=120,null=True,blank=True)
    list2        =models.CharField(max_length=120,null=True,blank=True)
    list3        =models.CharField(max_length=120,null=True,blank=True)
    list4        =models.CharField(max_length=120,null=True,blank=True)
    list5       =models.CharField(max_length=120,null=True,blank=True)

    def __str__(self):
        return str(self.title)