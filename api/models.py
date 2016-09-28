from photos.models import category
from photos.models import Image, Device, Subscribe
from sorl.thumbnail import get_thumbnail
from rest_framework import status
from django.conf import settings
from django.core.paginator import Paginator


def get_feed_activity_list(request):
	"""
	get feed activity list
	"""
	try:
		result = []
		imageCOllection = Image.objects.filter(status=1).order_by('-created_datetime')
		paginatedCollection = Paginator(imageCOllection, 10)
		page = int(request.GET.get("page", "1"))	
		pageCollection = paginatedCollection.page(page)
		for imageItem in pageCollection.object_list:
			temp = frame_image_details(imageItem)
			if temp:
				result.append(temp)
		return {
			'status':True,
			'details':{
				'total_page':paginatedCollection.num_pages,
				'current_page':page,
				'items':result
			}
		}
	except Exception, e:
		return {
			'status':False,
			'details':str(e),
			'statusCode':status.HTTP_500_INTERNAL_SERVER_ERROR
		}

def frame_image_details(imageObj):
	"""
	Frame image details
	"""
	try:
		temp = {}
		temp['id'] = imageObj.id
		temp['title'] = imageObj.title
		temp['image'] = settings.WEBSITE_BASE_DOMAIN +get_thumbnail(imageObj.image, '600x400', crop='center', quality=99).url
		return temp
	except Exception, e:
		print e
		return None
		
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
			temp['nav_icon'] = settings.WEBSITE_BASE_DOMAIN  + categoryItem.nav_icon.url
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

def get_category_image_list(request, categoryId):
	"""
	get category list
	"""
	try:
		result = []
		categoryObj = category.objects.get(id=categoryId)
		imageCOllection = Image.objects.filter(status=1, category=categoryObj)
		paginatedCollection = Paginator(imageCOllection, 10)
		page = int(request.GET.get("page", "1"))	
		pageCollection = paginatedCollection.page(page)
		for imageItem in pageCollection.object_list:
			temp = frame_image_details(imageItem)
			if temp:
				result.append(temp)
		return {
			'status':True,
			'details':{
				'total_page':paginatedCollection.num_pages,
				'current_page':page,
				'items':result
			}
		}
	except Exception, e:
		return {
			'status':False,
			'details':str(e),
			'statusCode':status.HTTP_500_INTERNAL_SERVER_ERROR
		}

def device_entry(request):
	"""
	device entry
	"""
	try:
		deviceType = request.data.get("deviceType")
		deviceId = request.data.get("deviceId")
		deviceToken = request.data.get("deviceToken")
		deviceObj, isNew = Device.objects.get_or_create(deviceType=deviceType, deviceId=deviceId, deviceToken=deviceToken)
		return {
			'status':True,
			'details':deviceObj
		}
	except Exception, e:
		return {
			'status':False,
			'details':str(e),
			'statusCode':status.HTTP_500_INTERNAL_SERVER_ERROR
		}

def post_subscribe(request):
	"""
	post subscribe
	"""
	try:
		email = request.data.get("email")
		result = device_entry(request)
		if result.get("status"):
			subscribeObj, isNew = Subscribe.objects.get_or_create(email=email)
			subscribeObj.devices.add(result.get('details'))
			subscribeObj.save()
			return {
				'status':True,
				'details':"Email has registered succesfully"
			}
	except Exception, e:
		return {
			'status':False,
			'details':str(e),
			'statusCode':status.HTTP_500_INTERNAL_SERVER_ERROR
		}