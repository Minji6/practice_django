from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    # on_delete=models.SET_NULL: 회원탈퇴를 했을 때 게시글이 사라지지 않고 알수없음 등으로 설정하겠다는 의미
    # 유저 객체에서 article을 접근할 때 직관적이기 위함

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_created=True, null=True)
    # 언제 만들어졌는지 확인, 생성되었을 때 자동으로 생성시간이 저장된다.