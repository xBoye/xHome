# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def text_mining(request):
	"""文本挖掘text_mining"""
	return render(request, 'text_mining/text_mining.html')	