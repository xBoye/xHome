from django.conf.urls import url

from . import views

urlpatterns = [
	# 单元测试
	url(r'^utest$', views.utest, name='utest'),
]
