from django.db import models


class BookInfoManager(models.Manager):
    '''改变查询的结果集'''

    def all(self):
        books = super().all()
        books = books.filter(isDelete=False)
        return books

    '''封装函数'''

    def create_book(self, btitle, bpub_date):
        # book = BookInfo()
        book = self.model
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        return book


# Create your models here.
class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField(null=True)
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    bprice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    isDelete = models.BooleanField(default=False)
    objects = BookInfoManager()
    '''
    @classmethod
    def createBook(cls, btitle, bpub_date):
        obj = cls()
        obj.btitle = btitle
        obj.bpub_date = bpub_date
        obj.save()
        return obj
    '''


class HeroInfo(models.Model):
    '''英雄人物模型类'''
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)


class NewsType(models.Model):
    '''新闻类型类'''
    type_name = models.CharField(max_length=20)
    news_info = models.ManyToManyField("NewsInfo")


class NewsInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    # news_type = models.ManyToManyField("NewsType")


class EmployeeBasicInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=False)
    age = models.IntegerField()
    employee_detail = models.OneToOneField('EmployeeDetailInfo', on_delete=models.CASCADE)


class EmployeeDetailInfo(models.Model):
    addr = models.CharField(max_length=256)
    # employee_basic = models.OneToOneField('EmployeeBasicInfo')


class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


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


class SystemMenu(models.Model):
    name = models.CharField(max_length=255, db_column='name')
    sn = models.CharField(max_length=255, db_column='sn')
    url = models.CharField(max_length=255, db_column='url')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "systemmenu"


class PicTest(models.Model):
    '''上传图片'''
    gpic = models.ImageField(upload_to='pps')
