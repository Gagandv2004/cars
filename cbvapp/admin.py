from django.contrib import admin
from cbvapp.models import Company,Products,InteriorImages,ExteriorImages
# Register your models here.
admin.site.register(Company)
admin.site.register(Products)
admin.site.register(InteriorImages)
admin.site.register(ExteriorImages)