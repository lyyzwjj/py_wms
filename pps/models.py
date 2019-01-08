from django.db import models


# Create your models here.
class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    bprice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
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


class Employee(models.Model):
    name = models.CharField(max_length=255, db_column='name')
    password = models.CharField(max_length=255, db_column='password')
    email = models.CharField(max_length=255, db_column='email')
    age = models.IntegerField(db_column='age')
    admin = models.BooleanField(default=False)
    dept = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "employee"


class Department(models.Model):
    name = models.CharField(max_length=255, db_column='name')
    sn = models.CharField(max_length=255, db_column='sn')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "department"
