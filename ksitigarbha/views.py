# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Ksitiscry
#from .forms import YiForm, YilinForm

# Create your views here.

def ksitiscry(request):
	"""地藏占察"""
	entries = Ksitiscry.objects.all().order_by('id')
	context = {'entries' : entries}
	return render(request, 'ksitigarbha/ksitiscry.html', context)

