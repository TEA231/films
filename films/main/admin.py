from django.contrib import admin

from .models import *

class FilmsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'key')
    list_display_links = ('id', 'key')
    search_fields = ['text']

admin.site.register(Comments, CommentsAdmin)
admin.site.register(Films, FilmsAdmin)
