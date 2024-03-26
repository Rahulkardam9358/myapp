from django.urls import path, include
from rest_framework.routers import DefaultRouter
from listings.views import ListingViewset
router = DefaultRouter()

router.register('listing', ListingViewset, basename='create-listing')

urlpatterns = [
    path('listings/create/', include(router.urls)),
]