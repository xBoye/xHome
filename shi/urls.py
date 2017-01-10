from django.conf.urls import url

from . import views

urlpatterns = [
	# 诗词馆
	url(r'^shi$', views.shi, name='shi'),
	
]
