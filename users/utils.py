from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from nextgen.settings import EMAIL_HOST_USER
from django.db.models import Q
from .models import PlayerOTW
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def searchPlayersOTW(request):
    search_query=''
    if request.GET.get('search_query'):
       search_query=request.GET.get('search_query')

    players = PlayerOTW.objects.distinct().filter(Q(player__name__icontains=search_query))
    
    return players, search_query

def paginatePlayersOTW(request, players, results):
    page = request.GET.get('page')
    paginator = Paginator(players,results)
    try:
        players = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        players = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        players = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex,rightIndex)
    return custom_range, players


def sendPlayerOTWEmail(potw):
    playerEmail = potw.player.email
    linkedEmail = potw.player.linked_email

    subject = 'Играч на седмицата - Седмица: ' + str(potw.week) + ', ' + str(potw.year) + ' година'
    html_message = render_to_string('users/potw_email.html', {'potw': potw})
    plain_message = strip_tags(html_message)

    if(playerEmail):
        send_mail(subject, plain_message, EMAIL_HOST_USER, [playerEmail], html_message=html_message)

    if(linkedEmail):
        send_mail(subject, plain_message, EMAIL_HOST_USER, [linkedEmail], html_message=html_message)





    