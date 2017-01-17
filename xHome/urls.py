from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	# 系统管理
	url(r'^admin/', include(admin.site.urls)),
	
	# 管理中心
	url(r'', include('centres.urls', namespace='centres')),
	url(r'^centres/', include('centres.urls', namespace='centres')),
	
	# 用户登录users
	url(r'^users/', include('users.urls', namespace='users')),
	
	# 应用yi
	url(r'^yi/', include('yi.urls', namespace='yi')),
	
	# 文本挖掘text_mining
	url(r'^text_mining/', include('text_mining.urls', namespace='text_mining')),
	
	# 数据分析
	url(r'^data_analysis/', include('data_analysis.urls', namespace='data_analysis')),
	
	# 应用诗词馆shi
	url(r'^shi/',include('shi.urls', namespace='shi')),
	
	# 应用地藏占察ksitiscry
	url(r'^ksitiscry/',include('ksitiscry.urls', namespace='ksitiscry')),
	
	# 试一试try
	url(r'^try/',include('try.urls', namespace='try')),

]
