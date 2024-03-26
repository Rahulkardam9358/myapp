from django.contrib import admin
from listings.models import Listing, Image

# Register your models here.
admin.site.register(Listing)
admin.site.register(Image)