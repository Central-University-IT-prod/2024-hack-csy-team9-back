from django.shortcuts import render

# Create your views here.
from django.views.generic import (
   ListView,
   DetailView,
)
 
from .models import Entry
 
class EntryListView(ListView):
   model = Entry
   queryset = Entry.objects.all().order_by("-date_created") #Это ключевой запрос — он возвращает все существующие записи по нашему первичному ключу, сортируя их по дате создания.
 
class EntryDetailView(DetailView): #Дополнительно создаём представление с подклассом DetailView. Будем использовать его позже.
   model = Entry