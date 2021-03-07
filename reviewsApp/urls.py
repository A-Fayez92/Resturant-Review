from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('logout/', views.user_logout, name="logout"),
    path('addreview/<str:pk>/', views.add_review, name="add_review"),
    path('viewreview/<str:pk>/', views.view_review, name="view_review"),
]