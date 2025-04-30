from django.contrib import admin
from .models import Article, Comment


# Register your models here.
class CommentAdmin(admin.TabularInline):
    model = Comment
    # list_display = ['article', 'author', 'body']
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentAdmin,
    ]

    model = Article

    list_display = ['title', 'author', 'body']




admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
