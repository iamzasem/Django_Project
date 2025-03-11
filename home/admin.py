# admin.py
from django.contrib import admin # type: ignore
from .models import AlbumCategory, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3

class AlbumCategoryAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('name',)

admin.site.register(AlbumCategory, AlbumCategoryAdmin)
admin.site.register(Photo)