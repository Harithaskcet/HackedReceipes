from django.shortcuts import render

# Create your views here.

def foods(request):
    return render(request, 'ReceipeList.html')

def detail(request):
    return render(request,'Details.html')
