from django.conf.urls import url

from . import views

urlpatterns = [
	# 主页
	url(r'^$', views.index, name='index'),
	#url(r'^$', views.yis, name='yis'),
	
	# 试一试
	url(r'^try/$', views.just_a_try, name='just_a_try'),
	
	# 显示周易列表
	url(r'^yis/$', views.yis, name='yis'),
	
	# 显示易卦详细
	url(r'^yis_detail/(?P<yi_id>\d+)/$', views.yi_detail, name='yi_detail'),
	
	# 添加易经新卦
	url(r'^new_yi/$', views.new_yi, name='new_yi'),
	
	# 显示某卦及关联易林所有之卦
	url(r'^yis/(?P<yi_id>\d+)/$', views.yi, name='yi'),
	
	# 显示易林卦目列表
	url(r'^yilins/$', views.yilins, name='yilins'),
	
	# 显示易林卦详细
	url(r'^yilins_detail/(?P<yilin_id>\d+)/$', views.yilin_detail, name='yilin_detail'),

	# 添加易林新卦
	url(r'^new_yilin/(?P<yi_id>\d+)/$', views.new_yilin, name='new_yilin'),
	
	# 编辑易经卦目
	url(r'^edit_yi/(?P<yi_id>\d+)/$', views.edit_yi, name='edit_yi'),
	
	# 编辑易林卦目
	url(r'^edit_yilin/(?P<yilin_id>\d+)/$', views.edit_yilin, name='edit_yilin'),

]
