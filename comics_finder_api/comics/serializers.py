from rest_framework import serializers

from .models import Comic, Author, Editor, Collection, Serie

class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = "__all__"

class CollectionSerializer(serializers.ModelSerializer):
    editor = EditorSerializer()

    class Meta:
        model = Collection
        fields = "__all__"

class SerieSerializer(serializers.ModelSerializer):
    collection = CollectionSerializer()

    class Meta:
        model = Serie
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class ComicSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    serie = SerieSerializer()

    class Meta:
        model = Comic
        fields = "__all__"