from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item

items = [
   {"id": 1, "name": "Кроссовки abibas", "brand": "abibas"},
   {"id": 2, "name": "Куртка кожаная", "brand": "puma"},
   {"id": 3, "name": "Coca-cola 1 литр", "brand": "квас"},
   {"id": 4, "name": "Картофель фри"},
   {"id": 5, "name": "Кепка"},
]

def home(request):
    context = {
        "name": "Петров",
        "email": "mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    text = """ 
                <header>
                /<a href="/"> Home</a> / <a href ='/items'> Items </a> / <a href = "/about"> About </a> /
                </header>
                <h1> "Имя: Антон "</h1> </br>
                <h1> "Отчество: Валерьевич "</h1> </br>
                <h1> "Фамилия: Проскуряков"</h1> 
                <a href='/'> Home </a> 
           """
    return HttpResponse(text)

def item_des(request,id):

    itemss = Item.objects.all()

    for item in itemss:
        if item.id == id:
            context = {
                "item": item
            }
            return render(request, "item.html", context)
    return HttpResponseNotFound(f'Item with id = {id} not found')

def get_items(request):
    itemss = Item.objects.all()
    context = {
        "items": itemss
    }
    return render(request, "items_list.html", context)
