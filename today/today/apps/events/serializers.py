# -*- coding: utf-8 -*-
from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'name': obj.name,
            'description': obj.description,
            'date': obj.date,
            'image': obj.image,
        }

    class Meta:
        model = Event
        fields = ('name', 'description', 'date', 'image',)
