from django import forms
from models import Post, Comment, PostImage

class imageForm(forms.Modelform):
    class Meta :
        model = PostImage
        fields = ['image',]

imageFormSet = forms.inlineformset_factory(Post, PostImage, form=ImageForm, )
class showoffCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        # 모든 필드를 입력받고 싶을 때
        fields = ['content',]
        # 특정 필드만 입력받고 싶을 때
        #fields = ['title','body']
