from rest_framework import viewsets

from .models import Comic, Serie, Collection, Editor, Author
from .serializers import ComicSerializer, SerieSerializer, CollectionSerializer, EditorSerializer, AuthorSerializer

# Create your views here.

class ComicViewset(viewsets.ModelViewSet):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer

class SerieViewset(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

class CollectionViewset(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class EditorViewset(viewsets.ModelViewSet):
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer

class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer