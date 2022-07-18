from django.db import models
from django.conf import settings

class ToDo(models.Model):
    title = models.CharField('タイトル', max_length=50, blank=False)
    content = models.TextField('内容')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='ログインユーザー', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.
