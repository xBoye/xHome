from django.conf.urls import url

from . import views

urlpatterns = [
	# 主页
	url(r'^$', views.centres, name='centres'),
	
	# 分发中心
	url(r'^centres/$', views.centres, name='centres'),
	
]
