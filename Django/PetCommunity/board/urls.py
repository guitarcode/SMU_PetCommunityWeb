from django.urls import path, include
from . import showoff_views,qna_views

showoffpatterns = [
    path('',showoff_views.showoffAll, name='showoffAll'),
    path('<int:post_id>/', showoff_views.showoffDetail, name='showoffDetail')
]

qnapatterns = [
    path('', qna_views.qnaAll),
    # path('<int:post_id>/', qna_views.qnaDetail),
]

urlpatterns = [
    path('showoff/', include(showoffpatterns)),
    path('qna/', include(qnapatterns)),
]