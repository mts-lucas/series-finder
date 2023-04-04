from django.contrib import admin

from .models import Episode, Season, Serie

# Register your models here.


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    ...


class EpisodeInLine(admin.TabularInline):
    model = Episode


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    ...


class SeasonInLine(admin.TabularInline):
    model = Season


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    inlines = [SeasonInLine]
