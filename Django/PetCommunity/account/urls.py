from django.urls import path
from . import views

urlpatterns = [
    path('', views.showstart),
    path('signup/', views.singup),
    path('login/', views.login),
    path('find/', views.find),
    path('findId/', views.findId),
]