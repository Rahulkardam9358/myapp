from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'for sale'
        FOR_RENT = 'for rent'
    
    class HomeType(models.TextChoices):
        HOUSE = 'house'
        CONDO = 'condo'
        TOWNHOUSE = 'townhouse'
    realtor = models.EmailField(
        _("email address"), 
        unique=True, max_length=255
    )
    title = models.CharField(_("title"), max_length=225)
    slug = models.SlugField(_("slug"), unique=True)
    description = models.TextField(_("description"))
    price = models.IntegerField()
    bedrooms = models.IntegerField(_("no of bedrooms"))
    bathrooms = models.IntegerField(_("no of bathrooms"))
    sale_type = models.CharField(
        _("sale type"),
        max_length=10,
        choices=SaleType.choices,
        default=SaleType.FOR_SALE
    )
    home_type = models.CharField(
        _("home type"),
        max_length=10,
        choices=HomeType.choices,
        default=HomeType.HOUSE
    )
    is_published = models.BooleanField(
        _("is published"),
        default=False
    )
    date_created = models.DateTimeField(
        _("date created"), 
        default=timezone.now
    )

    def __str__(self) -> str:
        return f'Listing | {self.title} | {self.slug}'
        


class Address(models.Model):
    listing = models.OneToOneField(
        Listing,
        on_delete=models.CASCADE, 
        related_name='address'
    )
    address_line1 = models.CharField(_("address line 1"), max_length=225)
    address_line2 = models.CharField(_("address line 2"), max_length=225)
    city = models.CharField(_("city"), max_length=30)
    zipcode = models.CharField(_("zipcode"), max_length=6)
    state = models.CharField(_("state"), max_length=30)
    country = models.CharField(_("country"), max_length=30)

    def __str__(self) -> str:
        return f'Image | {self.listing__title} | {self.id}'


class Image(models.Model):
    listing = models.ForeignKey(
        Listing, 
        on_delete=models.CASCADE, 
        related_name='images'
    )
    image = models.ImageField(upload_to='listings/')

    def __str__(self) -> str:
        return f'Image | {self.listing__title} | {self.id}'
