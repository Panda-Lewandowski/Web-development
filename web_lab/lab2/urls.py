from django.conf.urls import url
from . import views
from django.conf.urls import include


urlpatterns = [
    url(r'^$',  views.index),
    url(r'lab1/',  include('lab1.urls')),
]