from django.urls import path
from . import views

urlpatterns = [
    path('', views.showstart),
    path('signup/', views.singup),
]