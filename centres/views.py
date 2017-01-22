# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def centres(request):
	#Python练习项目管理中心Center
	return render(request, 'centres/centres.html')

def upload(request):
	#文件上传
	return render(request, 'centres/upload.html')


def uploadfile(request):  
	import os
	if request.method == "POST":    # 请求方法为POST时，进行处理  
		myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
		if not myFile: 		
			#return HttpResponse("no files for upload!")
			return render(request, 'centres/upload.html',{'what':'no file for upload!'})
		upfile = open(os.path.join("D:\\xHome\\data\\upload",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作  
		for chunk in myFile.chunks():      # 分块写入文件  
			upfile.write(chunk)  
		upfile.close()  
		#return HttpResponse("upload over!")
		return render(request, 'centres/upload.html', {'what':'upload over!'})