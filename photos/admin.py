from django.contrib import admin

from .models import category, Image, Subscribe
from sorl.thumbnail.admin import AdminImageMixin


class CategoryAdmin(admin.ModelAdmin):
    list_display  = ['title', 'status']

class ImageAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display  = ['title','image','cameraModel', 'category', 'status']

admin.site.register(category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Subscribe)