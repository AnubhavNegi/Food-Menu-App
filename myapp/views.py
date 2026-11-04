from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.

def index(request):
    # Getting items from the database
    item_list = Item.objects.all()
    # Creating context
    context = {
        'item_list' : item_list
    }
    # Passing the context object to the render method along with the template
    return render(request, "myapp\\index.html", context)

def detail(request, id):
    item = Item.objects.get(id = id)
    context = {
        'item' : item
    }
    return render(request, 'myapp\\detail.html', context)

def create_item(request):
    form = ItemForm()
    context = {
        'form' : form
    }
    return render(request, 'myapp\\item-form.html',context)