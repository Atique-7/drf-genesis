from profiles_api import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls))
]

