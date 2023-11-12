from django.contrib import admin
from .models import Category, Tag, Article, Comment


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_editable = ['slug']
    list_filter = ['name']
    prepopulated_fields = {
        'slug': ['name']
    }
    list_display_links = ['name']


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ['tag']
    list_filter = ['tag']
    list_display_links = ['tag']


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    fields = ['user', 'image', 'date_posted', 'title', 'content', 'slug', 'category', 'tags']
    list_display = ['user', 'category', 'image', 'date_posted', 'title', 'slug', 'content']
    list_filter = ['user', 'date_posted', 'category', 'tags']
    list_editable = ['title', 'content', 'category']
    list_display_links = ['user']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'email', 'date_posted', 'content']
    list_filter = ['user', 'full_name', 'email', 'date_posted']
    list_editable = ['full_name', 'email', 'content']
    list_display_links = ['user']
