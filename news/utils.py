from django.core.mail import send_mail
from django.db.models import Q
from .models import News
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def searchNews(request):
    search_query=''
    if request.GET.get('search_query'):
       search_query=request.GET.get('search_query')

    news = News.objects.distinct().filter(Q(title__icontains=search_query))
    
    return news, search_query

def paginateNews(request, news, results):
    page = request.GET.get('page')
    paginator = Paginator(news,results)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        news = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        news = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex,rightIndex)
    return custom_range, news