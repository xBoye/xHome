# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Yi, Yilin
from .forms import YiForm, YilinForm

def index(request):
	"""周易悦读主页"""
	return render(request, 'yi/index.html')

def yis(request):
	"""显示周易列表"""
	yis = Yi.objects.order_by('id')
	context = {'yis' : yis}
	return render(request, 'yi/yis.html', context)

def yi(request, yi_id):
	"""显示某卦及关联易林卦"""
	yi = Yi.objects.get(id=yi_id)

	yilins = yi.yilin_set.order_by('id')
	context = {'yi' : yi, 'yilins' : yilins}
	return render(request, 'yi/yi.html', context)

def yi_detail(request, yi_id):
	"""显示易卦详细"""
	yi = Yi.objects.get(id=yi_id)

	context = {'yi' : yi}
	return render(request, 'yi/yi_detail.html', context)
	
def yilin_detail(request, yilin_id):
	"""显示易林卦详细"""
	yilin = Yilin.objects.get(id=yilin_id)

	context = {'yilin' : yilin}
	return render(request, 'yi/yilin_detail.html', context)

def new_yi(request):
	"""添加新卦"""
	if request.method != 'POST':
		#未提交数据：创建一个新表单
		form = YiForm()
		
	else:
		#POST提交的数据，对数据进行处理
		form = YiForm(request.POST)
		if form.is_valid():
			new_yi = form.save(commit=False)
			new_yi.save()
			return HttpResponseRedirect(reverse('yi:yis'))
			
	context = {'form':form}
	return render(request,'yi/new_yi.html', context)

	
def yilins(request):
	"""显示焦氏易林列表"""
	yilins = Yilin.objects.order_by('id')
	context = {'yilins' : yilins}
	return render(request, 'yi/yilins.html', context)
	
def new_yilin(request, yi_id):
	"""某卦添加易林之卦"""
	yi = Yi.objects.get(id=yi_id)
	
	if request.method != 'POST':
		#未提交数据：创建一个新表单
		form = YilinForm()
	else:
		#POST提交的数据，对数据进行处理
		form = YilinForm(data=request.POST)
		if form.is_valid():
			new_yilin = form.save(commit=False)
			new_yilin.yi = yi
			new_entry.save()
			return HttpResponseRedirect(reverse('yi:yi',args=[yi_id]))
			
	context = {'yi': yi, 'form': form}
	return render(request,'yi/new_yilin.html', context)
	
def edit_yi(request, yi_id):
	"""编辑易经卦目"""
	yi = Yi.objects.get(id=yi_id)
	
	if request.method != 'POST':
		#初次请求，以当前条目填充表单
		form = YiForm(instance=yi)
	else:
		#POST提交的数据，对数据进行处理
		form = YiForm(instance=yi, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('yi:yis'))
			
	context = {'yi': yi, 'form': form}
	return render(request,'yi/edit_yi.html', context)


def edit_yilin(request, yilin_id):
	"""编辑易林卦目"""
	yilin = Yilin.objects.get(id=yilin_id)
	yi = yilin.yi
	
	if request.method != 'POST':
		#初次请求，以当前条目填充表单
		form = YilinForm(instance=yilin)
	else:
		#POST提交的数据，对数据进行处理
		form = YilinForm(instance=yilin, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('yi:yi',args=[yi.id]))
			
	context = {'yilin': yilin, 'yi': yi, 'form': form}
	return render(request,'yi/edit_yilin.html', context)
