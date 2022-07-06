# Q&A 게시판의 views
from .models import Post

def qnaAll(request) :
    qnaPostList = Post.objects.filter()