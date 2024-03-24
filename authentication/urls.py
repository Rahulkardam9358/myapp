from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authentication.views import UserCreateViewset, UserCreateRealtorViewset

router = DefaultRouter()

router.register('create-user', UserCreateViewset, basename='create-user')
router.register('create-realtor', UserCreateRealtorViewset, basename='create-realtor-user')

urlpatterns = [
    path('auth/', include(router.urls)),
]