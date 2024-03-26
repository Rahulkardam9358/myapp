from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authentication.views import UserCreateViewset, UserCreateRealtorViewset, UserGetViewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

router.register('me', UserGetViewset, basename='get-user')
router.register('create', UserCreateViewset, basename='create-user')
router.register('create-realtor', UserCreateRealtorViewset, basename='create-realtor')

urlpatterns = [
    path('auth/users/', include(router.urls)),
    path('auth/users/token/', TokenObtainPairView.as_view()),
    path('auth/users/refresh/', TokenRefreshView.as_view()),
    path('auth/users/verify/', TokenVerifyView.as_view()),
]