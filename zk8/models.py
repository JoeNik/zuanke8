# coding:utf-8
from django.db import models

# Create your models here.

class ArticleList(models.Model):
    class Meta:
        db_table = 'ArticleList'
    id = models.AutoField(u'id', max_length=11, db_column='UID', unique=True, primary_key=True)
    title = models.CharField(u'标题', max_length=128, db_index=True)
    content = models.CharField(u'地址', max_length=128, db_index=True)
    remark = models.CharField(u'栏目', max_length=128, blank=True)
