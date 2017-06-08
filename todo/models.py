# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Todo(models.Model):
    text = models.TextField()
    completed = models.BooleanField(default=False)
    class Meta:
        ordering = ('id',)