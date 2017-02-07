# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from text_mining.models import Words, Results

from centres.views import uploadfile

def text_mining(request):
	"""文本挖掘text_mining"""
	return render(request, 'text_mining/text_mining.html')

def word_degrees(request):
	"""字频统计"""
	return render(request, 'text_mining/word_degrees.html')

	
def wordslab(request):
	"""字词组库"""
	return render(request, 'text_mining/wordslab.html')
	
def name_degrees(request):
	"""人物统计"""
	return render(request, 'text_mining/name_degrees.html')
	
def anysearch(request):
	"""任意查询"""
	return render(request, 'text_mining/anysearch.html')
	

	
def uploadfile(request):  
	import os
	if request.method == "POST":    # 请求方法为POST时，进行处理  
		myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
		if not myFile: 		
			#return HttpResponse("no files for upload!")
			return render(request, 'text_mining/text_mining.html',{'what':'no file for upload!'})
		upfile = open(os.path.join("D:\\xHome\\data\\upload",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作  
		for chunk in myFile.chunks():      # 分块写入文件  
			upfile.write(chunk)  
		upfile.close()  
		#return HttpResponse("upload over!")
		return render(request, 'text_mining/text_mining.html', {'what':'upload over!'})
	
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
	
	repl = '[，：。？∶:;！（）、=《》’‘“\'"\r\n\s )ばhＮB0℃zＧｎｂｄｃ□ｊｔYoｙt／_Ａp@ -Luｌ；bｕ·yie．dｅ３a「２nF,＠Ｖｋ＜＞ｒｐｉ【】『』ｇｏjａ/2┦ｘ\sZ(＝（）ｖΥw”TW○乙－Ｔ￣１Ｑ８Ｓ０s,r＂Ｆ─0123456789―７６４…cxl]'
		
	d={}
	results =Results.objects.filter(textbook=book)
	
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
		Results(textbook=book, summary=results).save()	
		
		d=sorted(d.items(),key=lambda a:a[1],reverse=True)
		id = 1
		for l in d:
			Words(name=l[0], degrees=l[1], textbook=book).save()
	
	results =Results.objects.filter(textbook=book).values('textbook','summary').distinct()[0]
	
	data = Words.objects.filter(textbook=book)[0:20]
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
	results =Results.objects.filter(textbook=book)
	
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
		Results(textbook=book, summary=results).save()	
		
		d=sorted(d.items(),key=lambda a:a[1],reverse=True)
		id = 1
		for l in d:
			Words(name=l[0], degrees=l[1], textbook=book).save()
	
	results =Results.objects.filter(textbook=book).values('textbook','summary').distinct()[0]
	
	data = Words.objects.filter(textbook=book)[0:20]
	context = {'results':results, 'data':data}

	return render_to_response('text_mining/results.html', context)

	
def searchservice(request):
	"""任意查询后台服务"""
	import os,re
	what = ''
	
	if request.method == "POST":    # 请求方法为POST时，进行处理 
		getfile =request.FILES.get("upfile", None)    # 获取上传的文件，如果没有文件，则默认为None
		content = request.POST['content']
		print(content)
		if not getfile: 		
			#return HttpResponse("no files for upload!")
			return render(request, 'text_mining/anysearch.html',{'what':'未选择文件!'})
		
		book = getfile.name.split('.')[0]
		print('book：',book)
		fin = os.path.join("D:\\xHome\\data\\upload",getfile.name)
		print(fin)
		what = '【%s】文件已存在！' %(getfile.name)
		if not os.path.exists(fin):
			bfile = open(fin,'wb+')    # 打开特定的文件进行二进制的写操作  
			for chunk in getfile.chunks():      # 分块写入文件  
				bfile.write(chunk)  
			bfile.close() 
			what = '【%s】文件已上传！' %(getfile.name)

	content = request.POST['content']
	#print('content:',content)
	dls = '[,\-\.，##。；：;:、|]'
	content = re.sub(dls, '|', content)
	print('content:',content)
	#fin = 'D:\\xHome\\data\\upload\\test.txt'
	d = {}
	try:
		with open(fin, 'r', encoding='utf-8') as infile:
			mbook = infile.read()
			mbook = re.sub('[\r\n]','',mbook)
			#print(mbook)
			l = re.findall(content, mbook)
			for k in l:
				if k in d:
					d[k] += 1
				else:
					d.update({k:1})
			print(d)	
			
	except IOError:
		print('File error..')
	
	d=sorted(d.items(),key=lambda a:a[1],reverse=True)
	what = d
	title = '关键词在文本《%s》中出现频度为：' %(book)
	context = {'title':title,'what':what}
	return render(request, 'text_mining/anysearch.html', context)
	
"""
d = {}

try:
	with open(fin, 'r', encoding='utf-8') as in_file:
		for f in in_file:
			l=re.findall(repl,f)
			for k in l:
				if k in d:
					d[k] += 1
				else:
					d.update({k:1})
except IOError:
	print('File error..')

d=sorted(d.items(),key=lambda a:a[1],reverse=True)

id = 1
try:
	with open(fout, 'w', encoding='utf-8') as out_file:
		#print('《天龙八部》人物出现频次排名(Top40)\n序号,名字,频度')
		#print('《射雕英雄传》降龙十八掌出招频度\n序号,招式,频度')
		#print('《神雕侠侣》降龙十八掌出招频度\n序号,招式,频度')
		
		print('《笑傲江湖》人物频度排名(Top40)\n序号,名字,频度')
		print('id,name,degrees', file=out_file)
		for l in d:
			print(str(id)+','+l[0]+','+str(l[1]))
			print(str(id)+','+l[0]+','+str(l[1]), file=out_file)
			id += 1
except IOError:
	print('File error..')
	
"""