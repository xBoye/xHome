# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def data_analysis(request):
	"""数据分析data_analysis"""
	return render(request, 'data_analysis/data_analysis.html')	