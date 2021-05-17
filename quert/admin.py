from django.contrib import admin
from .models import Contact
from .models import Product,Price,client,testimonial,documentt
# Register your models here.

admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Price)
admin.site.register(client)
admin.site.register(testimonial)
admin.site.register(documentt)
