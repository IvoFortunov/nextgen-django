from django.urls import path
from . import views

urlpatterns = [
    path('programs', views.programs, name='programs'),
    path('program/<str:pk>', views.programDetail, name='program-detail'),
    path('programs-admin', views.programsAdmin, name='programs-admin'),

    path('create-program', views.createProgram, name='create-program'),
    path('edit-program/<str:pk>', views.editProgram, name='edit-program'),
    path('delete-program/<str:pk>', views.deleteProgram, name='delete-program'),
]