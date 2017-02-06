from django.conf.urls import url

from . import views

urlpatterns = [
	# 主页
	url(r'^divination', views.divination, name='divination'),
	url(r'^divining', views.divining, name='divining'),
	
	# 地藏占察
	url(r'^ksitiscry/$', views.ksitiscry, name='ksitiscry'),
	
	
	# 观音签Avalokiteśvara
	url(r'^avalokiscry', views.avalokiscry, name='avalokiscry'),
	url(r'^find', views.find, name='find'),
]
