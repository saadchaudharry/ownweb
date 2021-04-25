"""owneb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quert.views import te,service,contact_us,sof,wev,data,erp,pri
from blog.views import Bloglist,Blogdetail
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',te.as_view(),name='test'),
    path('contact/',contact_us.as_view(),name='contact_us'),
    path('services/',service.as_view(),name='service'),
    path('sof/',sof.as_view(),name='sof'),
    path('wev/',wev.as_view(),name='wev'),
    path('data/',data.as_view(),name='data'),
    path('erp/',erp.as_view(),name='erp'),
    path('privacy/',pri.as_view(),name='pri'),
#     blog
    path('blog/list', Bloglist.as_view(), name='Bloglist'),
    path('events/<slug:slug>/', Blogdetail.as_view(), name="homedeatail"),

]

if settings.DEBUG:
    urlpatterns = urlpatterns +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)