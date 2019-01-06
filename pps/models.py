from django.db import models


# Create your models here.
class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    '''英雄人物模型类'''
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)


class Brand(models.Model):
    name = models.CharField(max_length=255, db_column='name')
    sn = models.CharField(max_length=255, db_column='sn')

    class Meta:
        db_table = "brand"
