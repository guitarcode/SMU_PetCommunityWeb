from django.urls import path, include
from . import views,showoff_views,qna_views
import account
from . import views

showoffpatterns = [
    path('',showoff_views.showoffAll, name='showoffAll'),
    path('<int:id>/', showoff_views.showoffDetail, name='showoffDetail'),
    path('create/', showoff_views.showoffCreate, name='showoffCreate'),
    path('update/<int:post_id>', showoff_views.showoffUpdate, name='showoffUpdate'),
    path('delete/', showoff_views.showoffDelete, name='showoffDelete'),
]

qnapatterns = [
    path('', qna_views.qnaAll),
    # path('<int:post_id>/', qna_views.qnaDetail),
]


urlpatterns = [
    path('showoff/', include(showoffpatterns)),
    path('qna/', include(qnapatterns)),
    path('account/', include(account.urls)),
    path('main/' ,views.main, name='main' ),
    path('set/' ,views.set, name='set'),
    path('profilepage/' ,views.profilepage, name='profilepage'),

    path('infoShare/', views.infoShare, name="infoShare"),
]
