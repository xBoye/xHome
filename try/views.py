# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from yi.models import Yi, Yilin
from ksitiscry.models import Ksitiscry

@login_required
def just_a_try(request):
	"""试一试"""
	return render(request, 'try/try.html')	

import random	
def find(request):
	"""搜索可能性"""
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
	
	return render(request, 'try/try.html', {'yi_entry':yi_entry, 'yl_entry':yl_entry, 'ks_entry':ks_entry})