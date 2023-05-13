from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/supers/', include('supers.urls')), # Allows relative paths in supers/urls.py
]