# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from text_mining.models import Words, Results

from centres.views import uploadfile

def text_mining(request):
	"""文本挖掘text_mining"""
	return render(request, 'text_mining/text_mining.html')
	
def wordslab(request):
	"""词库words"""
	return render(request, 'text_mining/wordslab.html')
	
def test_wordcounts(request):
	"""单字计数"""
	import os
	if request.method == "POST":    # 请求方法为POST时，进行处理 
		upFile =request.FILES.get("upfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
		if not upFile: 		
			#return HttpResponse("no files for upload!")
			return render(request, 'text_mining/text_mining.html',{'what':'未选择文件做字频统计!'})
		book = upFile.name
		upfile = open(os.path.join("D:\\xHome\\data\\upload",upFile.name),'wb+')    # 打开特定的文件进行二进制的写操作  
		for chunk in upFile.chunks():      # 分块写入文件  
			upfile.write(chunk)  
		upfile.close()  

	"""字频统计"""
	import re

	fin = os.path.join("D:\\xHome\\data\\upload",upFile.name)
	book = book.split('.')[0]   #书名
	
	repl = '[，：。？∶:;！（）、=《》’‘“\'"\r\n\s )ばhＮB0℃zＧｎｂｄｃ□ｊｔYoｙt／_Ａp@ -Luｌ；bｕ·yie．dｅ３a「２nF,＠Ｖｋ＜＞ｒｐｉ【】『』ｇｏjａ/2┦ｘ\sZ(＝（）ｖΥw”TW○乙－Ｔ￣１Ｑ８Ｓ０s,r＂Ｆ─]'
		
	d={}
	results =Results.objects.filter(item=book)
	
	if len(results)==0:
		with open(fin, 'r', encoding='utf-8') as in_file:
			for l in in_file:
				l = list(re.sub(repl,'',l))
				for k in l:
					if k in d:
						d[k] += 1
					else:
						d.update({k:1})
		results = book + '总字数为：' + str(sum(list((d.values())))) + '；不重复字数为：'+str(len(d))
		Results(item=book, summary=results).save()	
		
		d=sorted(d.items(),key=lambda a:a[1],reverse=True)
		id = 1
		for l in d:
			Words(name=l[0], degrees=l[1], isfrom=book).save()
	
	results =Results.objects.filter(item=book).values('item','summary').distinct()[0]
	
	data = Words.objects.filter(isfrom=book)[0:20]
	what = '《' + book + '》' + '已经上传！'
	context = {'results':results, 'data':data, 'what':what}

	return render_to_response('text_mining/results.html', context)		

def wordcounts(request):
	"""单字计数"""
	import os, re

	fin = "d:\\xhome\\data\\text_mining\\鹿鼎记.txt"
	book=os.path.split(fin)[1].split('.')[0]   #书名
	
	repl = '[，：。？∶:;！（）、=《》’‘“\'"\r\n\s )ばhＮB0℃zＧｎｂｄｃ□ｊｔYoｙt／_Ａp@ -Luｌ；bｕ·yie．dｅ３a「２nF,＠Ｖｋ＜＞ｒｐｉ【】『』ｇｏjａ/2┦ｘ\sZ(＝（）ｖΥw”TW○乙－Ｔ￣１Ｑ８Ｓ０s,r＂Ｆ─]'
		
	d={}
	results =Results.objects.filter(item=book)
	
	if len(results)==0:
		with open(fin, 'r', encoding='utf-8') as in_file:
			for l in in_file:
				l = list(re.sub(repl,'',l))
				for k in l:
					if k in d:
						d[k] += 1
					else:
						d.update({k:1})
		results = book + '总字数为：' + str(sum(list((d.values())))) + '；不重复字数为：'+str(len(d))
		Results(item=book, summary=results).save()	
		
		d=sorted(d.items(),key=lambda a:a[1],reverse=True)
		id = 1
		for l in d:
			Words(name=l[0], degrees=l[1], isfrom=book).save()
	
	results =Results.objects.filter(item=book).values('item','summary').distinct()[0]
	
	data = Words.objects.filter(isfrom=book)[0:20]
	context = {'results':results, 'data':data}

	return render_to_response('text_mining/results.html', context)