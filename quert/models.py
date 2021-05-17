from django.db import models
# Create your models here.



class Contact(models.Model):
    name        =models.CharField(max_length=120)
    email       =models.CharField(max_length=120)
    contact_no  =models.IntegerField()
    message     =models.TextField(max_length=1000)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    title        =models.CharField(max_length=120)
    subtitle     =models.CharField(max_length=120)
    photo        = models.ImageField(upload_to='photos')
    description  =models.CharField(max_length=999)
    site         =models.CharField(max_length=120)
    order_img    =models.IntegerField()
    order_text    =models.IntegerField()

    def __str__(self):
        return str(self.title)


class Price(models.Model):
    title       =models.CharField(max_length=50)
    img         =models.ImageField(upload_to='service_photos')
    img1        =models.ImageField(upload_to='service_photos/IMG1',blank=True,null=True)
    img2        =models.ImageField(upload_to='service_photos/IMG2',blank=True,null=True)
    img3        =models.ImageField(upload_to='service_photos/IMG3',blank=True,null=True)
    head        =models.CharField(max_length=50,default='This is heading')
    message     =models.TextField(max_length=1000)
    star        =models.BooleanField(blank=True,null=True,default=False)

    class Meta:
        verbose_name = 'case study'

    def __str__(self):
        return str(self.title)


class client(models.Model):
    name       =models.CharField(max_length=50)
    img        =models.ImageField(upload_to='logo')
    height     =models.IntegerField()
    width      =models.IntegerField()
    site       =models.CharField(max_length=50,default='#')


    def __str__(self):
        return str(self.name)

class testimonial(models.Model):
    img        =models.ImageField(upload_to='testimonial')
    def __str__(self):
        return str(self.img)

