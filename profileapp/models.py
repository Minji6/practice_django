from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True) # 이미지 필드 생성
    nickname = models.CharField(max_length=20, unique=True, null=True) # 닉네임은 1계정 1닉네임
    message = models.CharField(max_length=100, null=True) # 메세지 필드 생성
