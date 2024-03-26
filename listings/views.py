from rest_framework import viewsets, permissions
from listings.serializers import ListingSerializer, ImageSerializer
from listings.models import Listing, Image

# Create your views here.
class ListingViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

