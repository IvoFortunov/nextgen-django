from django.urls import path
from . import views

urlpatterns = [
    path('weekly/', views.weekEvaluations, name='week-evaluations'),
    path('common/', views.commonEvaluations, name='common-evaluations'),
    path('match/', views.matchEvaluations, name='match-evaluations'),
    path('daily/', views.dailyEvaluations, name='daily-evaluations'),
    path('conditioning/', views.conditioningEvaluations, name='conditioning-evaluations'),
    
    path('createweekly/', views.createWeekEvaluation, name='create-week-evaluations'),
    path('editweekly/<str:pk>', views.editWeekEvaluation, name='edit-week-evaluations'),

    path('createcommon/', views.createCommonEvaluation, name='create-common-evaluations'),
    path('editcommon/<str:pk>', views.editCommonEvaluation, name='edit-common-evaluations'),
    path('viewcommon/<str:pk>', views.viewCommonEvaluation, name='view-common-evaluations'),

    path('creatematch/', views.createMatchEvaluation, name='create-match-evaluations'),
    path('editmatch/<str:pk>', views.editMatchEvaluation, name='edit-match-evaluations'),
    path('viewmatch/<str:pk>', views.viewMatchEvaluation, name='view-match-evaluations'),

    path('createdaily/', views.createDailyEvaluation, name='create-daily-evaluations'),
    path('editdaily/<str:pk>', views.editDailyEvaluation, name='edit-daily-evaluations'),
    path('viewdaily/<str:pk>', views.viewDailyEvaluation, name='view-daily-evaluations'),

    path('createconditioning/', views.createConditioningEvaluation, name='create-conditioning-evaluations'),
    path('editconditioning/<str:pk>', views.editConditioningEvaluation, name='edit-conditioning-evaluations'),
    path('viewdconditioning/<str:pk>', views.viewConditioningEvaluation, name='view-conditioning-evaluations'),

    
]