from django.shortcuts import render
from django.http import HttpResponse

items = [
   {"id": 1, "name": "Кроссовки abibas"},
   {"id": 2, "name": "Куртка кожаная"},
   {"id": 3, "name": "Coca-cola 1 литр"},
   {"id": 4, "name": "Картофель фри"},
   {"id": 5, "name": "Кепка"},
]

def home(request):
    text = """<h1> "Изучаем django" </h1 >
              <strong> Автор </strong>: <i> Проскуряков А.П. </i>
           """
    return HttpResponse(text)
def about(request):
    text = """ <h1> "Имя: Антон "</h1> </b>
               <h1> "Отчество: Валерьевич "</h1> </b>
               <h1> "Фамилия: Проскуряков"</h1>  
           """
    return HttpResponse(text)