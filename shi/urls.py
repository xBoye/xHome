from django.conf.urls import url

from . import views

urlpatterns = [
	# 地藏占察
	url(r'^shi$', views.shi, name='shi'),
	
]
