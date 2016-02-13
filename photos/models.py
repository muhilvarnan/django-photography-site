from __future__ import unicode_literals

from django.db import models
from sorl.thumbnail import ImageField

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
		result = []
		for item in category.objects.filter(status=1):
			tempImages = []
			for image in item.imageCategory.filter(status=1)[:5]:
				tempImages.append(image)
			if tempImages:
			   result.append({
			   	'category':item,
			   	'imageSet':tempImages
			   	})
		return result

class Image(models.Model):
	"""
	Photo Image Model
	"""
	STATUS_CHOICES = (
		(0,'Disabled'),
		(1,'Enabled')
	)
	title = models.CharField(max_length=255)
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
	share_instagram = models.BooleanField(default=False)
	share_twitter = models.BooleanField(default=False)
	share_googleplus = models.BooleanField(default=False)
	created_datetime = models.DateTimeField(auto_now_add=True, editable=False)
	last_updated_datetime =  models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		ordering = ['-created_datetime']

	def __str__(self):
		return self.title