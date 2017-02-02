# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Ksitiscry, Avalokiscry
from django.contrib.auth.decorators import login_required

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