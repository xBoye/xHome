from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # 系统管理
	url(r'^admin/', include(admin.site.urls)),
	
	# 用户登录users
	url(r'^users/', include('users.urls', namespace='users')),
	
	# 我的应用yi
	url(r'',include('yi.urls', namespace='yi')),

]
