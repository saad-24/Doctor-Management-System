from . import views
from django.urls import path

#defining the url that will use the index function from views.py file

urlpatterns= [
    path('', views.index),
]