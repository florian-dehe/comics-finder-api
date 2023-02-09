from rest_framework import serializers

from .models import Comic, Author, Editor, Collection, Serie

class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = [ "id", "name" ]


class CollectionSerializer(serializers.ModelSerializer):
    editor_info = EditorSerializer(source="editor", read_only=True)

    class Meta:
        model = Collection
        fields = [ "id", "name", "editor", "editor_info"]


class SerieSerializer(serializers.ModelSerializer):
    collection_info = CollectionSerializer(source="collection", read_only=True)
    
    name = serializers.CharField(max_length=25, source="serie_name")

    class Meta:
        model = Serie
        fields = [ "id", "name", "collection", "collection_info"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [ "id", "name" ]


class ComicSerializer(serializers.ModelSerializer):
    authors_info = AuthorSerializer(source="authors", many=True, read_only=True)
    serie_info = SerieSerializer(source="serie", read_only=True)

    class Meta:
        model = Comic
        fields = "__all__"