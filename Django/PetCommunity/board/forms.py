from django import forms
from .models import Post, Comment, PostImage, Hashtag

class ImageForm(forms.ModelForm):
    class Meta :
        model = PostImage
        fields = ['image',]

class NoneTitleForm(forms.ModelForm):
    content =  forms.CharField(max_length=300)
    class Meta:
        model = Post
        # 모든 필드를 입력받고 싶을 때
        fields = ['content','hashtag',]