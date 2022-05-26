from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from blog.models import (
	Category, Article, Comment, Like
)
# Register your models here.


# Category register to admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('cr_date',)


admin.site.register(Category, CategoryAdmin)


# Article register to admin
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
    	'title', 'is_active' , 'cr_date', 'up_date',
    )
    search_fields = ('title',)
    list_filter = ('cr_date',)


admin.site.register(Article, ArticleAdmin)


# Comment register to admin
class CommentAdmin(admin.ModelAdmin):
    list_display = (
    	'name', 'email', 'is_active', 'article',
    	'cr_date', 'up_date',
    )
    search_fields = ('name',)
    list_filter = ('cr_date',)


admin.site.register(Comment, CommentAdmin)


# Like register to admin
class LikeAdmin(admin.ModelAdmin):
    list_display = (
    	'article', 'cr_date', 'up_date',
    )
    search_fields = ('article',)
    list_filter = ('cr_date',)


admin.site.register(Like, LikeAdmin)