from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

items = [
   {"id": 1, "name": "Кроссовки abibas"},
   {"id": 2, "name": "Куртка кожаная"},
   {"id": 3, "name": "Coca-cola 1 литр"},
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
    text = """ <h1> "Имя: Антон "</h1> </br>
               <h1> "Отчество: Валерьевич "</h1> </br>
               <h1> "Фамилия: Проскуряков"</h1>  
           """
    return HttpResponse(text)

def item_des(request,id):
    for item in items:
        if item["id"] == id:
            context = {
                "item": item["name"]
            }

    return render(request, "item.html", context)

def get_items(request):
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)
