# tweet/models.py
from django.db import models
from user.models import UserModel #유저앱의 모델을 들고 온 것
from taggit.managers import TaggableManager


# Create your models here.
class TweetModel(models.Model): #트윗이 가능하게 모델 생성
    class Meta: #DB에 추가
        db_table = "tweet"
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE) #ForeignKey는 다른 DB에서 가져오겠다
    content = models.CharField(max_length=256)
    tags = TaggableManager(blank=True) #태그가 비어있어도 작성 하겠다라는 뜻 False라면 무조건 작성해야된다는 것
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TweetComment(models.Model):
    class Meta:
        db_table = "comment"
    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)