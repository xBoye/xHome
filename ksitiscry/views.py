# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Ksitiscry
from django.contrib.auth.decorators import login_required

@login_required
def ksitiscry(request):
	"""地藏占察"""
	entries = Ksitiscry.objects.all().order_by('id')
	context = {'entries' : entries}
	return render(request, 'ksitiscry/ksitiscry.html', context)

