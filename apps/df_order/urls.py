#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from df_order import views

app_name = 'df_order'

urlpatterns = [
    url(r'^$', views.order),
    url(r'^push/$', views.order_handle),
]