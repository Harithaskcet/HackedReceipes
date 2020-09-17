from django.shortcuts import render, get_object_or_404, redirect
from .models import Receipe
import requests
import json
import urllib.request

# Create your views here.
# remove numbers in view and list.html


def foods(request):
    receipes = Receipe.objects
    if not receipes.filter(id=42).exists():
        lists= urllib.request.urlopen('http://starlord.hackerearth.com/recipe')
        responses = json.load(lists)
        x = 2
        for response in responses:
            food = Receipe()
            food.name = response['name']
            food.image = response['image']
            food.category = response['category']
            food.label = response['label']
            food.price = response['price']
            food.description = response['description']
            food.top = x*(12)/(x-1)
            food.favourite = False
            food.ingredients = ['1/2 Maida', 'Salt to taste', '1 tspn Oil']
            food.preparation = food.getDesc()
            food.save()
            x += 1
    receipeList = Receipe.objects.all().order_by("pk")
    print(receipeList)
    return render(request, 'ReceipeList.html',{'items':receipeList, 'numbers':[1,2,3,4,5], 'categories': ['mains','appetizer','dessert','clone','weird', 'All'], 'selected': 'All' })

def detail(request, receipe_id):
    if request.method == "POST" or request.method == "GET":
        receipe_detail = get_object_or_404(Receipe, pk=receipe_id)
        return render(request,'Details.html',{ 'receipe': receipe_detail, 'numbers': [1,2,3,4,5]})

def like(request, receipe_id):
    if request.method == "POST":
        receipe = get_object_or_404(Receipe, pk=receipe_id)
        receipe.favourite =  not receipe.favourite
        receipe.save()
        return redirect('/receipe/' + str(receipe.id))

def addlike(request, receipe_id):
    if request.method == "POST":
        receipe = get_object_or_404(Receipe, pk=receipe_id)
        receipe.favourite =  not receipe.favourite
        receipe.save()
        return redirect('foods')

def category(request, name):
    lists = [] 
    receipes = Receipe.objects
    if name == 'All':
        lists = receipes
    else:
        lists = receipes.filter(category=name)
    return render(request, 'ReceipeList.html',{'items':lists, 'numbers':[1,2,3,4,5], 'categories': ['mains','appetizer','dessert','clone','weird', 'All'], 'selected': name})

def search(request, dish):
    check = dish+'%'
    lists = Receipe.objects.all().extra(where=['upper(name) LIKE upper(%s)'], params=[check])
    return render(request, 'ReceipeList.html',{'items':lists, 'numbers':[1,2,3,4,5], 'categories': ['mains','appetizer','dessert','clone','weird', 'All'], 'selected': 'All'    })
