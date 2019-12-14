from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import CreateView
from .forms import Contactform
from .models import Contact
# Create your views here.


class te(CreateView):
    model =Contact
    # form_class = Contactform()
    form_class = Contactform
    template_name = 'default.html'
    success_url = reverse_lazy('test')