from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import auth
from django.conf import settings
from account.models import Profile
from account.models import Member
from account.forms import MemberChangeForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def showstart(request):
    return render(request, 'account/start.html')

def find(request):
    return render(request, 'account/find.html')



def findPW(request):
    return render(request, 'account/findPw.html')


def find1(request):
    return render(request, 'account/find1.html')

# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['repeat']:
            memberId = request.POST['memberId']
            password = request.POST['password']
            username = request.POST['memberName']
            phoneNumber = request.POST['phoneNumber']
            #gender = request.POST['gender']
            email = request.POST['email']
            address = request.POST['address']
            newMember = Member.objects.create_user( username,password , email, memberId=memberId, phoneNumber=phoneNumber, address=address)

            auth.login(request, newMember)
            return redirect('/main')
    return render(request, 'account/signup.html')

# 로그인
def login(request):
    if request.method == 'POST':
        #memberId = request.POST["memberId"]
        memberId = request.POST.get("memberId")
        print(memberId)
        password = request.POST.get("password")
        print(password)
        user = auth.authenticate(request, username=memberId, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/main')
        else:
            return render(request, 'account/bad_login.html')
    else:
        return render(request, 'account/login.html')

# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('showstart')

# 회원정보 수정
@login_required
def update(request):
    if request.method == 'POST':
        changeMemberForm = MemberChangeForm(request.POST, instance=request.user)
        if changeMemberForm.is_valid():
            changeMemberForm.save()
            # 회원정보 확인 페이지 있다면 -> 
            return redirect('account:member_detail')
            # return redirect('showstart')
    else:
        changeMemberForm = MemberChangeForm(instance=request.user)
    return render(request, 'account/member_update.html', {'changeMemberForm':changeMemberForm})

# 프로필
@login_required
def profile(request, member_id):
    if request.method == 'POST' or request.method == "FILES":
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('account:profile')
    else:
        profile, create = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'account/profile_update.html', {'ProfileForm':profile_form})

# 회원 탈퇴
def delete(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user.password == request.POST['password']:
                request.user.delete()
                logout(request)
                return redirect('showstart')
    else:
        return render(request, 'account/delete.html')
        
# 아이디 찾기
def findID(request):
    if request.method == 'POST':
            memberName = request.POST['memberName']
            email = request.POST['email']
            try:
                member = Member.objects.get(email=email)
                memberId = request.POST.get('memberId')
                if member is not None:
                    template = render_to_string('email_template.html', {'memberName': memberName, 'memberId': memberId})
                    method_email = EmailMessage(
                        '우애귀 아이디 찾기 메일을 전송합니다.',
                        template,
                        settings.EMAIL_HOST_USER,
                        [email],
                    )
                    method_email.send(fail_silently=False)
                    return render(request, 'account/findId.html')
            except:
                messages.info(request, "해당 이메일을 가진 회원이 존재하지 않습니다")
    return render(request, 'account/find.html')


