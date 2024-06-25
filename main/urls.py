
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('reservation/', views.profile, name="reservation"),
    path('logout/', views.logout, name="logout"),
    path('details/<int:pk>', views.details, name="details"),
    
    # API Routes
    path('reservation/cancel/<int:id>', views.cancelReservation, name="cancel"),
]


