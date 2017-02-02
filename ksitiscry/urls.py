from django.conf.urls import url

from . import views

urlpatterns = [
	# 地藏占察
	url(r'^ksitiscry/$', views.ksitiscry, name='ksitiscry'),
	
	# 观音签Avalokiteśvara
	url(r'^avalokiscry', views.avalokiscry, name='avalokiscry'),
	url(r'^find', views.find, name='find'),
]
