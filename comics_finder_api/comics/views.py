from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Comic, Serie, Collection, Editor, Author
from .serializers import ComicSerializer, SerieSerializer, CollectionSerializer, EditorSerializer, AuthorSerializer

# Create your views here.

class ComicViewset(viewsets.ModelViewSet):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer
    permission_classes = [IsAuthenticated]

class SerieViewset(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    permission_classes = [IsAuthenticated]

class CollectionViewset(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]

class EditorViewset(viewsets.ModelViewSet):
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer
    permission_classes = [IsAuthenticated]

class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]