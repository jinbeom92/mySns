from django.contrib import admin #어드민 툴을 사용하겠다
from .models import UserModel #내가 만든 모델을 들고 온 것

# Register your models here.
admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다