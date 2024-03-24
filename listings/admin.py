from django.contrib import admin
from listings.models import Listing, Address, Image

# Register your models here.
admin.site.register(Listing)
admin.site.register(Address)
admin.site.register(Image)