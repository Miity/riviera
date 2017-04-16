from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.


# Модель категории
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True, verbose_name="Название")
    category_slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name="URL-название")
    category_parent = models.ForeignKey('self', related_name='category', verbose_name='Родительская категория',
                                        blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blog:BlogListByCategory', args=[self.category_slug,])

    class Meta():
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Post(models.Model):
    post_category = models.ForeignKey(Category, related_name='post', verbose_name="Категория")
    post_title = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    post_slug = models.SlugField(max_length=200, db_index=True, verbose_name="URL-название")
    post_img = models.ImageField(upload_to='blog_titels/', blank=True, null=True, verbose_name="Изображение")
    post_description = RichTextUploadingField(blank=True, verbose_name="Описание")
    post_short_description = models.TextField(max_length=300, blank=True, null=True, verbose_name="Короткое описание")
    post_available = models.BooleanField(default=True, verbose_name="Опубликованно")
    post_posted = models.DateField(auto_now_add=True, verbose_name="Дата публикации")


    class Meta():
        db_table = 'posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-id']

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('blog:PostDetail', args=[self.id])

    def get_next(self):
        try:
            return Post.objects.all().filter(id__gt=self.id).exclude(id=self.id).order_by(
                'id')[:1].get()
        except Post.DoesNotExist:
            return

    def get_prev(self):
        try:
            return Post.objects.all().filter(id__lt=self.id).exclude(id=self.id).order_by(
                '-id')[:1].get()
        except Post.DoesNotExist:
            return

    def bit(self):
        if self.post_img:
            return u'<img src="/media/{}" width="100px"/>'.format(self.post_img)
        else:
            return u'(none)'
    bit.short_description = u'Изображение'
    bit.allow_tags = True




