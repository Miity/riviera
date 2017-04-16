from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


# страница блога (всех статтей)
def blog(request, category_slug=None,):
    category = None
    categories = Category.objects.all()
    post = Post.objects.filter(post_available=True)
    current_page = Paginator(post, 5)
    page = request.GET.get('page')

    if category_slug:
        category = get_object_or_404(Category, category_slug=category_slug)
        post = Post.objects.filter(post_category=category)
        current_page = Paginator(post, 5)
        page = request.GET.get('page')

    try:
        posts = current_page.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = current_page.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = current_page.page(current_page.num_pages)

    return render(request, 'blog/blog.html', {
        'categories': categories,
        'category': category,
        'posts': posts
    })


# Страница поста
def post_detail(request, id):
    post = get_object_or_404(Post, id=id, post_available=True)
    return render(request, 'blog/post_detail.html', {'post': post})