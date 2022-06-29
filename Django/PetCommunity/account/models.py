from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from django.core.validators import RegexValidator

class Member(AbstractUser):
    #회원id : Model에서 자동으로 생성
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
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

    # Profile
    # nickname = models.CharField(max_length=100)
    # intorduction = models.TextField(blank=True)
    # image
