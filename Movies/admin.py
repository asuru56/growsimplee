from django.contrib import admin
from .models import Movies, NewTrailer, SeriesModel, season
# Register your models here.

admin.site.register(Movies)
admin.site.register(NewTrailer)
admin.site.register(SeriesModel)
admin.site.register(season)
