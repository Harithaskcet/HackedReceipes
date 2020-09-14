from django.contrib import admin
from django.urls import path
from Receipe.views import *
from .views import *

urlpatterns = [
   path('<int:receipe_id>', detail, name = "detail"),
] 
