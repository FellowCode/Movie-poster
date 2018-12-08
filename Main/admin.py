from django.contrib import admin
from .models import *


class GenreInline(admin.TabularInline):
    model = FilmGenre
    extra = 1

class SessionInline(admin.TabularInline):
    model = Session
    extra = 1

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    inlines = [GenreInline,
               SessionInline,]