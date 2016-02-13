from django.shortcuts import render
from django.conf import settings
from .models import category


def index(request):
	"""
	Render Home Page
	"""
	title = settings.WEBSITE_TITLE
	data = category().get_categories()
	return render(request, 'photos/index.html', {
		'title':title,
		'data':data,
		'BASE_BACKGROUND_IMAGE': settings.BASE_BACKGROUND_IMAGE_STATIC_PATH
	})
