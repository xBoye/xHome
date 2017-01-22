from django.conf.urls import url

from . import views

urlpatterns = [
	# 区块链blockchain
	url(r'^blockchain\$', views.blockchain, name='blockchain'),
	
]
