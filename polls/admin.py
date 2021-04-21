from django.contrib import admin

from .models import Question
from .models import Song

admin.site.register(Question)
admin.site.register(Song)