#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/7/13 9:50
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: views_base.py
# 开发团队：云飞国际
# 开发工具：PyCharm

from django.views.generic.base import View

from .models import UserProfile

class UserProfileListView(View):
    def get(self, request):
        """
        通过 django 的 view 实现人员信息列表
        :param request:
        :return:
        """
        json_list = []
        users = UserProfile.objects.all()[:10]
        for user in users:
            json_dict = {}
            json_dict["first_name"] = user.first_name
            json_dict["last_name"] = user.last_name
            # json_dict["email"] = user.email
            json_list.append(json_dict)
        from django.http import HttpResponse
        import json
        return HttpResponse(json.dumps(json_list), content_type="application/json")