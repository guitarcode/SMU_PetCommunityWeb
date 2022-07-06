# 자랑하기 게시판의 views
import datetime
from .models import Post,Comment,PostImage
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from .forms import NoneTitleForm, ImageForm

def showoffAll(request) :
    showoffPostList = Post.objects.filter(type = 1).order_by('-date')
    return render(request,'post_all.html',{'showoffPostList':showoffPostList})

def showoffDetail(request, id) :
    showoffPost = Post.get_object_or_404(Post,pk=id)
    comments = showoffPost.post.all()

    return render(request,'post_detail.html',{'showoffPost':showoffPost,'comments':comments})

def showoffCreate(request) :
    ImageFormSet = modelformset_factory(PostImage,form=ImageForm, extra=3)
    if request.method == 'POST':
        form = NoneTitleForm()
        formset = ImageFormSet(request.POST, request.FILES, queryset = PostImage.objects.none())
        if form.is_valid() and formset.is_valid():
            post = form.save(commit = False)
            post.writer = request.user
            post.date = datetime.timezone.now()
            post.save()
            for form in formset.cleaned_data:
                image = form['image']
                photo = PostImage(post = post, image = image)
                photo.save()
            return redirect('showoffAll')
    else :
        form = NoneTitleForm()
        formset = ImageFormSet(queryset = PostImage.objects.none())
    return render(request, 'post_create.html',{'showoffCreateForm':form,'formset':formset},
                    context_instance=RequestContext(request))

def showoffDelete(request, id) :
        Post.objects.filter(pk=id).delete()
        return redirect('showoffAll')

