#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 开发时间: 2019/7/13 11:33
# 开发人员: Mikel
# 邮箱地址: plyx_46204@126.com
# 文件名称: serializers.py
# 开发团队：云飞国际
# 开发工具：PyCharm

from rest_framework import serializers
from users.models import UserProfile

"""使用简单序列化
class UserProfileSerializer(serializers.Serializer):
    
    # 简单序列化
    新建一个序列化对象来映射每一个字段，当返回数据或者post数据的时候
    可以直接通过 serializer 保存到数据库中
    和 form 的功能相类似，专门用于 json 中的
    
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    email = serializers.CharField(required=True, max_length=100)
"""

"""使用模型序列化"""

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['password']




