from django.conf.urls import url
from django.contrib import admin
from photos import views

urlpatterns = [
	url(r'^$', views.index, name='home_page'),
]
