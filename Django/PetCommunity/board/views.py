from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import CommentForm

def createComment(request, post_id) :
    mid_form = CommentForm(request.POST)
    if mid_form.is_valid():
        fin_form = mid_form.save(commit=False)
        fin_form.post = get_object_or_404(Post,pk=post_id)
        fin_form.save()
        return redirect('postDetail',post_id)

# Create your views here.
