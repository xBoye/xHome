from django.conf.urls import url

from . import views

urlpatterns = [
	# 地藏占察
	url(r'^ksitigarbha$', views.ksitigarbha, name='ksitigarbha'),
	
]
