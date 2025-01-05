from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
import os
from .utils import searchNews,paginateNews
from .models import News
from .forms import EditNewsForm
from users.models import Profile

def news(request):   
    news = News.objects.all
    context = {'news':news}
    return render(request, 'news/news.html', context)

def newsDetail(request, pk):
    newsObj = News.objects.get(id=pk)
    context={'news':newsObj}
    return render(request, 'news/news-detail.html', context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def newsAdmin(request):
    news, search_query = searchNews(request)
    
    custom_range, news = paginateNews(request, news, 10)    

    context = {'news' : news, 'custom_range':custom_range, 'search_query':search_query}
    return render(request, 'news/news-admin.html', context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def createNews(request):
    form = EditNewsForm()
    
    form.fields['author'].queryset = Profile.objects.filter(user__id=request.user.id)
    
    if request.method == 'POST':
        form = EditNewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news-admin')
      

    context={'form':form, 'isNew': True}
    return render(request, 'news/news_form.html',context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def editNews(request, pk):
    news = News.objects.get(id=pk)
    form = EditNewsForm(instance=news)

    form.fields['author'].widget.attrs['readonly'] = "readonly"

    if request.method == 'POST':
        form = EditNewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news-admin')
      

    context={'form':form, 'isNew':False}
    return render(request, 'news/news_form.html',context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def deleteNews(request, pk):
    news = News.objects.get(id=pk)
    if request.method == 'POST':
        image = news.image.path
        news.delete()
        if os.path.exists(image):
            os.remove(image)
        messages.success(request, 'Новината е изтрита успешно!')
        return redirect('news-admin')

    context = {'object': news}
    return render(request, 'delete_template.html', context)



