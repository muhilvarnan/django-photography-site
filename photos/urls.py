from django.conf.urls import url
from django.contrib import admin
from photos import views

urlpatterns = [
	url(r'^$', views.indexView, name='home_page'),
	url(r'^category/(?P<id>[0-9]+)/$', views.categoryView, name='category_page'),
	url(r'^image/(?P<id>[0-9]+)/$', views.imageView, name='image_page'),
]
