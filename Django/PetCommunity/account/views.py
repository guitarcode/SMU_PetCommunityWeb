from django.shortcuts import render

# Create your views here.



def showstart(request):
    return render(request, 'account/start.html')


def singup(request):
    return render(request, 'account/signup.html')


def login(request):
    return render(request, 'account/login.html')


def find(request):
    return render(request, 'account/find.html')


def findId(request):
    return render(request, 'account/findId.html')


def findPw(request):
    return render(request, 'account/findPw.html')


def find1(request):
    return render(request, 'account/find1.html')