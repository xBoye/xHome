from django.conf.urls import url

from . import views

urlpatterns = [
	# 离散数学lisan
	url(r'^lisan', views.lisan, name='lisan'),
	
	
]
