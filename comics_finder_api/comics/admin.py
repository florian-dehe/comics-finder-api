from django.contrib import admin

from .models import Author, Editor, Collection, Serie, Comic

# Register your models here.

admin.site.register(Author)
admin.site.register(Editor)
admin.site.register(Collection)
admin.site.register(Serie)
admin.site.register(Comic)
