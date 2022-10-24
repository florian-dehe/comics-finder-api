from rest_framework import viewsets

from .models import Comic
from .serializers import ComicSerializer

# Create your views here.

class ComicViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer