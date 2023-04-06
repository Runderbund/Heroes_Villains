from django.urls import path
from . import views

urlpatterns = [
    path ('/api/supers/'),
    path ('/api/supers/<int:pk>/')
]
# As a developer, I want my API to serve the “supers” app’s content on the following urls paths: 
# Paths must match these exactly! 
# ‘127.0.0.1:8000/api/supers/' - optional params 
# ‘127.0.0.1:8000/api/supers/<int:pk>/’ 