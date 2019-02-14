from django.db import models
from ckeditor.fields import RichTextField

class Article(models):
    """
    文章类型：
        推荐
            原创
            转载
    """
    title = models.CharField(max_length = 32,verbose_name = "文章标题")
    author = models.CharField(max_length = 32,verbose_name = "文章作者")
    time = models.DateField(verbose_name = "发表时间")
    discription = RichTextField(verbose_name="文章描述")
    content = RichTextField(verbose_name="文章内容")
    picture = models.ImageField(verbose_name="文章图片")
    type = models.CharField(max_length = 32,verbose_name = "文章类型")
    favor = models.IntegerField(default = 0,verbose_name = "点赞数")
    #原创 转载
    #置顶
    #点赞

# Create your models here.
