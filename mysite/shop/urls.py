from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^shop/$', views.home, name='home'),
     url(r'^$', views.product_list, name='product_list'),
    url(r'^shop/(?P<category_slug>[-\w]+)/$',
        views.product_list, name='product_list_by_category'),
    url(r'^shop/(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail, name='product_detail'),
]
