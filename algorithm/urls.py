from django.conf.urls import url

from . import views

urlpatterns = [
	# 算法algorithm
	url(r'^algorithm', views.algorithm, name='algorithm'),
	
	
]
