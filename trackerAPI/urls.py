from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^categories', views.categories),
    url(r'^listings', views.listings),
    url(r'^locations', views.locations),
    url(r'^$', views.landing),
]
