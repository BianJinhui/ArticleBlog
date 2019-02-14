from django.contrib import admin
from Article.models import  Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","time"]
    fields = ["title","author","time","discription","content","picture","type"]
admin.site.register(Article,ArticleAdmin)

# Register your models here.
