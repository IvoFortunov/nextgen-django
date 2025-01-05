from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('change-password/', views.changePassword, name='change-password'),
    # path('register/', views.registerUser, name='register'),


    path('players/', views.playerProfiles, name='players'),
    path('presentations/', views.presentations, name='presentations'),
    path('playersotw/', views.playersOTW, name='playersotw'),
    path('coaches/', views.coachProfiles, name='coaches'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('presentation/<str:pk>/', views.userPresentation, name='user-presentation'),
    path('account/', views.userAccount, name='account'),
    path('edit-account/', views.editAccount, name='edit-account'),
    path('create-player/', views.createPlayer, name='create-player'),
    path('create-coach/', views.createCoach, name='create-coach'),
    path('delete-user/<str:pk>', views.deleteUser, name='delete-user'),

    path('playersotwadmin/', views.playersOTWAdmin, name='playersotwadmin'),
    path('create-playerotw/', views.createPlayerOTW, name='create-playerotw'),
    path('edit-playerotw/<str:pk>/', views.editPlayerOTW, name='edit-playerotw'),
    
    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('create-message/<str:pk>/', views.createMessage, name="create-message"),
]