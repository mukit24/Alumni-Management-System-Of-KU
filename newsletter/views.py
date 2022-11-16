from django.shortcuts import render
from .models import News, News_Letter
# Create your views here.

def index_view(request, id):
    news_letters = News_Letter.objects.all()
    news_list = News.objects.filter(news_letter = id).order_by('created_on')

    context = {
        'newsletters':news_letters,
        'news_list': news_list,
    }
    return render(request,'newsletter/index.html',context)

def news_details(request,id):
    news = News.objects.get(id=id)
    context = {
        'news':news,
    }
    return render(request,"newsletter/news_details.html",context)
