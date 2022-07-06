from tkinter import CASCADE
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from django.conf import settings
from account.validation import validate_email, validate_password

class Member(AbstractUser):
    memberId = models.CharField(max_length=30, unique=True, default='')
    password = models.CharField(max_length=100)
    memberName = models.CharField(max_length=30, unique=True, default = '', null = True)
    name = models.CharField(max_length=30, null = True)
    # 정규식으로 유효성 검증
    phoneNumber = models.CharField(validators = [validate_password], max_length = 11, unique = True, null = True)
    GENDER_CHOICES = (
        (0, 'Female'),
        (1, 'Male')
    )
    gender = models.SmallIntegerField(choices = GENDER_CHOICES, null = True)
    email = models.EmailField(validators = [validate_email], max_length=128, null = True)
    address = models.CharField(max_length=200, null = True)
    point = models.IntegerField(blank=True, null = True)
    #이모티콘 외래키 참조
    # emoticon = models.ForeignKey(Emoticon, blank=True, null=True, on_delete=models.SET_NULL)
    #팔로우, 팔로워
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    MEMBERSHIP_CHOICES = (
        (1, '아기집사'),
        (2, '어린이집사'),
        (3, '청년집사'),
        (4, '베테랑집사'),
    )
    membership = models.SmallIntegerField(choices = MEMBERSHIP_CHOICES, default=1, null = True)

class Profile(models.Model):
    memberId = models.OneToOneField(Member, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    intorduction = models.TextField(blank=True)
    photo = models.ImageField(blank=True, null=True, upload_to='profile/photo')

class Accuse(models.Model):
    #신고id : Model에서 자동으로 생성
    title = models.CharField(max_length=100)
    body = models.TextField()
    accusedUser = models.ForeignKey(Member, related_name = 'accusedUsers', on_delete=models.CASCADE)
    #accusingUser

    def __str__(self):
        return self.title

class Suspend(models.Model):
    #정지처리id : Model에서 자동으로 생성
    date = models.DateTimeField(auto_now_add=True)
    cause = models.CharField(max_length=300)
    suspendedUser = models.OneToOneField(Member, related_name = 'suspendedUsers', blank=True, null=True, on_delete=models.CASCADE)
