from rest_framework import serializers
from listings.models import Listing, Image
from django.conf import settings


class ImageSerializer(serializers.StringRelatedField):
    def to_representation(self, value):
        return f'{settings.MEDIA_URL}{value.image}'


class ListingSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(
            max_length = 1000000,
            allow_empty_file = False,
            use_url = False
        ),
        write_only = True
    )
    class Meta:
        model = Listing
        fields = '__all__'
        extra_kwargs = {
            'realtor': {
                'read_only': True
            },
            'date_created': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        user = self.context['request'].user
        if user.is_realtor:
            listing = Listing.objects.create(realtor=user.email, **validated_data)
            listing.save(using=settings.LISTING_DB_INSTANCE)
            for image in uploaded_images:
                new_image = Image.objects.create(listing=listing, image=image)
                new_image.save(using=settings.LISTING_DB_INSTANCE)
            return listing
        else:
            raise ValueError('User is not allowed to create listing, since it is not realtor user')


