from django.contrib import admin
from photo_manager.models import Photos,Category,Location

# Register your models here.
admin.site.register(Photos)
admin.site.register(Category)
admin.site.register(Location)
