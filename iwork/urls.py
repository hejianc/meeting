# -*- coding: utf-8 -*-


from django.conf.urls import patterns

urlpatterns = patterns(
    'iwork.views',
    (r'^$', 'home'),
)
