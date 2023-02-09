from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComicViewset, SerieViewset, CollectionViewset, EditorViewset

router = DefaultRouter()
router.register(r'comics', ComicViewset, basename="comic")
router.register(r'series', SerieViewset, basename="series")
router.register(r'collections', CollectionViewset, basename="collection")
router.register(r'editors', EditorViewset, basename="editor")

urlpatterns = [
    path('', include(router.urls))
]
