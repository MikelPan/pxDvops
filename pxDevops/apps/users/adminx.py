#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/7/13 16:13
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: adminx.py
# 开发团队：云飞国际
# 开发工具：PyCharm

import xadmin
from .models import UserProfile




class UserProfileAdmin(object):
      list_display = ['username', 'first_name', 'name', 'birthday', 'gender', 'mobile', 'email']
      search_fields = ['name', 'birthday', 'gender', 'mobile', 'email']
      list_editable = ['name', 'birthday', 'gender', 'mobile']
      list_filter = ['name', 'birthday', 'gender']

xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
