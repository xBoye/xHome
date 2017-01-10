from django.conf.urls import url

from . import views

urlpatterns = [
	# 地藏占察
	url(r'^ksitiscry$', views.ksitiscry, name='ksitiscry'),
	
]
