#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-27 下午3:32
# @Author  : hucl
"""Defines url patterns for login."""

from django.conf.urls import url

from . import views

app_name = 'login'
urlpatterns = [
    # Home page.
    url(r'^$', views.index, name='index'),

    # Show all topics.
    url(r'^topics/$', views.topics, name='topics'),

    # Detail page for a single topic.
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # Page for adding a new topic.
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # Page for adding a new entry.
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # Page for editing an entry.
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
        name='edit_entry'),
]
