# from django.shortcuts import render
# from django.views.generic.base import View
# from .models import UserProfile

from .serializers import UserProfileSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework  import DjangoFilterBackend
from .filter import UserProfileFilter
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import render
# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model
from django.db.models import Q
# User = get_user_model()


# Create your views here.

"""django 视图类
class UserProfileListView(View):
    def get(self, request):
        
        #通过 django 的 view 实现人员信息列表
        :param request:
        :return:
        json_list = []
        users = UserProfile.objects.all()[:10]

        序列化json load 再 dump
        # import json
        # from django.core import serializers
        # json_data = serializers.serialize("json", users)
        # json_data = json.loads(json_data)
        # from django.http import HttpResponse
        # return HttpResponse(json.dumps(json_data), content_type="application/json")
        
        #序列化json 不做转化
        import json
        from django.core import serializers
        json_data = serializers.serialize("json", users)
        from django.http import HttpResponse
        return HttpResponse(json_data, content_type="application/json")
        
        # jsonresponse
        import json
        from django.core import serializers
        json_data = serializers.serialize("json", users)
        json_data = json.loads(json_data)  # 这里转换成 dict
        from django.http import JsonResponse  # json.dumps() 转换成 字符串
        return JsonResponse(json_data, safe=False)
"""
"""使用apiview视图"""
# class UserProfileListView(APIView):
#     """ List all users """
#     def get(self, request, format=None):
#             users = UserProfile.objects.all()[:10]
#             users_serializer = UserProfileSerializer(users, many=True)
#             return Response(users_serializer.data)
#
#     def post(self, request, format=None):
#         serializer = UserProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""使用generics.GenericAPIView"""
# class UserProfileListView(mixins.ListModelMixin, generics.GenericAPIView):
#     """ 用户列表 """
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

"""分页实现"""
# class UserProfilePagination(PageNumberPagination):
# #     page_size = 10
# #     page_size_query_param = 'page_size'
# #     page_query_param = 'p'
# #     max_page_size = 100
# #
# #
# # class UserProfileListView(generics.ListAPIView):
# #     """ 用户列表页 """
# #     queryset = UserProfile.objects.all()[:5]
# #     serializer_class = UserProfileSerializer
# #     pageination_class = UserProfileSerializer

"""使用vieset"""
# class UserProfileListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """ 商品列表页 """
#     queryset = UserProfile.objects.all()[:10]
#     serializer_class = UserProfileSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):

"""使用过虑器"""
# class UserProfilePagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     page_query_param = 'p'
#     max_page_size = 100

"""搜索"""
# class UserProfileListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """ 用户列表 """
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#     pageination_class = UserProfilePagination
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter)
#     filter_class = UserProfileFilter
#     search_fields = ('id', 'name')

# class UserProfileListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """ 用户列表页，分页，搜索，过滤，排序 """
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#     pageination_class = UserProfilePagination
#     # authentication_classes = (TokenAuthentication,)
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
#     filter_class = UserProfileFilter
#     search_fields = ('name', 'id')
#     ordering_fields = ('id', 'name')

# class CustomBackend(ModelBackend):
#     """ 自定义用户验证 """
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(Q(username=username) | Q(email=username))
#             if user.check_password(password):
#                 return user
#         except Exception as e:
#             return None

"""ViewSet类"""

# from django.shortcuts import get_object_or_404
# from .serializers import UserProfileSerializer
# from rest_framework import viewsets
# from rest_framework.response import Response
#
# class UserProfileViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     # def list(self, request):
#     #     queryset = UserProfile.objects.all()
#     #     serializer = UserProfileSerializer(queryset, many=True)
#     #     return Response(serializer.data)
#     #
#     # def retrieve(self, request, pk=None):
#     #     queryset = UserProfile.objects.all()
#     #     user = get_object_or_404(queryset, pk=pk)
#     #     serializer = UserProfileSerializer(user)
#     #     return Response(serializer.data)
#
#     def list(self, request):
#         pass
#
#     def create(self, request):
#         pass
#
#     def retrieve(self, request, pk=None):
#         pass
#
#     def update(self, request, pk=None):
#         pass
#
#     def partial_update(self, request, pk=None):
#         pass
#
#     def destroy(self, request, pk=None):
#         pass
#
#     def get_permissions(self):
#         """
#         Instantiates and returns the list of permissions that this view requires.
#         """
#         if self.action == 'list':
#             permission_classes = [IsAuthenticated]
#         else:
#             permission_classes = [IsAdmin]
#         return [permission() for permission in permission_classes]

"""View类使用装饰器"""
# from rest_framework import status, viewsets
# # from rest_framework.decorators import action
# # from rest_framework.response import Response
# # from .serializers import UserProfileSerializer, PasswordSerializer
# #
# # class UserViewSet(viewsets.ModelViewSet):
# #     """
# #     A viewset that provides the standard actions
# #     """
# #     queryset = UserProfile.objects.all()
# #     serializer_class = UserProfileSerializer
# #
# #     @action(detail=True, methods=['post'])
# #     def set_password(self, request, pk=None):
# #         user = self.get_object()
# #         serializer = PasswordSerializer(data=request.data)
# #         if serializer.is_valid():
# #             user.set_password(serializer.data['password'])
# #             user.save()
# #             return Response({'status': 'password set'})
# #         else:
# #             return Response(serializer.errors,
# #                             status=status.HTTP_400_BAD_REQUEST)
# #
# #     @action(detail=False)
# #     def recent_users(self, request):
# #         recent_users = UserProfile.objects.all().order_by('-last_login')
# #
# #         page = self.paginate_queryset(recent_users)
# #         if page is not None:
# #             serializer = self.get_serializer(page, many=True)
# #             return self.get_paginated_response(serializer.data)
# #
# #         serializer = self.get_serializer(recent_users, many=True)
# #         return Response(serializer.data)
# #
# #     @action(detail=True, methods=['post'], permission_classes=[IsAdminOrIsSelf])
# #     def set_password(self, request, pk=None):
# #         psss
# #
# #     @action(detail=True, methods=['put'], name='Change Password')
# #     def password(self, request, pk=None):
# #         """Update the user's password."""
# #         pass
# #
# #     @password.mapping.delete
# #     def delete_password(self, request, pk=None):
# #         """Delete the user's password."""
# #         pass

"""ModelView"""
class UserProfileViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAccountAdminOrReadOnly]
