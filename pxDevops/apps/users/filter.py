#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/7/13 17:53
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: filter.py
# 开发团队：云飞国际
# 开发工具：PyCharm

import django_filters
from .models import UserProfile


class UserProfileFilter(django_filters.rest_framework.FilterSet):
    """ 用户过滤类"""
    min_name = django_filters.NumberFilter(field_name="email", lookup_expr='gte')
    max_name = django_filters.NumberFilter(field_name="email", lookup_expr='lte')
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')  # 模糊查询

    class Meta:
        model = UserProfile
        fields = ['min_name', 'max_name', 'name']