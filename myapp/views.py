from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    return render(request, "myapp\\index.html")

def item(request):
    return HttpResponse("This is an item view")