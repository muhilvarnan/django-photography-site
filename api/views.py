from serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models import get_category_list, get_category_image_list

class CategoriesList(APIView):

	serializer_class = CategorySerializer

	def get(self, request, *args, **kwargs):
		result = get_category_list()
		print result
		if result.get("status"):
			return Response(result.get("details"), status=status.HTTP_200_OK)
		else:
			return Response(result.get("details"), status=result.get("statusCode"))


class CategoryImageList(APIView):

	serializer_class = CategoryImageSerializer

	def get(self,  request, categoryId, *args, **kwargs):
		result = get_category_image_list(categoryId)
		print result
		if result.get("status"):
			return Response(result.get("details"), status=status.HTTP_200_OK)
		else:
			return Response(result.get("details"), status=result.get("statusCode"))