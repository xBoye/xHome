from django.conf.urls import url

from . import views

urlpatterns = [
	# 主页
	url(r'^$', views.centres, name='centres'),
	
	# 分发中心
	url(r'^centres/$', views.centres, name='centres'),
	
	# 文件上传
	url(r'^upload/$', views.upload, name='upload'),
	url(r'^uploadfile/$', views.uploadfile, name='uploadfile'),
	
]
