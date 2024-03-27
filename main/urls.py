from django.contrib import admin
from django.urls import path
from .views import *
app_name = 'main'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact', contact, name='contact')
]
