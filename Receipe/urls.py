from django.contrib import admin
from django.urls import path
from Receipe.views import *
from .views import *

urlpatterns = [
   path('<int:receipe_id>', detail, name = "detail"),
   path('<int:receipe_id>/like', like, name="like"),
   path('<str:name>', category, name="category"),
] 
