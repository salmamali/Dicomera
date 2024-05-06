# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models


class DicomEntity(models.Model):
    image_type = models.JSONField(null=True)
    instance_creator_uid = models.CharField(null=True, max_length=250)
    extracted = models.BooleanField(default=False)
    processed = models.BooleanField(default=False)
    path = models.CharField(max_length=100)


