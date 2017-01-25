from django.conf.urls import url

from . import views

urlpatterns = [
	# 文本挖掘
	url(r'^text_mining$', views.text_mining, name='text_mining'),
	
	# 词库
	url(r'^wordslab$', views.wordslab, name='wordslab'),
	
	# 单字计数
	url(r'^wordcounts', views.wordcounts, name='wordcounts'),
	
	# test_wordcounts
	url(r'^test_wordcounts', views.test_wordcounts, name='test_wordcounts'),
	
]
