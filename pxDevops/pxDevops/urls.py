"""pxDevops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.conf.urls import url
import xadmin
from xadmin.plugins import xversion
xadmin.autodiscover()
xversion.register_models()
from users.views_base import UserProfileListView
from users.views import UserProfileViewSet
from rest_framework.documentation import include_docs_urls
# from users.views import UserProfileListView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
# # 配置user_list的url
# router.register('users', UserProfileListViewSet, base_name='users')
router.register('users', UserProfileViewSet, base_name='users')
# router.register('cmdb', )
# users_list = UserProfileListViewSet.as_view({
#     'get': 'list'
# })


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url('api-token-auth/', views.obtain_auth_token),
    url('api-token-auth/', obtain_jwt_token),
    # 人员信息
    # url('users/$', UserProfileListView.as_view(), name="users-list"),
    # url('users/$', users_list, name="users-list"),
    url('docs/', include_docs_urls(title="运维平台")),
    url('', include(router.urls)),
    url('login/', obtain_jwt_token),
]

# urlpatterns += [
#     url(r'^api-token-auth/', views.obtain_auth_token)
# ]