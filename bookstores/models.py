from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=20, default='example')
    file = models.TextField(max_length=20*1024*1024)

    def __str__(self):
        return self.name

admin.site.register(Store)

