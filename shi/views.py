# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from yi.models import Yi, Yilin
#from .forms import YiForm, YilinForm

# Create your views here.

def shi(request):
	"""诗词馆shi"""
	return render(request, 'shi/shi.html')	