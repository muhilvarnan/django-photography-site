from photos.models import category
from photos.models import Image
from sorl.thumbnail import get_thumbnail
from rest_framework import status
from django.conf import settings

def get_category_list():
	"""
	get category list
	"""
	try:
		result = []
		categoryCOllection = category.objects.filter(status=1)
		for categoryItem in categoryCOllection:
			temp = {}
			temp['id'] = categoryItem.id
			temp['title'] = categoryItem.title
			temp['image'] = settings.WEBSITE_BASE_DOMAIN +get_thumbnail(categoryItem.image, '600x400', crop='center', quality=99).url
			print temp['image']
			result.append(temp)
		return {
			'status':True,
			'details':result
		}
	except Exception, e:
		return {
			'status':False,
			'details':str(e),
			'statusCode':status.HTTP_500_INTERNAL_SERVER_ERROR
		}

def get_category_image_list(categoryId):
	"""
	get category list
	"""
	try:
		result = []
		categoryObj = category.objects.get(id=categoryId)
		imageCOllection = Image.objects.filter(status=1, category=categoryObj)
		for imageItem in imageCOllection:
			temp = {}
			temp['id'] = imageItem.id
			temp['title'] = imageItem.title
			temp['image'] = settings.WEBSITE_BASE_DOMAIN +get_thumbnail(imageItem.image, '600x400', crop='center', quality=99).url
			print temp['image']
			result.append(temp)
		return {
			'status':True,
			'details':result
		}
	except Exception, e:
		return {
			'status':False,
			'details':str(e),
			'statusCode':status.HTTP_500_INTERNAL_SERVER_ERROR
		}