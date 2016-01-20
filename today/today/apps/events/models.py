# -*- coding: utf-8 -*-
from django.db import models


class Event(models.Model):
    name = models.TextField(blank=False, max_length=100)
    description = models.TextField(blank=False, max_length=1000)
    date = models.DateTimeField(blank=False, null=False)
    image = models.URLField(blank=True, max_length=500)

    def __unicode__(self):
        return self.name