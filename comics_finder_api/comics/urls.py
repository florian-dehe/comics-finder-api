from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComicViewset

router = DefaultRouter()
router.register(r'comics', ComicViewset, basename="comic")

urlpatterns = [
    path('', include(router.urls))
]
