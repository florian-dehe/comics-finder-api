from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=25, null=False)

    def __str__(self) -> str:
        return self.name

class Editor(models.Model):
    name = models.CharField(max_length=25, null=False)

    def __str__(self) -> str:
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=25, null=False)

    editor = models.ForeignKey(Editor, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return self.name

class Serie(models.Model):
    serie_name = models.CharField(max_length=25, null=False)

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return self.serie_name


class Comic(models.Model):
    title = models.CharField(max_length=25, null=False)
    description = models.TextField()
    volume = models.IntegerField()

    release_date = models.DateField()
    pages = models.IntegerField()
    isbn = models.IntegerField()

    cover_url = models.CharField(max_length=250)

    serie = models.ForeignKey(Serie, models.CASCADE, null=False)
    authors = models.ManyToManyField("Author")

    def __str__(self) -> str:
        return str(self.serie) + " - " + str(self.volume) + "." + str(self.title)