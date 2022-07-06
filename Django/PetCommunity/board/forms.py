from django import forms
from .models import Post, Comment, PostImage, Hashtag

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta :
        model = PostImage
        fields = ['image',]

class NoneTitleForm(forms.Form):
    content = forms.CharField(max_length=300, label = "내용")
    tag = forms.CharField(required=False, label="태그")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']