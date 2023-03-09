from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',home,name='home'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('portfolio/',portfolio,name='portfolio'),
    path('price/',price,name='price'),
    path('services/',services,name='services'),
]
