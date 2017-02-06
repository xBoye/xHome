from django.conf.urls import url

from . import views

urlpatterns = [
	# 算法algorithm
	url(r'^algorithm', views.algorithm, name='algorithm'),
	
	# 黑洞数blackholenumbers
	url(r'^blackholenumbers', views.blackholenumbers, name='blackholenumbers'),
	
	# 寻找黑洞数findblackholenumbers
	url(r'^findblackholenumbers', views.findblackholenumbers, name='findblackholenumbers'),
	
]
