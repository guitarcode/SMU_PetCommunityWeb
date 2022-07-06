from django.urls import path
from . import qna_views, showoff_views

showoffpatterns = [
    path('',showoff_views.showoffAll, name='showoffAll'),
    path('<int:post_id>', showoff_views.showoffDetail, name='showoffDetail')
]

qnapatterns = [
    path('', qna_views.qnaAll),
    path('<int:post_id>/', qna_views.qnaDetail),
]

urlpatterns = [
    path('showoff/', include(showoffpatterns)),
    path('qna/', include(qnapatterns)),
]