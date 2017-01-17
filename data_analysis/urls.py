from django.conf.urls import url

from . import views

urlpatterns = [
	# 数据分析
	url(r'^data_analysis$', views.data_analysis, name='data_analysis'),
	
]
