from django.contrib import admin
from django.urls import path, include
from galeria.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
]
