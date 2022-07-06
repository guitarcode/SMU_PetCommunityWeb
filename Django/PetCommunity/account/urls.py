from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import URLPattern

urlpatterns = [
    path('', views.showstart),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('member_update/', views.update, name='update'),
    path('profile/<str:member_id>', views.profile, name='profile'),
    path('delete/', views.delete, name='delete'),
    path('find/', views.find),
    path('find1/', views.find1),
    path('findID/', views.findID, name='findID'),
    path('findPW/', views.findPW, name='findPW'),
    path('main/' ,views.main, name='main' ),
    path('set/' ,views.set, name='set'),
    path('profilepage/' ,views.profilepage, name='profilepage'),
    path('write/' ,views.write, name="write"),

    # 비밀번호 찾기 URL
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


]