from django.shortcuts import render, get_object_or_404
from .models import Receipe
# Create your views here.

def foods(request):
    return render(request, 'ReceipeList.html')

def detail(request, receipe_id):
    receipe_detail = get_object_or_404(Receipe, pk=receipe_id)
    return render(request,'Details.html',{ 'receipe': receipe_detail, 'numbers': [0,1,2,3,4]})
