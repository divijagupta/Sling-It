# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UrlTable(models.Model):
	short_url=models.URLField(max_length=100)
	long_url=models.URLField(max_length=1000)
	active_hits=models.IntegerField(default=0)
# Create your models here.
