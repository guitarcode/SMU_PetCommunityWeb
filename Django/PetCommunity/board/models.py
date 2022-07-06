from django.db import models

class Hashtag(models.Model):
    hashtag = models.CharField(max_length=30)
    def __str__(self):
        return self.hashtag


#이미지를 위해 pip로 pillow를 설치해줘야함
#게시글
class Post(models.Model):
    #게시글 기본정보
    title = models.CharField(max_length=50)
    content = models.TextField(blank = True, null = True)
    date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey('account.Member', on_delete= models.DO_NOTHING)
    hashtag = models.ManyToManyField(Hashtag, null = True)

    #게시판 목록
    TYPE_CHOICES = [
        (1,'Showoff'),
        (2,'Challenge'),
        (3,'Qna'),
        (4,'Share'),
    ]
    type = models.SmallIntegerField(choices = TYPE_CHOICES)

    recommandCount = models.IntegerField(blank = True, default = 0)

    #답변 게시글, 답변이 있는 경우 질문 글은 삭제 불가능
    answerPost = models.ForeignKey('self', on_delete = models.PROTECT, null = True)

    def __int__(self):
        return self.pk


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'postImage')

#좋아요
class Recommand(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    recommander = models.ForeignKey('account.Member', on_delete= models.DO_NOTHING)

#댓글
class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    writer = models.ForeignKey('account.Member', on_delete= models.DO_NOTHING)
    reply = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)


# Create your models here.
