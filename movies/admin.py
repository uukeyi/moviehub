from django.contrib import admin
from . import models

class ActorAdmin(admin.ModelAdmin):
    pass

class FilmWorkAdmin(admin.ModelAdmin):
    pass

class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Actor , ActorAdmin)
admin.site.register(models.FilmWork , FilmWorkAdmin)
admin.site.register(models.Genre , GenreAdmin)
