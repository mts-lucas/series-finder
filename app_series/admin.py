from django.contrib import admin

from .models import Episode, Season, Serie

# Register your models here.


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    ...


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    ...


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    ...
