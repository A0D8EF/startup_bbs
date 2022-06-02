from django.db import models
from django.utils import timezone


class Category(models.Model):
    
    name = models.CharField(verbose_name="カテゴリ名", max_length=20)

    def __str__(self):
        return self.name


class Topic(models.Model):

    category = models.ForeignKey(Category, verbose_name="カテゴリ", on_delete=models.CASCADE)

    name = models.CharField(verbose_name="名前", max_length=100)
    comment = models.CharField(verbose_name="コメント", max_length=2000)
    dt = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)

    def __str__(self):
        return self.comment