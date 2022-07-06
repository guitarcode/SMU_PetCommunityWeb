from django.contrib import admin
from .models import Post, PostImage, Comment, Hashtag

admin.site.register(Post)
admin.site.register(Hashtag)

# Register your models here.
