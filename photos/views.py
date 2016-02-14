from django.shortcuts import render
from django.conf import settings
from .models import category, Image


def indexView(request):
	"""
	Render Home Page
	"""
	title = settings.WEBSITE_TITLE
	description = settings.WEBSITE_DESCRIPTION
	keywords = settings.WEBSITE_KEYWORDS
	author = settings.WEBSITE_AUTHOR
	baseDomain = settings.WEBSITE_BASE_DOMAIN
	data = category().get_categories()
	return render(request, 'photos/index.html', {
		'title':title,
		'description':description,
		'keywords':keywords,
		'author':author,
		'data':data,
		'BASE_BACKGROUND_IMAGE': settings.BASE_BACKGROUND_IMAGE_STATIC_PATH,
		'baseDomain':baseDomain
	})


def categoryView(request, id):
	"""
	Render category view
	"""
	requestData = request.GET
	title = settings.WEBSITE_TITLE
	description = settings.WEBSITE_DESCRIPTION
	keywords = settings.WEBSITE_KEYWORDS
	author = settings.WEBSITE_AUTHOR
	data = Image().get_images(category_id=id, request_data=requestData)
	baseDomain = settings.WEBSITE_BASE_DOMAIN
	if data:
		return render(request, 'photos/category/index.html', {
			'title':title,
			'description':description,
			'author':author,
			'keywords':keywords,
			'data':data,
			'baseDomain':baseDomain
		})
	else:
		return render(request, 'photos/err/404.html', {
			'title':title,
			'description':description,
			'author':author,
			'keywords':keywords
		})


def imageView(request, id):
	"""
	Render Image View
	"""
	title = settings.WEBSITE_TITLE
	description = settings.WEBSITE_DESCRIPTION
	keywords = settings.WEBSITE_KEYWORDS
	author = settings.WEBSITE_AUTHOR
	baseDomain = settings.WEBSITE_BASE_DOMAIN
	try:
		data = Image.objects.get(id=int(id))
		return render(request, 'photos/image/index.html', {
			'title':title,
			'description':description,
			'keywords':keywords,
			'author':author,
			'baseDomain':baseDomain,
			'data':data
		})
	except Exception, e:
		return render(request, 'photos/err/500.html', {
			'title':title,
			'description':description,
			'author':author,
			'keywords':keywords
		})
	except Image.DoesNotExist, e:
		return render(request, 'photos/err/404.html', {
			'title':title,
			'description':description,
			'author':author,
			'keywords':keywords
		})


