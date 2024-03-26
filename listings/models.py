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
        max_length=255
    )
    title = models.CharField(_("title"), max_length=225)
    slug = models.SlugField(_("slug"), unique=True)
    description = models.TextField(_("description"))
    address_line1 = models.CharField(max_length=255, null=False, blank=False)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=25, blank=False)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=25, blank=False)
    country = models.CharField(max_length=25, blank=False)
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


class Image(models.Model):
    listing = models.ForeignKey(
        Listing, 
        on_delete=models.CASCADE, 
        related_name='images'
    )
    image = models.ImageField(upload_to='media/listings/')

    def __str__(self) -> str:
        return f'Image | {self.id}'
