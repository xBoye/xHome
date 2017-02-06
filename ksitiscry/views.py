# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Ksitiscry, Avalokiscry
from yi.models import Yi, Yilin

from django.contrib.auth.decorators import login_required

def divination(request):
	"""占卜学"""
	entries = Ksitiscry.objects.all().order_by('id')
	context = {'entries' : entries}
	return render(request, 'ksitiscry/divination.html', context)

import random	
def divining(request):
	"""任意占卜"""
	yi = Yi.objects.get(id=random.randint(1,64))
	bi = random.randint(0,6)   #变爻
	if bi==0:
		yi_entry = yi.gci
	elif bi==1:
		yi_entry = yi.y1
	elif bi==2:
		yi_entry = yi.y2
	elif bi==3:
		yi_entry = yi.y3
	elif bi==4:
		yi_entry = yi.y4
	elif bi==5:
		yi_entry = yi.y5
	elif bi==6:
		yi_entry = yi.y6
	yi_entry = '(' + str(yi.id) + ')' + yi.gname + '：' + yi_entry + '(易占)'
	
	yl = Yilin.objects.get(id=random.randint(1,4096))
	yl_entry = '(' + str(yl.id) + ')' + yl.jname + '：' + yl.jci + '(易林占)'
	
	ks = Ksitiscry.objects.get(id=random.randint(1,189))
	ks_entry = '(' + str(ks.id) + ')' + ks.kci + '。(地藏占)'
	
	av = Avalokiscry.objects.get(id=random.randint(1,100))
	av_entry = '(' + str(av.id) + ')' + '(' + av.signtype + ')' + '(' + av.signmetaphor+ ')' + '【' + av.signpoem + '】' + '(观音签)'
	
	return render(request, 'ksitiscry/divination.html', {'yi_entry':yi_entry, 'yl_entry':yl_entry, 'ks_entry':ks_entry, 'av_entry':av_entry})
	
@login_required
def ksitiscry(request):
	"""地藏占察"""
	entries = Ksitiscry.objects.all().order_by('id')
	context = {'entries' : entries}
	return render(request, 'ksitiscry/ksitiscry.html', context)

def avalokiscry(request):
	"""观音签"""
	return render(request, 'ksitiscry/avalokiscry.html')
	
import random	
def find(request):
	"""搜索可能性"""
	
	avk = Avalokiscry.objects.get(id=random.randint(1,100))
	avk_entry = '(' + str(avk.id) + ')' + avk.signtype + '【' + avk.signmetaphor +'】' + avk.signpoem + '(观音签)'
	
	return render(request, 'ksitiscry/avalokiscry.html', {'avk_entry':avk_entry})