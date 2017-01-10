from django.conf.urls import url

from . import views

urlpatterns = [
	# 试一试
	url(r'^try$', views.just_a_try, name='try'),
]