from django.contrib import admin
from django.contrib.admin import site
from django.contrib.admin.options import ModelAdmin

from .models import Link

class LinkAdmin(ModelAdmin):
    list_display = ['pk', 'value', 'expires', 'user']

site.register(Link, LinkAdmin)