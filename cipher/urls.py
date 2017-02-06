from django.conf.urls import url

from . import views

urlpatterns = [
	# 密码学
	url(r'^cipher', views.cipher, name='cipher'),
	
	# 密码生成
	url(r'^makersakeys', views.makersakeys, name='makersakeys'),
	
	# 消息摘要及数字签名
	url(r'^message_digest', views.message_digest, name='message_digest'),
	url(r'^digital_signature', views.digital_signature, name='digital_signature'),
	
]
