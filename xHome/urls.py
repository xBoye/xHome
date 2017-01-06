from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/$', include(admin.site.urls)),
	
	# 应用yi
	url(r'',include('yi.urls', namespace='yi')),

]
