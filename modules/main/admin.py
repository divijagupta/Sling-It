# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

@admin.register(UrlTable)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('short_url', 'active_hits',)
# Register your models here.