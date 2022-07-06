from django.urls import path
from . import views

urlpatterns = [
    path('', views.showstart),
    path('signup/', views.singup),
    path('login/', views.login),
    path('find/', views.find),
    path('find1/', views.find1),
    path('findId/', views.findId),
    path('findPw/', views.findPw),

]