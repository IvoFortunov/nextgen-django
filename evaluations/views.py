from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WeeklyEvaluation, CommonEvaluation, MatchEvaluation, DailyEvaluation, ConditioningEvaluation
from users.models import Profile
from django.contrib import messages
from .forms import EditWeeklyForm, EditCommonForm, EditMatchForm, EditDailyForm, EditConditioningForm
from .utils import sendWeekEvaluationEmail, paginateEvaluations, searchWeeklyEvaluations, searchCommonEvaluations, searchMatchEvaluations, searchDailyEvaluations, searchConditioningEvaluations

@login_required(login_url='login')
def weekEvaluations(request):
    evaluations, search_query = searchWeeklyEvaluations(request)
    if request.user.profile.is_coach:
       isCoach=True
       pass
    else:
        isCoach=False
        evaluations = evaluations.filter(player=request.user.profile)
    
    custom_range, evaluations = paginateEvaluations(request, evaluations, 10)    

    context = {'evaluations' : evaluations, 'custom_range':custom_range, 'search_query':search_query, 'isCoach':isCoach}
    return render(request, 'evaluations/weekly.html', context)

@login_required(login_url='login')
def commonEvaluations(request):
    evaluations, search_query = searchCommonEvaluations(request)
    if request.user.profile.is_coach:
       isCoach=True
       pass
    else:
        isCoach=False
        evaluations = evaluations.filter(player=request.user.profile)
    
    custom_range, evaluations = paginateEvaluations(request, evaluations, 10)    

    context = {'evaluations' : evaluations, 'custom_range':custom_range, 'search_query':search_query, 'isCoach':isCoach}
    return render(request, 'evaluations/common.html', context)

@login_required(login_url='login')
def matchEvaluations(request):
    evaluations, search_query = searchMatchEvaluations(request)
    if request.user.profile.is_coach:
       isCoach=True
       evaluations = evaluations.filter(coachVisible=True)
    else:
        isCoach=False
        evaluations = evaluations.filter(player=request.user.profile)
    
    custom_range, evaluations = paginateEvaluations(request, evaluations, 10)    

    context = {'evaluations' : evaluations, 'custom_range':custom_range, 'search_query':search_query, 'isCoach':isCoach}
    return render(request, 'evaluations/match.html', context)

@login_required(login_url='login')
def dailyEvaluations(request):
    evaluations, search_query = searchDailyEvaluations(request)
    if request.user.profile.is_coach:
       isCoach=True
       evaluations = evaluations.filter(coachVisible=True)
    else:
        isCoach=False
        evaluations = evaluations.filter(player=request.user.profile)
    
    custom_range, evaluations = paginateEvaluations(request, evaluations, 10)    

    context = {'evaluations' : evaluations, 'custom_range':custom_range, 'search_query':search_query, 'isCoach':isCoach}
    return render(request, 'evaluations/daily.html', context)

@login_required(login_url='login')
def conditioningEvaluations(request):
    evaluations, search_query = searchConditioningEvaluations(request)
    if request.user.profile.is_coach:
       isCoach=True
       pass
    else:
        isCoach=False
        evaluations = evaluations.filter(player=request.user.profile)
    
    custom_range, evaluations = paginateEvaluations(request, evaluations, 10)    

    context = {'evaluations' : evaluations, 'custom_range':custom_range, 'search_query':search_query, 'isCoach':isCoach}
    return render(request, 'evaluations/conditioning.html', context)




@login_required(login_url='login')
def createWeekEvaluation(request):
    form = EditWeeklyForm()

    if request.user.profile.is_coach:
        form.fields['player_motivation'].widget.attrs['readonly'] = "readonly"
        form.fields['player_concentration'].widget.attrs['readonly'] = "readonly"
        form.fields['player_discipline'].widget.attrs['readonly'] = "readonly"
        form.fields['player_effort'].widget.attrs['readonly'] = "readonly"
        form.fields['player_understanding'].widget.attrs['readonly'] = "readonly"
        form.fields['player_feedback'].widget.attrs['readonly'] = "readonly"
        form.fields['coach'].required=True
    else:
        form.fields['coach_motivation'].widget.attrs['readonly'] = "readonly"
        form.fields['coach_concentration'].widget.attrs['readonly'] = "readonly"
        form.fields['coach_discipline'].widget.attrs['readonly'] = "readonly"
        form.fields['coach_effort'].widget.attrs['readonly'] = "readonly"
        form.fields['coach_understanding'].widget.attrs['readonly'] = "readonly"
        form.fields['coach_feedback'].widget.attrs['readonly'] = "readonly"
        form.fields['player'].queryset = Profile.objects.filter(user__id=request.user.id)

    form.fields['coach'].queryset = Profile.objects.filter(is_coach=True)

    if request.method == 'POST':
        form = EditWeeklyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('week-evaluations')
        else:
            messages.error(request,'За тази седмица вече съществува оценка за този играч')
        

    context={'form':form, 'isNew': True}
    return render(request, 'evaluations/weekly_form.html',context)

@login_required(login_url='login')
def editWeekEvaluation(request, pk):
    evaluation = WeeklyEvaluation.objects.get(id=pk)
    form = EditWeeklyForm(instance=evaluation)

    form.fields['player'].widget.attrs['readonly'] = "readonly"
    form.fields['coach'].queryset = Profile.objects.filter(is_coach=True)

    if request.user.profile.is_coach:     
        form.fields['player_motivation'].widget.attrs['readonly'] = "readonly"
        form.fields['player_concentration'].widget.attrs['readonly'] = "readonly"
        form.fields['player_discipline'].widget.attrs['readonly'] = "readonly"
        form.fields['player_effort'].widget.attrs['readonly'] = "readonly"
        form.fields['player_understanding'].widget.attrs['readonly'] = "readonly"
        form.fields['player_feedback'].widget.attrs['readonly'] = "readonly"
        form.fields['coach'].required=True
    else:
        form.fields['coach_motivation'].widget.attrs['readonly'] = "readonly"
        form.fields['coach_concentration'].widget.attrs['readonly'] = "readonly"
        form.fields['coach_discipline'].widget.attrs['readonly'] = "readonly"
        form.fields['coach_effort'].widget.attrs['readonly'] = "readonly"
        form.fields['coach_understanding'].widget.attrs['readonly'] = "readonly"
        form.fields['coach_feedback'].widget.attrs['readonly'] = "readonly"


    if request.method == 'POST':
        form = EditWeeklyForm(request.POST, instance=evaluation)
        if form.is_valid():
            form.save()
            if request.user.profile.is_coach:
                sendWeekEvaluationEmail(evaluation)
            return redirect('week-evaluations')
        else:
            messages.error(request,'За тази седмица вече съществува оценка за този играч')
      

    context={'form':form, 'isNew':False}
    return render(request, 'evaluations/weekly_form.html',context)


@login_required(login_url='login')
def createCommonEvaluation(request):
    form = EditCommonForm()
    
    form.fields['player'].queryset = Profile.objects.filter(user__id=request.user.id)
    if request.method == 'POST':
        form = EditCommonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('common-evaluations')
      

    context={'form':form, 'isNew': True}
    return render(request, 'evaluations/common_form.html',context)

@login_required(login_url='login')
def editCommonEvaluation(request, pk):
    evaluation = CommonEvaluation.objects.get(id=pk)
    form = EditCommonForm(instance=evaluation)

    form.fields['player'].widget.attrs['readonly'] = "readonly"

    if request.method == 'POST':
        form = EditCommonForm(request.POST, instance=evaluation)
        if form.is_valid():
            form.save()
            return redirect('common-evaluations')
      

    context={'form':form, 'isNew':False}
    return render(request, 'evaluations/common_form.html',context)

@login_required(login_url='login')
def viewCommonEvaluation(request, pk):
    evaluation = CommonEvaluation.objects.get(id=pk)
    form = EditCommonForm(instance=evaluation)

    for name, field in form.fields.items():
        field.widget.attrs['readonly'] = "readonly"
      
    context={'form':form, 'isNew':False, 'viewOnly':True}
    return render(request, 'evaluations/common_form.html',context)


@login_required(login_url='login')
def createMatchEvaluation(request):
    form = EditMatchForm()
    
    form.fields['player'].queryset = Profile.objects.filter(user__id=request.user.id)
    if request.method == 'POST':
        form = EditMatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('match-evaluations')
      

    context={'form':form, 'isNew': True}
    return render(request, 'evaluations/match_form.html',context)

@login_required(login_url='login')
def editMatchEvaluation(request, pk):
    evaluation = MatchEvaluation.objects.get(id=pk)
    form = EditMatchForm(instance=evaluation)

    form.fields['player'].widget.attrs['readonly'] = "readonly"

    if request.method == 'POST':
        form = EditMatchForm(request.POST, instance=evaluation)
        if form.is_valid():
            form.save()
            return redirect('match-evaluations')
      

    context={'form':form, 'isNew':False}
    return render(request, 'evaluations/match_form.html',context)

@login_required(login_url='login')
def viewMatchEvaluation(request, pk):
    evaluation = MatchEvaluation.objects.get(id=pk)
    form = EditMatchForm(instance=evaluation)

    for name, field in form.fields.items():
        field.widget.attrs['readonly'] = "readonly"
      
    context={'form':form, 'isNew':False, 'viewOnly':True}
    return render(request, 'evaluations/match_form.html',context)

@login_required(login_url='login')
def createDailyEvaluation(request):
    form = EditDailyForm()
    
    form.fields['player'].queryset = Profile.objects.filter(user__id=request.user.id)
    form.fields['coach'].queryset = Profile.objects.filter(is_coach=True)
    
    if request.method == 'POST':
        form = EditDailyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daily-evaluations')
      

    context={'form':form, 'isNew': True}
    return render(request, 'evaluations/daily_form.html',context)

@login_required(login_url='login')
def editDailyEvaluation(request, pk):
    evaluation = DailyEvaluation.objects.get(id=pk)
    form = EditDailyForm(instance=evaluation)

    form.fields['player'].widget.attrs['readonly'] = "readonly"
    form.fields['coach'].queryset = Profile.objects.filter(is_coach=True)

    if request.method == 'POST':
        form = EditDailyForm(request.POST, instance=evaluation)
        if form.is_valid():
            form.save()
            return redirect('daily-evaluations')
      

    context={'form':form, 'isNew':False}
    return render(request, 'evaluations/daily_form.html',context)

@login_required(login_url='login')
def viewDailyEvaluation(request, pk):
    evaluation = DailyEvaluation.objects.get(id=pk)
    form = EditDailyForm(instance=evaluation)

    for name, field in form.fields.items():
        field.widget.attrs['readonly'] = "readonly"
      
    context={'form':form, 'isNew':False, 'viewOnly':True}
    return render(request, 'evaluations/daily_form.html',context)

@login_required(login_url='login')
def createConditioningEvaluation(request):
    form = EditConditioningForm()

    if request.user.profile.is_coach:
        form.fields['coach'].required=True
        form.fields['coach'].queryset = Profile.objects.filter(is_coach=True)

    if request.method == 'POST':
        form = EditConditioningForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conditioning-evaluations')
        else:
            messages.error(request,'За тази седмица вече съществува оценка за този играч')
        

    context={'form':form, 'isNew': True}
    return render(request, 'evaluations/conditioning_form.html',context)

@login_required(login_url='login')
def editConditioningEvaluation(request, pk):
    evaluation = ConditioningEvaluation.objects.get(id=pk)
    form = EditConditioningForm(instance=evaluation)

    form.fields['player'].widget.attrs['readonly'] = "readonly"
    form.fields['coach'].queryset = Profile.objects.filter(is_coach=True)

    if request.user.profile.is_coach:     
        form.fields['coach'].required=True


    if request.method == 'POST':
        form = EditConditioningForm(request.POST, instance=evaluation)
        if form.is_valid():
            form.save()
            return redirect('conditioning-evaluations')
        else:
            messages.error(request,'За тази седмица вече съществува оценка за този играч')
      

    context={'form':form, 'isNew':False}
    return render(request, 'evaluations/conditioning_form.html',context)

@login_required(login_url='login')
def viewConditioningEvaluation(request, pk):
    evaluation = ConditioningEvaluation.objects.get(id=pk)
    form = EditConditioningForm(instance=evaluation)

    for name, field in form.fields.items():
        field.widget.attrs['readonly'] = "readonly"
      
    context={'form':form, 'isNew':False, 'viewOnly':True}
    return render(request, 'evaluations/conditioning_form.html',context)

