# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from yi.models import Yi, Yilin
from yi.forms import YiForm, YilinForm

def justatry(request):
	"""试一试"""
	return render(request, 'justatry/justatry.html')	