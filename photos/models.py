from __future__ import unicode_literals

from django.db import models
from sorl.thumbnail import ImageField
from django.core.paginator import Paginator
from django.conf import settings

class category(models.Model):
	"""
	Photos category Model
	"""
	STATUS_CHOICES = (
		(0,'Disabled'),
		(1,'Enabled')
	)
	title = models.CharField(max_length=255)
	status = models.IntegerField(default=1, choices=STATUS_CHOICES)

	def __str__(self):
		return self.title

	def get_categories(self):
		"""
		list all categories
		"""
		try:
			result = []
			for item in category.objects.filter(status=1):
				try:
					tempImages = []
					for image in item.imageCategory.filter(status=1)[:5]:
						try:
							tempImages.append(image)
						except Exception, e:
							pass
					if tempImages:
					   result.append({
					   	'category':item,
					   	'imageSet':tempImages
					   	})
				except Exception, e:
					pass
			return result
		except Exception, e:
			print e #logger can be configured her
			return []

class Image(models.Model):
	"""
	Photo Image Model
	"""
	STATUS_CHOICES = (
		(0,'Disabled'),
		(1,'Enabled')
	)
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	keywords = models.CharField(max_length=255, blank=True)
	status = models.IntegerField(default=1, choices=STATUS_CHOICES)
	image = ImageField(upload_to='photos')
	category = models.ForeignKey(category, related_name='imageCategory')
	cameraModel = models.CharField(max_length=255)
	cameraLens = models.CharField(max_length=255)
	focalLength = models.CharField(max_length=255, blank=True)
	aperature = models.CharField(max_length=255, blank=True)
	exposureTime = models.CharField(max_length=255, blank=True)
	iso = models.CharField(max_length=255, blank=True)
	share_facebook = models.BooleanField(default=False)
	share_twitter = models.BooleanField(default=False)
	share_googleplus = models.BooleanField(default=False)
	created_datetime = models.DateTimeField(auto_now_add=True, editable=False)
	last_updated_datetime =  models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		ordering = ['-created_datetime']

	def __str__(self):
		return self.title

	def get_pagination_data(self, pagination_data, page_data):
		"""
		Frame pagination data
		"""
		result = { }
		result['totalPages'] = pagination_data.num_pages
		result['currentPage'] = page_data.number
		if page_data.has_next():
			result['nextPage'] = page_data.next_page_number()
		else:
			result['nextPage'] = False
		if page_data.has_previous():
			result['prevPage'] = page_data.previous_page_number()
		else:
			result['prevPage'] = False
		return result

	def get_images(self, category_id, request_data):
		"""
		Get images by category id
		"""
		try:
			result = {}
			categoryObj = category.objects.get(id=category_id, status=1)		
			result['category'] = categoryObj
			paginationData = Paginator(categoryObj.imageCategory.filter(status=1), settings.IMAGE_PAGINATION_COUNT)
			pageData = paginationData.page(int(request_data.get('page', 1)))
			result['imageSet'] = pageData
			result['paginationData'] = self.get_pagination_data(pagination_data=paginationData, 
																page_data=pageData)
			return result
 		except  Exception, e:
			print e
			return {}