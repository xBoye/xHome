from django.conf.urls import url

from . import views

urlpatterns = [
	# 文本挖掘
	url(r'^text_mining$', views.text_mining, name='text_mining'),
		url(r'^uploadfile', views.uploadfile, name='uploadfile'),
	
	# 字频统计
	url(r'^word_degrees', views.word_degrees, name='word_degrees'),
	
	# 字词组库
	url(r'^wordslab$', views.wordslab, name='wordslab'),
	
	# 单字计数
	url(r'^wordcounts', views.wordcounts, name='wordcounts'),
	
	# test_wordcounts
	url(r'^test_wordcounts', views.test_wordcounts, name='test_wordcounts'),
	
	# 人物统计
	url(r'^name_degrees', views.name_degrees, name='name_degrees'),
	
	# 任意查询
	url(r'^any_search', views.any_search, name='any_search'),
	#url(r'^any_search_fuwu/$', views.any_search_fuwu, name='any_search_fuwu'),
	
	
]
