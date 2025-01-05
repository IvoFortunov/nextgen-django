from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from nextgen.settings import EMAIL_HOST_USER
from django.db.models import Q
from .models import WeeklyEvaluation, CommonEvaluation, MatchEvaluation, DailyEvaluation, ConditioningEvaluation
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def searchWeeklyEvaluations(request):
    search_query=''
    if request.GET.get('search_query'):
       search_query=request.GET.get('search_query')

    evaluations = WeeklyEvaluation.objects.distinct().filter(Q(player__name__icontains=search_query))
    
    return evaluations, search_query

def paginateEvaluations(request, evaluations, results):
    page = request.GET.get('page')
    paginator = Paginator(evaluations,results)
    try:
        evaluations = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        evaluations = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        evaluations = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex,rightIndex)
    return custom_range, evaluations


def sendWeekEvaluationEmail(evaluation):
    playerEmail = evaluation.player.email
    linkedEmail = evaluation.player.linked_email

    subject = 'Оценка - Седмица: ' + str(evaluation.week) + ', ' + str(evaluation.year) + ' година'
    html_message = render_to_string('evaluations/weekly_email.html', {'evaluation': evaluation})
    plain_message = strip_tags(html_message)

    if(playerEmail):
        send_mail(subject, plain_message, EMAIL_HOST_USER, [playerEmail], html_message=html_message)

    if(linkedEmail):
        send_mail(subject, plain_message, EMAIL_HOST_USER, [linkedEmail], html_message=html_message)



def searchCommonEvaluations(request):
    search_query=''
    if request.GET.get('search_query'):
       search_query=request.GET.get('search_query')

    evaluations = CommonEvaluation.objects.distinct().filter(Q(player__name__icontains=search_query))
    
    return evaluations, search_query

def searchMatchEvaluations(request):
    search_query=''
    if request.GET.get('search_query'):
       search_query=request.GET.get('search_query')

    evaluations = MatchEvaluation.objects.distinct().filter(Q(player__name__icontains=search_query))
    
    return evaluations, search_query

def searchDailyEvaluations(request):
    search_query=''
    if request.GET.get('search_query'):
       search_query=request.GET.get('search_query')

    evaluations = DailyEvaluation.objects.distinct().filter(Q(player__name__icontains=search_query))
    
    return evaluations, search_query

def searchConditioningEvaluations(request):
    search_query=''
    if request.GET.get('search_query'):
       search_query=request.GET.get('search_query')

    evaluations = ConditioningEvaluation.objects.distinct().filter(Q(player__name__icontains=search_query))
    
    return evaluations, search_query




    