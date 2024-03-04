from django.contrib import admin #어드민 툴을 사용하겠다
from .models import TweetModel #트윗앱의 모델을 들고 오겠다

# Register your models here.
admin.site.register(TweetModel) #admin 페이지에 추가