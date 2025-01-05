from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Presentation, PlayerOTW
from .forms import ProfileForm, ChangePasswordForm, CustomUserCreationForm, MessageForm, PlayerOTWForm
import os
from .utils import searchPlayersOTW, paginatePlayersOTW, sendPlayerOTWEmail

def loginUser(request):
    page = 'login'
    context = {'page':page}
   
    if request.user.is_authenticated:
        return redirect('news')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:         
            messages.error(request, "User does not exist")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('news')
        else:
            messages.error(request, "Username or Password incorrect")

    return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, "User was logged out")
    return render(request, 'users/login.html')

@login_required(login_url='login')
def changePassword(request):
    user = request.user
    form = ChangePasswordForm(user=user)
    if request.method=='POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('account')
        else:
            messages.error(request,form.errors)
            

    context={'form':form}
    return render(request, 'users/changepassword_form.html',context)

def playerProfiles(request):
    profiles = Profile.objects.filter(is_coach=False)
    context = {'profiles' : profiles}
    return render(request, 'users/profiles.html', context)

def presentations(request):
    presentations = Presentation.objects.all
    context = {'presentations' : presentations}
    return render(request, 'users/presentations.html', context)

def playersOTW(request):
    players = PlayerOTW.objects.all
    context = {'players' : players}
    return render(request, 'users/playersotw.html', context)


def coachProfiles(request):
    profiles = Profile.objects.filter(is_coach=True)
    context = {'profiles' : profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profileObj = Profile.objects.get(id=pk)
    potw_count = PlayerOTW.objects.filter(player__id=pk).count()

    context = {'profile':profileObj, 'potw_count':potw_count}
    return render(request, 'users/user-profile.html', context)

def userPresentation(request, pk):
    presentationObj = Presentation.objects.get(id=pk)

    context = {'presentation':presentationObj}
    return render(request, 'users/user-presentation.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    context = {'profile':profile}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    old_image = profile.profile_image.path   
    form = ProfileForm(instance=profile)
    if request.method == 'POST':        
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            updated = form.save(commit=False)
            if not updated.profile_image:
                updated.profile_image = 'profiles/user-default.png'
                
            new_image = updated.profile_image.path
            if 'user-default' not in old_image and old_image!=new_image:
                if os.path.exists(old_image):
                    os.remove(old_image)
            updated.save()
            user = request.user
            user.email = request.POST.get('email')
            user.save()
            return redirect('account')
        else:
            messages.error(request,form.errors)

    context={'form':form}
    return render(request, 'users/profile_form.html',context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def createCoach(request):
    return createUser(request,True)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def createPlayer(request):
    return createUser(request,False)

@login_required(login_url='login')
def createUser(request,isCoach):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            profile = Profile()
            profile.user = user
            profile.name = user.first_name + ' ' + user.last_name
            profile.username = user.username
            profile.email = user.email
            profile.is_coach = isCoach
            user.save()
            profile.save()            
            messages.success(request, 'Потребителят е добавен!')

            return redirect('news')

        else:
            messages.error(
                request, form.errors)

    context = { 'form': form, 'isCoach':isCoach}
    return render(request, 'users/create_user.html', context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def deleteUser(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        user = profile.user
        profile.delete()
        user.delete()
        messages.success(request, 'Потребителят е изтрит успешно!')
        return redirect('players')

    context = {'object': profile}
    return render(request, 'delete_template.html', context)

@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.recipient.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
    return render(request, 'users/inbox.html', context)


@login_required(login_url='login')
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.recipient.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {'message': message}
    return render(request, 'users/message.html', context)

@login_required(login_url='login')
def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request, 'Съобщението е изпратено успешно!')
            return redirect('user-profile', pk=recipient.id)

    context = {'recipient': recipient, 'form': form}
    return render(request, 'users/message_form.html', context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def playersOTWAdmin(request):
    players, search_query = searchPlayersOTW(request)    
    custom_range, evaluations = paginatePlayersOTW(request, players, 10) 
    context = {'players':players, 'custom_range':custom_range, 'search_query':search_query}
    return render(request, 'users/playersotw_admin.html', context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def createPlayerOTW(request):
    form = PlayerOTWForm()

    form.fields['player'].queryset = Profile.objects.filter(is_coach=False)

    if request.method == 'POST':
        form = PlayerOTWForm(request.POST)
        if form.is_valid():
            playerOtw = form.save()
            sendPlayerOTWEmail(playerOtw)
            return redirect('playersotwadmin')
        else:
            messages.error(request,'За тази седмица вече съществува играч на седмицата')
        
    context={'form':form, 'isNew': True}
    return render(request, 'users/playerotw_form.html',context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def editPlayerOTW(request,pk):
    playerOtw = PlayerOTW.objects.get(id=pk)
    form = PlayerOTWForm(instance=playerOtw)

    form.fields['player'].queryset = Profile.objects.filter(is_coach=False)

    if request.method == 'POST':
        form = PlayerOTWForm(request.POST, instance=playerOtw)
        if form.is_valid():
            form.save()
            sendPlayerOTWEmail(playerOtw)
            return redirect('playersotwadmin')
        else:
            messages.error(request,'За тази седмица вече съществува играч на седмицата')
        
    context={'form':form, 'isNew': False}
    return render(request, 'users/playerotw_form.html',context)


