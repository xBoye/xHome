# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def lisan(request):
	"""离散数学lisan"""
	return render(request, 'lisan/lisan.html')