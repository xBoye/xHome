from django.conf.urls import url

from . import views

urlpatterns = [
	# 主页
	#url(r'^$', views.index, name='index'),
	
	# 试一试
	url(r'^justatry$', views.justatry, name='justatry'),
]