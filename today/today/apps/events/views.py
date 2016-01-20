# -*- coding: utf-8 -*-
from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets


class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self,):
        queryset = Event.objects.all()
        uid = self.kwargs.get('pk')
        if uid:
            return queryset.filter(pk=uid)
        else:
            return queryset
