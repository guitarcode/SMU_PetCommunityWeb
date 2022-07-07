from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.
def main(request):
    memberName = request.user.memberName
    return render(request, 'board/main.html', {'memberName': memberName})


def set(request):
    return render(request, 'board/set.html')


def profilepage(request):
    return render(request, 'board/profile.html')





def infoShare(request):
    return render(request, 'board/infoShare.html')
