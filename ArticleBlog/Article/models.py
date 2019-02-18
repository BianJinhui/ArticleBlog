from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    """
    文章类型：
        个人日记
        学习笔记
        技术文章
        个人简介
    文章族
        原创
        转载
    推荐
    """
    articleType = [
        ("selfDiary", "个人日记"),
        ("skillDiary", "学习笔记"),
        ("skillArticle", "技术文章"),
        ("diary", "个人简介"),
    ]
    articleFamily = [
        ("diary", "原创"),
        ("diary", "转载"),
    ]
    title = models.CharField(max_length = 32,verbose_name = "文章标题")
    author = models.CharField(max_length = 32,verbose_name = "文章作者")
    time = models.DateField(verbose_name = "发表时间")
    discription = RichTextField(verbose_name="文章描述")
    content = RichTextField(verbose_name="文章内容")
    picture = models.ImageField(verbose_name="文章图片")
    favor = models.IntegerField(default = 0,verbose_name = "点赞数")
    articleType = models.CharField(max_length = 32,verbose_name = "文章类型",choices = articleType,default = "个人日记",)
    articleFamily = models.CharField(max_length = 32,verbose_name = "文章类型",choices = articleFamily,default = "原创",)
    recommend = models.BooleanField(verbose_name="推荐")


# Create your models here.
