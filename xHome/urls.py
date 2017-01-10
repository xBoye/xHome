from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # 系统管理
	url(r'^admin/', include(admin.site.urls)),
	
	# 用户登录users
	url(r'^users/', include('users.urls', namespace='users')),
	
	# 应用yi
	url(r'',include('yi.urls', namespace='yi')),
	
	# 应用诗词馆shi
	url(r'^shi/',include('shi.urls', namespace='shi')),
	
	# 应用地藏占察ksitiscry
	url(r'^ksitiscry/',include('ksitiscry.urls', namespace='ksitiscry')),
	
	# 试一试try
	url(r'^try/',include('try.urls', namespace='try')),

]
