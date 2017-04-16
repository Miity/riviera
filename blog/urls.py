from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.blog, name='BlogList'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='PostDetail'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.blog, name='BlogListByCategory'),
]
