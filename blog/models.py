from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.

class Blogpost (models.Model):
    sr_no       =models.AutoField
    title       =models.CharField(max_length=99)
    photo       =models.ImageField(upload_to='blog')
    artical     = models.TextField(null=True,blank=True)
    slug        = models.CharField(max_length=50,blank=True,null=True)
    timestamp	=models.DateTimeField(auto_now_add=True)
    img      	=models.ImageField

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering=['-timestamp']


def Product_slug_pre_save(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(Product_slug_pre_save,sender=Blogpost)