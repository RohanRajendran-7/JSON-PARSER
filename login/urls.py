from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from login import views
from django.views.generic import RedirectView
urlpatterns = [
    path('register/',views.register, name="register"),
    path('',views.home,name="home"),
    path('home/', RedirectView.as_view(pattern_name='home', permanent=False)),
    path('data/',views.data, name="displaydata"),
]
