from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from mediafiles.models import Photo
from .models import Console, Computer, VideoGame, BoardGame


class PhotoInline(GenericTabularInline):
    model = Photo
    extra = 1


@admin.register(Console)
class ConsoleAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ["name", "company", "release_year", "region", "edition", "condition"]


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ["name", "company", "release_year", "region", "edition", "condition"]


@admin.register(VideoGame)
class VideoGameAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ["name", "company", "release_year", "platform", "region", "edition"]


@admin.register(BoardGame)
class BoardGameAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ["name", "company", "release_year", "region", "edition", "condition"]
