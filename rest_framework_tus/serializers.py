# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from rest_framework_tus.models import get_upload_model
from django.utils.module_loading import import_string


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_upload_model()
        fields = '__all__'


def resolve_serializer_from_string(serializer_import):
    return import_string(serializer_import)
