from django.contrib import admin
from .models import resturants, review
# Register your models here.
admin.site.site_header = 'Resturant Reviews By Fayez'
admin.site.register(resturants)
admin.site.register(review)