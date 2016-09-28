from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = [
	url(r'^categories/(?P<categoryId>[0-9]+)$', views.CategoryImageList.as_view()),
    url(r'^categories/$', views.CategoriesList.as_view()),
    url(r'^feed/$', views.FeedActivityList.as_view()),
    url(r'^subscribe/$', views.Subscribe.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)