from tkinter import CASCADE
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from django.core.validators import RegexValidator
from django.conf import settings

class Member(AbstractUser):
    memberID = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    # 정규식으로 유효성 검증
    phoneNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 11, unique = True)
    GENDER_CHOICES = (
        (0, 'Female'),
        (1, 'Male')
    )
    gender = models.SmallIntegerField(choices = GENDER_CHOICES)
    email = models.EmailField(max_length=128)
    address = models.CharField(max_length=200)
    point = models.IntegerField(blank=True)
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
    membership = models.SmallIntegerField(choices = MEMBERSHIP_CHOICES, default=1)

class Profile(models.Model):
    memberId = models.OneToOneField(Member, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    intorduction = models.TextField(blank=True)
    photo = models.ImageField(blank=True, null=True, upload_to='profile/photo')

class Accuse(models.Model):
    #신고id : Model에서 자동으로 생성
    title = models.CharField(max_length=100)
    body = models.TextField()
    accusedUser = models.ForeignKey(Member, on_delete=models.CASCADE)
    #accusingUser

    def __str__(self):
        return self.title

class Suspend(models.Model):
    #정지처리id : Model에서 자동으로 생성
    date = models.DateTimeField(auto_now_add=True)
    cause = models.CharField(max_length=300)
    suspendedUser = models.OneToOneField(Member, blank=True, null=True, on_delete=models.CASCADE)
