from django.conf.urls import url
from pages.views import index, contact

urlpatterns = [
    url(r'^$', index),
    url(r'^contact/$', contact)
]