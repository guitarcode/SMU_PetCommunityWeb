# 자랑하기 게시판의 views
import datetime
from .models import Post,Comment,PostImage,Hashtag
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.utils import timezone
from .forms import NoneTitleForm, ImageForm,CommentForm

def showoffAll(request) :
    showoffPostList = Post.objects.filter(type = 1).order_by('-date')
    return render(request,'post_all.html',{'showoffPostList':showoffPostList})

def showoffDetail(request, id) :
    showoffPost = get_object_or_404(Post,pk=id)
    images = showoffPost.postimage_set.all
    comments = showoffPost.comment_set.all
    tags = showoffPost.hashtag.all()
    commentForm = CommentForm()

    return render(request,'post_detail.html',{'showoffPost':showoffPost,'comments':comments,
                                              'images':images,'tags':tags,
                                            'commentForm':commentForm})

def showoffCreate(request) :
    ImageFormSet = modelformset_factory(PostImage,form=ImageForm, extra=3)
    if request.method == 'POST':
        form = NoneTitleForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset = PostImage.objects.none())
        if form.is_valid() and formset.is_valid():
            post = Post()
            print(form['title'])
            post.title = form['title']
            post.content = form['content']
            post.date = timezone.now()
            post.writer = request.user
            post.type = 1
            post.save()
            for form1 in formset.cleaned_data:
                image = form1['image']
                photo = PostImage(post=post, image=image)
                photo.save()

            tags = form.cleaned_data['tag'].split('#')
            for tag in tags:
                if not tag:
                    continue
                else:
                    tag = tag.strip()
                    tag_, created = Hashtag.objects.get_or_create(hashtag=tag)
                    post.hashtag.add(tag_)
            return redirect('showoffAll')
    else :
        form = NoneTitleForm()
        formset = ImageFormSet(queryset = PostImage.objects.none())
    return render(request, 'board/write.html',{'showoffCreateForm':form,'formset':formset})

def showoffUpdate(request, id) :
    update = Post.get_object_or_404(Post,pk=id)
    ImageFormSet = modelformset_factory(PostImage,form=ImageForm, extra=3)
    if request.method == 'POST':
        form = NoneTitleForm(request.POST, instance = update)
        formset = ImageFormSet(request.POST, request.FILES, instance = update)
        if form.is_valid() and formset.is_valid():
            post = form.save(commit = False)
            post.date = datetime.timezone.now()
            post.save()
            for form in formset.cleaned_data:
                image = form['image']
                photo = PostImage(post = post, image = image)
                photo.save()
            return redirect('showoffDetail',id)
    else :
        form = NoneTitleForm(instance = update)
        formset = ImageFormSet(instance = update)
    return render(request, 'post_create.html',{'showoffCreateForm':form,'formset':formset})


def showoffDelete(request, id) :
        Post.objects.filter(pk=id).delete()
        return redirect('showoffAll')

