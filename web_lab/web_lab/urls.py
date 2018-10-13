from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',  include('lab1.urls')),
    url('lab1/',  include('lab1.urls')),
    url('lab2/',  include('lab2.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
