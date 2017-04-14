from django.contrib import admin
from .models import Post, Category


# Register your models here.



# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_slug']
    prepopulated_fields = {'category_slug': ('category_name',)}


# Модель поста
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title','post_posted','bit','post_available',]
    list_filter = ['post_available', 'post_posted']
    list_editable = ['post_available']
    search_fields = ['post_title']
    prepopulated_fields = {'post_slug': ('post_title',)}


# Регистрация моделей
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
