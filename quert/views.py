from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from .forms import Contactform
from .models import Contact,Product,Price
import json
# Create your views here.


class te(CreateView):
    model =Contact
    form_class = Contactform
    template_name = 'default.html'
    success_url = reverse_lazy('test')

    def get_context_data(self,*args, **kwargs):
        context = super(te, self).get_context_data(*args, **kwargs)
        context['prod'] = Product.objects.all()
        return context


class service(ListView):
    template_name = 'service.html'
    model = Price















    # def post(self, request):
    #     if request.method == "POST":
    #         clientkey = request.POST["g-recaptcha-response"]
    #         secretkey = "6LfIKM8UAAAAAF3nWuIdvtpvBFwIzwcUr4ijQ2UI"
    #         captachdata = {
    #             'secret': secretkey,
    #             'response': clientkey
    #         }
    #         r = request.POST(" https://www.google.com/recaptcha/api/siteverify METHOD: POST", data=captachdata)
    #         response = json.load(r.txt)
    #         verify = response["success "]
    #         print(verify)
    #          if verify:
    #             return HttpResponse("<script>alert('reCaptcha successfull')</script>")
    #         else:
    #             return HttpResponse("<script>alert('reCaptcha unsuccessfull')</script>")
        # form_class = Contactform()