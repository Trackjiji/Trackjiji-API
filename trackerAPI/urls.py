from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^listings/(?P<filters>.*)/(?P<category>.*)/(?P<location>.*)/$', views.listings),
    url(r'^listings', views.listings),
    url(r'^categories', views.categories),
    url(r'^locations', views.locations),
    url(r'^$', views.landing),
]
