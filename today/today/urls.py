# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

from today.apps.router import router

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
]
