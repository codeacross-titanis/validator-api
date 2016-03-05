# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'student', views.StudentViewSet)
router.register(r'provider', views.ProviderViewSet)
router.register(r'badge', views.BadgeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
