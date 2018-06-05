# -*- coding: UTF-8 -*-
# Author: brain 
# Created_time:2018/6/5 15:51
# file:nav_processor.py
# location :china chengdu 61000
from .models import Column

nav_display_columns = Column.objects.filter(nav_display=True)


def nav_column(request):
    return {'nav_display_columns': nav_display_columns}