from django.shortcuts import render
from django.core.paginator import Paginator

from Article.models import Article
# def Base(request):
#     """
#     模板页，默认不用视图指出，指出的目的是在创建之初进行调试使用
#     """
#     return render(request,"base.html")

def index(request):
    """
    首页
    """
    # 按照点赞数为主排序时间倒序为第二排序的逻辑查询所有推荐的文章
    articles = Article.objects.filter(recommend=True).order_by("favor", "-time")[:10]
    return render(request, "index.html",locals())


def diary(request):
    """
    个人简介
    展示推荐文章
    """
    title = "个人简介"
    article = Article.objects.get(id = 6)
    return render(request, "article.html", locals())

def myPhoto(request):
    """
    个人相册
    """
    return render(request, "my_photo.html")

def articleList(request,types,page=1):
    articleType = Article.article_type
    title, = [i[1] for i in articleType if i[0] == types]
    page = int(page)
    next_page = page+1
    last_page = page-1
    articles = Article.objects.filter(articleType=types).order_by("favor", "-time")
    paginator = Paginator(articles,8)
    data = paginator.page(page)
    return render(request,"article_list.html",locals())
def articles(request,id):
    article = Article.objects.get(id=id)
    try:
        previous_article = Article.objects.filter(id__lt=id)[0] #上一页
    except Exception as e:
        print(e)
    try:
        next_article = Article.objects.filter(id__gt=id)[0] #下一页
    except Exception as e:
        print(e)
    return render(request,"article.html",locals())
#
# def selfDiary(request):
#     """
#     个人日记
#     """
#     title = "个人日记"
#     articles = Article.objects.filter(recommend=True).order_by("favor", "-time")[:10]
#     return render(request, "article_list.html",locals())
#
# def skillDiary(request):
#     """
#     学习笔记
#     """
#     title = "学习笔记"
#     return render(request, "article_list.html",locals())
#
# def skillArticle(request):
#     """
#     技术文章
#     """
#     title = "技术文章"
#     return render(request, "article_list.html",locals())

def message(request):
    """
    给我留言
    """
    return render(request, "tem/index.html")

# Create your views here.
