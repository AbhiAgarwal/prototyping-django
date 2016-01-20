# -*- coding: utf-8 -*-
from rest_framework import routers
from today.apps.events.views import EventsViewSet

router = routers.DefaultRouter()
router.register(r'events', EventsViewSet, base_name='event')
