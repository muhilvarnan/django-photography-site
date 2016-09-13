from photos.models import category, Image
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ('id', 'title', 'image')


class CategoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'title', 'image')

class FeedActivitySerializer(serializers.Serializer):
	"""
	Feed Activity Serializer
	"""