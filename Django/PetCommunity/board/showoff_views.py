# 자랑하기 게시판의 views
from models import Post,Comment
from django.shortcuts import render, redirect, get_object_or_404

def showoffAll(request) :
    showoffPostList = Post.objects.filter(type = 1).order_by('-date')
    return render(request,'post_all.html',{'showoffPostList':showoffPostList})

def showoffDetail(request, id) :
    showoffPost = Post.get_object_or_404(Post,pk=id)
    comments = showoffPost.post.all()

    return render(request,'post_detail.html',{'showoffPost':showoffPost,'comments':comments})

def showoffCreate(request) :
    if request.method == 'GET' :


