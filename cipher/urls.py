from django.conf.urls import url

from . import views

urlpatterns = [
	# 密码学
	url(r'^cipher', views.cipher, name='cipher'),
	
	url(r'^message_digest', views.message_digest, name='message_digest'),
	url(r'^digital_signature', views.digital_signature, name='digital_signature'),
	
]
