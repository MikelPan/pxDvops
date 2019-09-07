#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/9/7 12:16
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: backends.py
# 开发团队：云飞国际
# 开发工具：PyCharm



from .models import UserProfile

class EmailBackend(object):
    def authenticate(self, request, **credentials):
        # 要注意登录表单中用户输入的用户名或者邮箱的 field 名均为 username
        email = credentials.get('email', credentials.get('username'))
        try:
            user = UserProfile.objects.get(email=email)
        except UserProfile.DoesNotExist:
            pass
        else:
            if user.check_password(credentials["password"]):
                return user

    def get_user(self, user_id):
        """
        该方法是必须的
        """
        try:
            return UserProfile.objects.get(pk=user_id)
        except UserProfile.DoesNotExist:
            return None